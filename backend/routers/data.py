"""Data fetching endpoints."""
from fastapi import APIRouter, HTTPException
from typing import Optional
from datetime import datetime
from api.dependencies import GRPCClientDep, CacheServiceDep
from models.responses import PortfolioData, HistoricalData
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


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
            return PortfolioData(**cached_data)
        
        # Fetch from gRPC
        data = await grpc_client.get_current_margin_data(group_id)
        
        # Transform and cache
        result = PortfolioData(
            group_id=group_id,
            accounts=data.get("accounts", []),
            timestamp=datetime.utcnow(),
            total_margin=sum(acc.get("margin", 0) for acc in data.get("accounts", []))
        )
        
        await cache.set(cache_key, result.dict(), ttl=30)
        return result
        
    except Exception as e:
        logger.error(f"Failed to fetch portfolio data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{group_id}", response_model=HistoricalData)
async def get_historical_data(
    group_id: int,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep,
    days: int = 30
):
    """Get historical data for account group."""
    try:
        # Check cache (historical data is immutable, cache forever)
        cache_key = cache.cache_key("history", group_id, days)
        cached_data = await cache.get(cache_key)
        if cached_data:
            return HistoricalData(**cached_data)
        
        # Fetch from gRPC
        snapshots = await grpc_client.get_historical_data(group_id, days)
        
        # Transform and cache
        result = HistoricalData(
            group_id=group_id,
            days=days,
            snapshots=snapshots,
            data_points=len(snapshots)
        )
        
        # Cache forever since historical data doesn't change
        await cache.set(cache_key, result.dict())
        return result
        
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
        
        # Don't clear historical cache as it's immutable
        
        return {"status": "success", "message": "Cache cleared"}
        
    except Exception as e:
        logger.error(f"Failed to refresh data: {e}")
        raise HTTPException(status_code=500, detail=str(e))
