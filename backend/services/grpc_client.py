"""gRPC client for Sarna API."""
import grpc
import logging
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta
import asyncio
import json
from google.protobuf.timestamp_pb2 import Timestamp

# Import generated protobuf files
from generated.admin import admin_margin_manager_pb2
from generated.admin import admin_margin_manager_service_pb2_grpc
from generated import time_machine_pb2
from generated.api_hub import api_hub_service_pb2_grpc

logger = logging.getLogger(__name__)


class SarnaGRPCClient:
    """Client for Sarna gRPC API."""
    
    def __init__(self, url: str, jwt_token: str, use_tls: bool = True):
        self.url = url
        self.jwt_token = jwt_token
        self.use_tls = use_tls
        self.channel = None
        self.connected = False
    
    async def connect(self):
        """Establish gRPC connection."""
        try:
            # Create channel based on TLS setting
            if self.use_tls:
                self.channel = grpc.aio.secure_channel(
                    self.url,
                    grpc.ssl_channel_credentials()
                )
                logger.info(f"Connected to Sarna API at {self.url} (TLS enabled)")
            else:
                self.channel = grpc.aio.insecure_channel(self.url)
                logger.info(f"Connected to Sarna API at {self.url} (TLS disabled)")
            
            self.connected = True
        except Exception as e:
            logger.error(f"Failed to connect to Sarna API: {e}")
            raise
    
    async def close(self):
        """Close gRPC connection."""
        if self.channel:
            await self.channel.close()
            self.connected = False
    
    def _get_metadata(self):
        """Get auth metadata for requests."""
        return [('authorization', f'Bearer {self.jwt_token}')]
    
    async def get_current_margin_data(self, group_id: int) -> Dict[str, Any]:
        """Fetch current margin data from AdminMarginManagerService/Get."""
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
            portfolio_request.FetchAllAccounts = True
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
                    "margin": pm_values.Requirement if hasattr(pm_values, 'Requirement') else 0,
                    "buying_power": pm_values.BuyingPower,
                    "excess_liquidity": pm_values.ExcessLiquidity,
                    "net_liquidity": pm_values.NetLiquidity,
                    "nav": pm_values.NAV if hasattr(pm_values, 'NAV') else 0,
                    "credit_utilization": pm_values.CreditUtilization if hasattr(pm_values, 'CreditUtilization') else 0,
                    "morning_nav": pm_values.MorningNAV if hasattr(pm_values, 'MorningNAV') else 0
                })
                
                # Extract position aggregations if available
                if hasattr(pm_values, 'PositionAggregations'):
                    pos_agg = pm_values.PositionAggregations
                    account_data["position_aggregations"] = {
                        "long_market_value": pos_agg.LongMarketValue if hasattr(pos_agg, 'LongMarketValue') else 0,
                        "delta_long_exposure": pos_agg.DeltaLongExposure if hasattr(pos_agg, 'DeltaLongExposure') else 0,
                        "delta_long_count": pos_agg.DeltaLongCount if hasattr(pos_agg, 'DeltaLongCount') else 0
                    }
                
                # Aggregate totals
                result["total_margin"] += account_data.get("margin", 0)
                result["total_buying_power"] += account_data.get("buying_power", 0)
                result["total_excess_liquidity"] += account_data.get("excess_liquidity", 0)
                result["total_net_liquidity"] += account_data.get("net_liquidity", 0)
            
            # Extract regular account data if available
            elif margin_info.HasField("BpValuesResponse") and margin_info.BpValuesResponse.HasField("BpValues"):
                bp_values = margin_info.BpValuesResponse.BpValues
                account_data.update({
                    "buying_power": bp_values.BuyingPower if hasattr(bp_values, 'BuyingPower') else 0,
                    "excess_liquidity": bp_values.ExcessLiquidity if hasattr(bp_values, 'ExcessLiquidity') else 0,
                    "cash": bp_values.Cash if hasattr(bp_values, 'Cash') else margin_info.Cash
                })
                
                result["total_buying_power"] += account_data.get("buying_power", 0)
                result["total_excess_liquidity"] += account_data.get("excess_liquidity", 0)
            
            result["accounts"].append(account_data)
        
        # Calculate margin utilization
        if result["total_net_liquidity"] > 0:
            result["total_margin_utilization"] = result["total_margin"] / result["total_net_liquidity"]
        else:
            result["total_margin_utilization"] = 0
        
        return result
    
    def _get_risk_type_name(self, risk_type_enum) -> str:
        """Convert risk type enum to string."""
        # This mapping should match the enum values in the proto
        risk_type_map = {
            0: "Unknown",
            1: "RegTMargin",
            2: "PMCPM",
            3: "Cash"
        }
        return risk_type_map.get(risk_type_enum, f"Type_{risk_type_enum}")
    
    async def get_historical_data(self, group_id: int, days: int = 30) -> List[Dict[str, Any]]:
        """Fetch historical snapshots from TimeMachineService/List."""
        if not self.connected:
            raise RuntimeError("Not connected to Sarna API")
        
        try:
            # First, get accounts for the group to pick one account number
            margin_data = await self.get_current_margin_data(group_id)
            if not margin_data or not margin_data.get("accounts"):
                logger.warning(f"No accounts found for group {group_id}")
                return []
            
            # Use the first account's number for the query
            first_account = margin_data["accounts"][0]
            account_number = first_account.get("account_number")
            if not account_number:
                logger.error("No account number found in margin data")
                return []
            
            logger.info(f"Using account {account_number} to fetch historical data for group {group_id}")
            
            # Create stub for TimeMachineService
            stub = api_hub_service_pb2_grpc.TimeMachineServiceStub(self.channel)
            
            # Calculate time range
            end_time = datetime.utcnow()
            start_time = end_time - timedelta(days=days)
            
            # Create request with proper format
            request = time_machine_pb2.TimeMachineBrowseRequest()
            request.AccountNumber = account_number
            # Use FromDatetime to properly set the timestamps
            request.From.FromDatetime(start_time)
            request.To.FromDatetime(end_time)
            request.RequestOrigin = 0  # Undefined = 0
            
            logger.info(f"Request: AccountNumber={account_number}, From={start_time.isoformat()}, To={end_time.isoformat()}")
            
            # Make the call
            response = await stub.List(request, metadata=self._get_metadata())
            
            logger.info(f"Received {len(response.Files)} historical files")
            
            # Process the file list from the response
            snapshots = []
            for file_info in response.Files:
                # Convert protobuf timestamp to datetime
                created_time = datetime.fromtimestamp(
                    file_info.CreatedTime.seconds + file_info.CreatedTime.nanos / 1e9
                )
                
                snapshot = {
                    "timestamp": created_time.isoformat(),
                    "file_name": file_info.FileName,
                    "type": str(file_info.Type) if hasattr(file_info, 'Type') else "",
                    "requirement": float(file_info.Requirement) if hasattr(file_info, 'Requirement') else 0,
                    "net_liquidity": float(file_info.NetLiquidity) if hasattr(file_info, 'NetLiquidity') else 0,
                    "day_pnl": float(file_info.DayPnL) if hasattr(file_info, 'DayPnL') else 0,
                    "day_pnl_utilization": float(file_info.DayPnLUtilization) if hasattr(file_info, 'DayPnLUtilization') else 0,
                    "credit_utilization": float(file_info.CreditUtilization) if hasattr(file_info, 'CreditUtilization') else 0,
                    "excess_liquidity": float(file_info.ExcessLiquidity) if hasattr(file_info, 'ExcessLiquidity') else 0,
                    "account_group_ids": list(file_info.AccountGroupIds) if file_info.AccountGroupIds else [],
                    "data": {
                        "requirement": float(file_info.Requirement) if hasattr(file_info, 'Requirement') else 0,
                        "net_liquidity": float(file_info.NetLiquidity) if hasattr(file_info, 'NetLiquidity') else 0,
                        "credit_utilization": float(file_info.CreditUtilization) if hasattr(file_info, 'CreditUtilization') else 0,
                        "excess_liquidity": float(file_info.ExcessLiquidity) if hasattr(file_info, 'ExcessLiquidity') else 0,
                        "day_pnl": float(file_info.DayPnL) if hasattr(file_info, 'DayPnL') else 0
                    }
                }
                
                # Include snapshots that have our group ID, group ID 0, or no group IDs
                group_ids = snapshot["account_group_ids"]
                if not group_ids or group_id in group_ids or 0 in group_ids:
                    snapshots.append(snapshot)
            
            # Sort by timestamp
            snapshots.sort(key=lambda x: x["timestamp"])
            
            return snapshots
            
        except grpc.RpcError as e:
            logger.error(f"gRPC error fetching historical data: {e.code()} - {e.details()}")
            raise
        except Exception as e:
            logger.error(f"Error fetching historical data: {e}")
            raise
    
    async def get_time_machine_snapshot(self, file_name: str) -> Dict[str, Any]:
        """Download a specific time machine snapshot."""
        if not self.connected:
            raise RuntimeError("Not connected to Sarna API")
        
        try:
            # Create stub
            stub = api_hub_service_pb2_grpc.TimeMachineServiceStub(self.channel)
            
            # Create request
            request = time_machine_pb2.TimeMachineDownloadRequest()
            request.FileName = file_name
            
            # Make the call
            response = await stub.Get(request, metadata=self._get_metadata())
            
            # Process the response
            snapshot_data = {
                "file_name": response.FileName,
                "request": response.Request,
                "response": response.Response
            }
            
            # Extract PM BP values if available
            if response.HasField("PmBpValuesResponse"):
                snapshot_data["pm_bp_values"] = self._extract_pm_bp_values(response.PmBpValuesResponse)
            
            # Extract regular BP values if available
            if response.HasField("BpValuesResponse"):
                snapshot_data["bp_values"] = self._extract_bp_values(response.BpValuesResponse)
            
            # Extract portfolio report if available
            if response.PortfolioReport:
                snapshot_data["portfolio_report"] = response.PortfolioReport
            
            return snapshot_data
            
        except grpc.RpcError as e:
            logger.error(f"gRPC error downloading snapshot: {e.code()} - {e.details()}")
            raise
        except Exception as e:
            logger.error(f"Error downloading snapshot: {e}")
            raise
    
    def _extract_pm_bp_values(self, pm_response) -> Dict[str, Any]:
        """Extract PM BP values from response."""
        # Similar extraction logic as in _convert_margin_response
        return {
            "account_id": pm_response.AccountId,
            "account_number": pm_response.AccountNumber,
            "account_name": pm_response.AccountName
            # Add more fields as needed
        }
    
    def _extract_bp_values(self, bp_response) -> Dict[str, Any]:
        """Extract regular BP values from response."""
        return {
            # Extract relevant fields
        }


# Singleton instance management
_client_instance = None
_client_lock = asyncio.Lock()


async def get_grpc_client() -> SarnaGRPCClient:
    """Get or create singleton gRPC client instance."""
    global _client_instance
    
    async with _client_lock:
        if _client_instance is None:
            from core.config import settings
            _client_instance = SarnaGRPCClient(
                url=settings.SARNA_API_URL,
                jwt_token=settings.SARNA_JWT_TOKEN,
                use_tls=settings.RISK_SYSTEM_USE_TLS
            )
            await _client_instance.connect()
    
    return _client_instance


async def close_grpc_client():
    """Close the gRPC client connection."""
    global _client_instance
    
    async with _client_lock:
        if _client_instance:
            await _client_instance.close()
            _client_instance = None
