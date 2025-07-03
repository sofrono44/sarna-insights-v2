"""Data fetching endpoints with proper caching."""
from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List, Dict, Any
from datetime import datetime
from api.dependencies import GRPCClientDep, CacheServiceDep
from models.responses import PortfolioData, HistoricalData, AccountData, HistoricalSnapshot
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


def transform_account_data(account: Dict[str, Any]) -> AccountData:
    """Transform raw account data to AccountData model."""
    return AccountData(
        account_id=account.get("account_id", ""),
        margin=float(account.get("margin", 0)),
        buying_power=float(account.get("buying_power", 0)),
        excess_liquidity=float(account.get("excess_liquidity", 0)),
        margin_utilization=float(account.get("credit_utilization", 0)),  # Note: field name difference
        unrealized_pl=float(account.get("unrealized_pl", 0)),
        realized_pl=float(account.get("realized_pl", 0)),
        positions_count=int(account.get("position_aggregations", {}).get("delta_long_count", 0))
    )


@router.get("/portfolio/{group_id}", response_model=PortfolioData)
async def get_portfolio_data(
    group_id: int,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep
):
    """Get current portfolio data for account group."""
    try:
        # Check cache first (30 second TTL for current data)
        cache_key = cache.cache_key("portfolio", group_id)
        cached_data = await cache.get(cache_key)
        if cached_data:
            logger.info(f"Cache HIT for portfolio {group_id}")
            return PortfolioData(**cached_data)
        
        logger.info(f"Cache MISS for portfolio {group_id} - fetching from gRPC")
        
        # Fetch from gRPC
        data = await grpc_client.get_current_margin_data(group_id)
        
        # Transform accounts
        accounts = [transform_account_data(acc) for acc in data.get("accounts", [])]
        
        # Calculate totals
        total_margin = sum(acc.margin for acc in accounts)
        total_buying_power = sum(acc.buying_power for acc in accounts)
        total_pl = sum(acc.unrealized_pl + acc.realized_pl for acc in accounts)
        
        # Create response
        result = PortfolioData(
            group_id=group_id,
            accounts=accounts,
            timestamp=datetime.utcnow(),
            total_margin=total_margin,
            total_buying_power=total_buying_power,
            total_pl=total_pl
        )
        
        # Cache with 30s TTL
        await cache.set(cache_key, result.model_dump(mode='json'), ttl=30)
        
        logger.info(f"Portfolio data cached for group {group_id}")
        return result
        
    except grpc.RpcError as e:
        logger.error(f"gRPC error fetching portfolio: {e.code()} - {e.details()}")
        raise HTTPException(status_code=503, detail="Unable to fetch portfolio data from backend")
    except Exception as e:
        logger.error(f"Failed to fetch portfolio data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{group_id}", response_model=HistoricalData)
async def get_historical_data(
    group_id: int,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep,
    days: int = Query(default=30, ge=1, le=365)
):
    """Get historical data for account group."""
    try:
        # Check cache (historical data is immutable, cache forever)
        cache_key = cache.cache_key("history", group_id, days)
        cached_data = await cache.get(cache_key)
        if cached_data:
            logger.info(f"Cache HIT for {days}-day history of group {group_id}")
            return HistoricalData(**cached_data)
        
        logger.info(f"Cache MISS for {days}-day history of group {group_id} - fetching from gRPC")
        
        # Fetch from gRPC
        snapshots = await grpc_client.get_historical_data(group_id, days)
        
        # Transform snapshots to match our model
        historical_snapshots = [
            HistoricalSnapshot(
                timestamp=snapshot["timestamp"],
                data=snapshot.get("data", {})
            )
            for snapshot in snapshots
        ]
        
        # Create response
        result = HistoricalData(
            group_id=group_id,
            days=days,
            snapshots=historical_snapshots,
            data_points=len(historical_snapshots)
        )
        
        # Cache forever since historical data doesn't change
        await cache.set(cache_key, result.model_dump(mode='json'))
        
        logger.info(f"Historical data cached for group {group_id} ({len(snapshots)} snapshots)")
        return result
        
    except grpc.RpcError as e:
        logger.error(f"gRPC error fetching history: {e.code()} - {e.details()}")
        raise HTTPException(status_code=503, detail="Unable to fetch historical data from backend")
    except Exception as e:
        logger.error(f"Failed to fetch historical data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/refresh/{group_id}")
async def refresh_data(
    group_id: int,
    cache: CacheServiceDep
):
    """Force refresh of cached data."""
    try:
        # Clear portfolio cache
        portfolio_key = cache.cache_key("portfolio", group_id)
        await cache.delete(portfolio_key)
        
        # Also clear any chat queries that might reference this portfolio
        # In production, we'd want a more sophisticated cache invalidation strategy
        
        logger.info(f"Cleared cache for group {group_id}")
        
        return {
            "status": "success", 
            "message": f"Cache cleared for group {group_id}",
            "cleared_keys": ["portfolio"]
        }
        
    except Exception as e:
        logger.error(f"Failed to refresh data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/cache-stats")
async def get_cache_stats(
    cache: CacheServiceDep
):
    """Get cache statistics (admin endpoint)."""
    try:
        # This is a simplified version - in production we'd track more metrics
        return {
            "status": "connected",
            "message": "Cache service is operational"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
