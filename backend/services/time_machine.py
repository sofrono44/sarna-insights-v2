"""Time Machine service wrapper for historical data access."""
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from services.grpc_client import SarnaGRPCClient
from services.cache_service import CacheService

logger = logging.getLogger(__name__)


class TimeMachineService:
    """Service for accessing historical portfolio data."""
    
    def __init__(self, grpc_client: SarnaGRPCClient, cache_service: CacheService):
        self.grpc_client = grpc_client
        self.cache = cache_service
    
    async def get_portfolio_trends(
        self, 
        group_id: int, 
        days: int = 30,
        metric: str = "net_liquidity"
    ) -> Dict[str, Any]:
        """Get trend data for a specific metric over time."""
        # Get historical snapshots
        snapshots = await self.get_historical_snapshots(group_id, days)
        
        # Extract metric values over time
        trend_data = []
        for snapshot in snapshots:
            data = snapshot.get("data", {})
            value = data.get(metric, 0)
            if value > 0:  # Filter out empty data points
                trend_data.append({
                    "timestamp": snapshot["timestamp"],
                    "value": value
                })
        
        # Calculate statistics
        if trend_data:
            values = [point["value"] for point in trend_data]
            avg_value = sum(values) / len(values)
            min_value = min(values)
            max_value = max(values)
            
            # Calculate trend (simple linear regression)
            if len(values) > 1:
                # Simple trend: compare first half average to second half average
                mid_point = len(values) // 2
                first_half_avg = sum(values[:mid_point]) / mid_point
                second_half_avg = sum(values[mid_point:]) / len(values[mid_point:])
                trend_direction = "up" if second_half_avg > first_half_avg else "down"
                trend_percent = ((second_half_avg - first_half_avg) / first_half_avg) * 100
            else:
                trend_direction = "stable"
                trend_percent = 0
        else:
            avg_value = min_value = max_value = 0
            trend_direction = "no_data"
            trend_percent = 0
        
        return {
            "metric": metric,
            "days": days,
            "data_points": len(trend_data),
            "trend_data": trend_data[-100:],  # Limit to last 100 points for UI
            "statistics": {
                "average": avg_value,
                "minimum": min_value,
                "maximum": max_value,
                "trend_direction": trend_direction,
                "trend_percent": trend_percent
            }
        }
    
    async def get_historical_snapshots(
        self, 
        group_id: int, 
        days: int
    ) -> List[Dict[str, Any]]:
        """Get historical snapshots with caching."""
        # Check cache first
        cache_key = self.cache.cache_key("history", group_id, days)
        cached_data = await self.cache.get(cache_key)
        
        if cached_data:
            logger.info(f"Using cached historical data for group {group_id}")
            return cached_data.get("snapshots", [])
        
        # Fetch from gRPC
        logger.info(f"Fetching historical data from gRPC for group {group_id}")
        snapshots = await self.grpc_client.get_historical_data(group_id, days)
        
        # Cache the result
        cache_data = {
            "group_id": group_id,
            "days": days,
            "snapshots": snapshots,
            "data_points": len(snapshots)
        }
        await self.cache.set(cache_key, cache_data)
        
        return snapshots
    
    async def get_daily_summaries(
        self, 
        group_id: int, 
        days: int = 7
    ) -> List[Dict[str, Any]]:
        """Get daily summary statistics."""
        snapshots = await self.get_historical_snapshots(group_id, days)
        
        # Group by day
        daily_data = {}
        for snapshot in snapshots:
            # Parse timestamp and get date
            timestamp = datetime.fromisoformat(snapshot["timestamp"].replace("Z", "+00:00"))
            date_key = timestamp.date().isoformat()
            
            if date_key not in daily_data:
                daily_data[date_key] = {
                    "date": date_key,
                    "snapshots": [],
                    "net_liquidity_values": [],
                    "requirement_values": [],
                    "pnl_values": []
                }
            
            data = snapshot.get("data", {})
            daily_data[date_key]["snapshots"].append(snapshot)
            
            if data.get("net_liquidity"):
                daily_data[date_key]["net_liquidity_values"].append(data["net_liquidity"])
            if data.get("requirement"):
                daily_data[date_key]["requirement_values"].append(data["requirement"])
            if data.get("day_pnl"):
                daily_data[date_key]["pnl_values"].append(data["day_pnl"])
        
        # Calculate daily summaries
        summaries = []
        for date, day_data in sorted(daily_data.items()):
            summary = {
                "date": date,
                "snapshot_count": len(day_data["snapshots"]),
                "avg_net_liquidity": sum(day_data["net_liquidity_values"]) / len(day_data["net_liquidity_values"]) if day_data["net_liquidity_values"] else 0,
                "avg_requirement": sum(day_data["requirement_values"]) / len(day_data["requirement_values"]) if day_data["requirement_values"] else 0,
                "total_pnl": sum(day_data["pnl_values"]) if day_data["pnl_values"] else 0,
                "max_pnl": max(day_data["pnl_values"]) if day_data["pnl_values"] else 0,
                "min_pnl": min(day_data["pnl_values"]) if day_data["pnl_values"] else 0
            }
            summaries.append(summary)
        
        return summaries
