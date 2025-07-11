import grpc
import os
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from google.protobuf.timestamp_pb2 import Timestamp

# Import generated proto files
from generated.admin import admin_margin_manager_pb2
from generated.admin import admin_margin_manager_service_pb2_grpc
from generated import time_machine_pb2
from generated.api_hub import api_hub_service_pb2_grpc
from generated import pmbp_pb2
from generated import search_pb2
from generated import alerts_pb2
from generated import alerts_service_pb2_grpc
from generated import alerts_enums_pb2

logger = logging.getLogger(__name__)

class SarnaGRPCClient:
    def __init__(self, url: Optional[str] = None, jwt_token: Optional[str] = None):
        self.channel = None
        self.connected = False
        # Try to use RISK_SYSTEM_HOST if SARNA_API_URL is not set
        if url:
            self.api_url = url
        else:
            host = os.getenv("RISK_SYSTEM_HOST", os.getenv("SARNA_API_URL", "api.stage.sarnafinance.com"))
            port = os.getenv("RISK_SYSTEM_PORT", "443")
            self.api_url = f"{host}:{port}" if ":" not in host else host
        self.jwt_token = jwt_token or os.getenv("SARNA_JWT_TOKEN", "") or os.getenv("RISK_API_KEY", "")
        
    async def connect(self):
        """Establish connection to Sarna gRPC API."""
        try:
            # Use secure channel with default SSL credentials
            logger.info(f"Connecting to Sarna API at {self.api_url}")
            self.channel = grpc.aio.secure_channel(
                self.api_url,
                grpc.ssl_channel_credentials()
            )
            
            # Wait for channel to be ready
            await self.channel.channel_ready()
            self.connected = True
            logger.info("Successfully connected to Sarna API")
            
        except Exception as e:
            logger.error(f"Failed to connect to Sarna API: {e}")
            raise
    
    async def disconnect(self):
        """Close the gRPC channel."""
        if self.channel:
            await self.channel.close()
            self.connected = False
            logger.info("Disconnected from Sarna API")
    
    async def close(self):
        """Alias for disconnect to match expected interface."""
        await self.disconnect()
    
    def _get_metadata(self):
        """Get metadata for authentication."""
        return [
            ("authorization", f"Bearer {self.jwt_token}"),
        ]
    
    async def get_margin_data(self, group_id: int) -> Dict[str, Any]:
        """Fetch margin data for a specific account group."""
        if not self.connected:
            raise RuntimeError("Not connected to Sarna API")
        
        try:
            # Create stub
            stub = admin_margin_manager_service_pb2_grpc.AdminMarginManagerServiceStub(self.channel)
            
            # Create request
            request = admin_margin_manager_pb2.MarginManagerRequest()
            
            # Set up portfolio request for the account group
            portfolio_request = admin_margin_manager_pb2.MarginManagerPortfolioRequest()
            portfolio_request.AccountGroupIds.append(group_id)
            portfolio_request.FetchAllAccounts = True  # Use True to get all accounts in group
            portfolio_request.NumberOfScenarios = 11  # Default scenarios
            portfolio_request.UnderlyingPriceShockPercentDown = 0.08
            portfolio_request.UnderlyingPriceShockPercentUp = 0.06
            portfolio_request.IncludeOrders = True
            
            request.MarginManagerPortfolioRequest.CopyFrom(portfolio_request)
            
            # Make the call
            response = await stub.Get(request, metadata=self._get_metadata())
            
            # Convert response to dict format
            return self._convert_margin_response(response, group_id)
            
        except grpc.RpcError as e:
            logger.error(f"gRPC error fetching margin data: {e.code()} - {e.details()}")
            raise
        except Exception as e:
            logger.error(f"Error fetching margin data: {e}")
            raise
    
    async def get_current_margin_data(self, group_id: int) -> Dict[str, Any]:
        """Alias for get_margin_data to match expected interface."""
        return await self.get_margin_data(group_id)
    
    async def get_portfolio_with_risk_profile(self, group_id: int, risk_profile_id: int = 10011) -> Dict[str, Any]:
        """Fetch comprehensive portfolio data with risk profile and scenarios."""
        logger.info(f"=== get_portfolio_with_risk_profile called with group_id={group_id}, risk_profile_id={risk_profile_id} ===")
        
        if not self.connected:
            raise RuntimeError("Not connected to Sarna API")
        
        try:
            # Create stub
            stub = admin_margin_manager_service_pb2_grpc.AdminMarginManagerServiceStub(self.channel)
            
            # Create request
            request = admin_margin_manager_pb2.MarginManagerRequest()
            
            # Set up portfolio request EXACTLY matching the sample
            portfolio_request = admin_margin_manager_pb2.MarginManagerPortfolioRequest()
            
            # Set all fields in EXACT order from sample
            portfolio_request.NumberOfScenarios = 0
            portfolio_request.UnderlyingPriceShockPercentDown = 0
            portfolio_request.UnderlyingPriceShockPercentUp = 0
            portfolio_request.VolatilityShockPercentage = 0
            portfolio_request.VolatilityShockDirection = 3
            portfolio_request.ReturnOccStyleReportForPM = False
            portfolio_request.ReturnOccStyleInputForPM = False
            
            # Empty StressTestInput
            stress_test_input = pmbp_pb2.PmBpStressTestInput()
            portfolio_request.StressTestInput.CopyFrom(stress_test_input)
            
            portfolio_request.FetchAllAccounts = False
            portfolio_request.IncludeOrders = True
            portfolio_request.OptionPricingModel = 7
            
            # Apply risk profile ID
            portfolio_request.AppliedRiskProfileIds.append(risk_profile_id)
            
            portfolio_request.LotsAggregatorAlgo = 0
            
            # Add account group ID
            portfolio_request.AccountGroupIds.append(group_id)
            
            # RequirementAddOns - all false
            portfolio_request.RequirementAddOns.ApplyLowPricedStocksAddOn = False
            portfolio_request.RequirementAddOns.ApplyConcentrationAddOn = False
            portfolio_request.RequirementAddOns.ApplyLiquidityAddOn = False
            
            # SearchCriteria with Page info
            # TODO: Fix Page import issue - commenting out for now
            # search_criteria = search_pb2.SearchCriteria()
            # page = search_pb2.Page()
            # page.PageRequestId = ""
            # page.Page = 1
            # page.PageSize = 50
            # search_criteria.Page.CopyFrom(page)
            # portfolio_request.SearchCriteria.CopyFrom(search_criteria)
            
            # Log the complete request details
            logger.info(f"Portfolio request details:")
            logger.info(f"  AccountGroupIds: {list(portfolio_request.AccountGroupIds)}")
            logger.info(f"  AppliedRiskProfileIds: {list(portfolio_request.AppliedRiskProfileIds)}")
            logger.info(f"  NumberOfScenarios: {portfolio_request.NumberOfScenarios}")
            logger.info(f"  FetchAllAccounts: {portfolio_request.FetchAllAccounts}")
            logger.info(f"  IncludeOrders: {portfolio_request.IncludeOrders}")
            logger.info(f"  OptionPricingModel: {portfolio_request.OptionPricingModel}")
            logger.info(f"  VolatilityShockDirection: {portfolio_request.VolatilityShockDirection}")
            
            # Try to log the full request for debugging
            logger.debug(f"Full portfolio request: {portfolio_request}")
            
            request.MarginManagerPortfolioRequest.CopyFrom(portfolio_request)
            
            # Make the call
            response = await stub.Get(request, metadata=self._get_metadata())
            
            # Log response structure for debugging
            logger.info(f"Response has {len(response.MarginManagerInfo)} accounts")
            for account_id, margin_info in response.MarginManagerInfo.items():
                logger.debug(f"Account {account_id}: {margin_info.AccountNumber}")
                if margin_info.HasField("PmBpValuesResponse") and margin_info.PmBpValuesResponse.HasField("PmBpValues"):
                    logger.debug(f"  Has PM values data")
            
            # Convert to dict and preserve structure
            return {
                "group_id": group_id,
                "risk_profile_id": risk_profile_id,
                "MarginManagerInfo": self._convert_protobuf_to_dict(response.MarginManagerInfo)
            }
            
        except grpc.RpcError as e:
            logger.error(f"gRPC error fetching portfolio with risk profile: {e.code()} - {e.details()}")
            raise
        except Exception as e:
            logger.error(f"Error fetching portfolio with risk profile: {e}")
            raise
    
    def _convert_protobuf_to_dict(self, protobuf_obj) -> Any:
        """Recursively convert protobuf object to dict."""
        if isinstance(protobuf_obj, (list, tuple)):
            return [self._convert_protobuf_to_dict(item) for item in protobuf_obj]
        elif isinstance(protobuf_obj, dict):
            result = {}
            for key, value in protobuf_obj.items():
                result[str(key)] = self._convert_protobuf_to_dict(value)
            return result
        elif hasattr(protobuf_obj, 'ListFields'):
            # Handle message types
            result = {}
            for descriptor, value in protobuf_obj.ListFields():
                if descriptor.type == descriptor.TYPE_MESSAGE:
                    if descriptor.label == descriptor.LABEL_REPEATED:
                        result[descriptor.name] = [self._convert_protobuf_to_dict(v) for v in value]
                    else:
                        result[descriptor.name] = self._convert_protobuf_to_dict(value)
                elif descriptor.label == descriptor.LABEL_REPEATED:
                    result[descriptor.name] = list(value)
                else:
                    result[descriptor.name] = value
            return result
        else:
            # Primitive types
            return protobuf_obj
    
    def _convert_margin_response(self, response, group_id: int) -> Dict[str, Any]:
        """Convert MarginManagerResponse protobuf to dict format."""
        result = {
            "group_id": group_id,
            "accounts": [],
            "timestamp": datetime.utcnow().isoformat(),
            "total_margin": 0,
            "total_buying_power": 0,
            "total_excess_liquidity": 0,
            "total_net_liquidity": 0
        }
        
        # Process each account in the response
        for account_id, margin_info in response.MarginManagerInfo.items():
            account_data = {
                "account_id": f"ACCOUNT_{account_id}",  # Anonymized
                "account_number": margin_info.AccountNumber,
                "cash": margin_info.Cash,
                "is_pm_account": margin_info.IsPMAccount,
                "risk_type": self._get_risk_type_name(margin_info.AccountRiskType),
                "yesterday_liquidation_value": margin_info.YesterdayLiquidationValue,
                "alert_level": margin_info.AlertLevel if hasattr(margin_info, 'AlertLevel') else 0
            }
            
            # Extract PM account data if available
            if margin_info.HasField("PmBpValuesResponse") and margin_info.PmBpValuesResponse.HasField("PmBpValues"):
                pm_values = margin_info.PmBpValuesResponse.PmBpValues
                account_data.update({
                    "total_margin": pm_values.Requirement,
                    "net_liquidity": pm_values.NAV,
                    "excess_liquidity": pm_values.BuyingPower,
                    "buying_power": pm_values.BuyingPower,
                    "cash": pm_values.Cash,
                    "credit_limit": pm_values.CreditLimit,
                    "requirement": pm_values.Requirement,
                    "nav": pm_values.NAV
                })
                
                # Update totals
                result["total_margin"] += pm_values.Requirement
                result["total_buying_power"] += pm_values.BuyingPower
                result["total_excess_liquidity"] += pm_values.BuyingPower
                result["total_net_liquidity"] += pm_values.NAV
            
            result["accounts"].append(account_data)
        
        return result
    
    def _get_risk_type_name(self, risk_type: int) -> str:
        """Convert risk type enum to string."""
        risk_types = {
            0: "UNKNOWN",
            1: "CASH",
            2: "MARGIN",
            3: "PORTFOLIO_MARGIN"
        }
        return risk_types.get(risk_type, "UNKNOWN")
    
    async def get_historical_data(self, account_number: str, days: int = 7) -> List[Dict[str, Any]]:
        """Fetch historical data for an account using time machine service."""
        if not self.connected:
            raise RuntimeError("Not connected to Sarna API")
        
        try:
            # Create stub
            stub = api_hub_service_pb2_grpc.TimeMachineServiceStub(self.channel)
            
            # Calculate date range
            end_time = datetime.utcnow()
            start_time = end_time - timedelta(days=days)
            
            # Create request with proper format
            request = time_machine_pb2.TimeMachineBrowseRequest()
            request.AccountNumbers.append(account_number)
            # Use FromDatetime to properly set the timestamps
            request.From.FromDatetime(start_time)
            request.To.FromDatetime(end_time)
            request.IsCompressed = True
            
            logger.info(f"Request: AccountNumber={account_number}, From={start_time.isoformat()}, To={end_time.isoformat()}")
            
            # Make the call
            response = await stub.List(request, metadata=self._get_metadata())
            
            # Convert response to list of historical data points
            history = []
            for file_info in response.FileInfo:
                history.append({
                    "account_number": account_number,
                    "timestamp": file_info.MarginCalculatedTime.ToDatetime().isoformat(),
                    "net_liquidity": file_info.Netliq,
                    "margin_requirement": file_info.MarginReq,
                    "excess_liquidity": file_info.Excessliq,
                    "maintenance_requirement": file_info.MaintReq,
                    "total_pl": file_info.TotalPl,
                    "margin_type": file_info.MarginType,
                    "buying_power": file_info.Excessliq * 4 if file_info.MarginType == "PM" else file_info.Excessliq * 2,
                    "margin_utilization": (file_info.MarginReq / file_info.Netliq * 100) if file_info.Netliq > 0 else 0
                })
            
            # Sort by timestamp
            history.sort(key=lambda x: x["timestamp"])
            
            logger.info(f"Retrieved {len(history)} historical data points for {account_number}")
            return history
            
        except grpc.RpcError as e:
            logger.error(f"gRPC error fetching historical data: {e.code()} - {e.details()}")
            raise
        except Exception as e:
            logger.error(f"Error fetching historical data: {e}")
            raise
    
    async def get_historical_file(self, file_id: str) -> Dict[str, Any]:
        """Download a specific historical file."""
        if not self.connected:
            raise RuntimeError("Not connected to Sarna API")
        
        try:
            # Create stub
            stub = api_hub_service_pb2_grpc.TimeMachineServiceStub(self.channel)
            
            # Create request
            request = time_machine_pb2.TimeMachineDownloadRequest()
            request.FileId = file_id
            
            # Make the call
            response = await stub.Get(request, metadata=self._get_metadata())
            
            # Process the response
            return {
                "file_id": file_id,
                "content": response.Content,
                "timestamp": datetime.utcnow().isoformat()
            }
            
        except grpc.RpcError as e:
            logger.error(f"gRPC error downloading file: {e.code()} - {e.details()}")
            raise
        except Exception as e:
            logger.error(f"Error downloading file: {e}")
            raise
    
    async def get_alerts(self, page: int = 1, page_size: int = 50) -> Dict[str, Any]:
        """Get active alerts for the current user."""
        if not self.connected:
            raise RuntimeError("Not connected to Sarna API")
        
        try:
            # Create stub
            stub = alerts_service_pb2_grpc.AlertServiceStub(self.channel)
            
            # Create request
            request = alerts_pb2.AlertListRequest()
            request.Page.Page = page
            request.Page.PageSize = page_size
            
            # Make the call
            response = await stub.ListAlerts(request, metadata=self._get_metadata())
            
            # Process the response
            alerts = []
            for alert in response.Alerts:
                alerts.append({
                    "alert_id": alert.AlertId,
                    "account_id": alert.AccountId,
                    "account_number": alert.AccountNumber,
                    "alert_rule_id": alert.AlertRuleId,
                    "message": alert.Message,
                    "current_value": alert.CurrentValue,
                    "severity": self._get_alert_severity_name(alert.Severity),
                    "status": self._get_alert_status_name(alert.Status),
                    "created_time": alert.CreatedTime.ToDatetime().isoformat() if alert.HasField("CreatedTime") else None,
                    "last_notification_time": alert.LastNotificationTime.ToDatetime().isoformat() if alert.HasField("LastNotificationTime") else None,
                    "resolved_time": alert.ResolvedTime.ToDatetime().isoformat() if alert.HasField("ResolvedTime") else None,
                    "acknowledged_time": alert.AcknowledgedTime.ToDatetime().isoformat() if alert.HasField("AcknowledgedTime") else None,
                    "acknowledged_user_id": alert.AcknowledgedUserId if alert.AcknowledgedUserId else None
                })
            
            return {
                "alerts": alerts,
                "page": response.Page.Page if response.HasField("Page") else page,
                "page_size": response.Page.PageSize if response.HasField("Page") else page_size,
                "total_count": response.Page.TotalCount if response.HasField("Page") else len(alerts)
            }
            
        except grpc.RpcError as e:
            logger.error(f"gRPC error fetching alerts: {e.code()} - {e.details()}")
            raise
        except Exception as e:
            logger.error(f"Error fetching alerts: {e}")
            raise
    
    def _get_alert_severity_name(self, severity: int) -> str:
        """Convert alert severity enum to string."""
        severity_map = {
            alerts_enums_pb2.EnumAlertSeverity_Undefined: "undefined",
            alerts_enums_pb2.EnumAlertSeverity_Warning: "warning",
            alerts_enums_pb2.EnumAlertSeverity_Critical: "critical"
        }
        return severity_map.get(severity, "unknown")
    
    def _get_alert_status_name(self, status: int) -> str:
        """Convert alert status enum to string."""
        status_map = {
            alerts_enums_pb2.EnumAlertStatus_Undefined: "undefined",
            alerts_enums_pb2.EnumAlertStatus_Open: "open",
            alerts_enums_pb2.EnumAlertStatus_Acknowledged: "acknowledged",
            alerts_enums_pb2.EnumAlertStatus_Resolved: "resolved"
        }
        return status_map.get(status, "unknown")
