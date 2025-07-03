#!/usr/bin/env python
"""Test cache integration with gRPC client."""
import asyncio
import logging
import json
import time
from services.cache_service import CacheService
from services.grpc_client import SarnaGRPCClient
from core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_cache_integration():
    """Test cache integration with real gRPC data."""
    cache = CacheService(settings.REDIS_URL)
    grpc_client = SarnaGRPCClient(
        url=settings.SARNA_API_URL,
        jwt_token=settings.SARNA_JWT_TOKEN,
        use_tls=settings.RISK_SYSTEM_USE_TLS
    )
    
    try:
        # Connect to both services
        await cache.connect()
        await grpc_client.connect()
        logger.info("✅ Connected to Redis and gRPC")
        
        # Test 1: Current portfolio data with caching
        logger.info("\n📊 Test 1: Current portfolio data caching")
        group_id = 10006
        portfolio_key = cache.cache_key("portfolio", group_id)
        
        # First call - should hit gRPC
        start_time = time.time()
        portfolio_data = await grpc_client.get_current_margin_data(group_id)
        grpc_time = time.time() - start_time
        logger.info(f"gRPC call took: {grpc_time:.3f}s")
        
        # Cache the data with 30s TTL
        cache_data = {
            "group_id": group_id,
            "accounts": portfolio_data.get("accounts", []),
            "timestamp": portfolio_data.get("timestamp"),
            "total_margin": sum(acc.get("margin", 0) for acc in portfolio_data.get("accounts", [])),
            "total_buying_power": sum(acc.get("buying_power", 0) for acc in portfolio_data.get("accounts", []))
        }
        await cache.set(portfolio_key, cache_data, ttl=30)
        logger.info(f"Cached portfolio data for group {group_id}")
        
        # Second call - should hit cache
        start_time = time.time()
        cached_portfolio = await cache.get(portfolio_key)
        cache_time = time.time() - start_time
        logger.info(f"Cache retrieval took: {cache_time:.3f}s")
        logger.info(f"Speed improvement: {grpc_time/cache_time:.1f}x faster")
        
        # Verify data
        assert cached_portfolio["group_id"] == group_id
        assert len(cached_portfolio["accounts"]) == 9  # We know group 10006 has 9 accounts
        logger.info(f"✅ Portfolio caching working! Total margin: ${cached_portfolio['total_margin']:,.2f}")
        
        # Test 2: Historical data caching
        logger.info("\n📈 Test 2: Historical data caching")
        days = 7
        history_key = cache.cache_key("history", group_id, days)
        
        # Check if already cached
        cached_history = await cache.get(history_key)
        if cached_history:
            logger.info("Historical data already cached from previous run")
        else:
            # Fetch from gRPC
            start_time = time.time()
            snapshots = await grpc_client.get_historical_data(group_id, days)
            grpc_time = time.time() - start_time
            logger.info(f"gRPC historical call took: {grpc_time:.3f}s for {len(snapshots)} snapshots")
            
            # Cache forever (historical data is immutable)
            history_data = {
                "group_id": group_id,
                "days": days,
                "snapshots": snapshots[:100],  # Just cache first 100 for demo
                "data_points": len(snapshots)
            }
            await cache.set(history_key, history_data)
            logger.info(f"✅ Cached {len(snapshots)} historical snapshots")
        
        # Test 3: Simulate API endpoint behavior
        logger.info("\n🔄 Test 3: Simulate API endpoint with cache check")
        
        async def get_portfolio_with_cache(group_id: int):
            """Simulate how the API endpoint would use cache."""
            key = cache.cache_key("portfolio", group_id)
            
            # Check cache first
            cached = await cache.get(key)
            if cached:
                logger.info("Cache HIT ✅")
                return cached
            
            logger.info("Cache MISS ❌ - fetching from gRPC")
            # Fetch from gRPC
            data = await grpc_client.get_current_margin_data(group_id)
            
            # Transform and cache
            result = {
                "group_id": group_id,
                "accounts": data.get("accounts", []),
                "timestamp": data.get("timestamp"),
                "total_margin": sum(acc.get("margin", 0) for acc in data.get("accounts", [])),
                "total_buying_power": sum(acc.get("buying_power", 0) for acc in data.get("accounts", []))
            }
            await cache.set(key, result, ttl=30)
            return result
        
        # First call - should miss cache (if TTL expired)
        await cache.delete(portfolio_key)  # Force cache miss
        result1 = await get_portfolio_with_cache(group_id)
        
        # Second call - should hit cache
        result2 = await get_portfolio_with_cache(group_id)
        
        assert result1["total_margin"] == result2["total_margin"]
        logger.info("✅ Cache integration pattern working correctly!")
        
        # Test 4: Refresh functionality
        logger.info("\n🔄 Test 4: Manual refresh (cache invalidation)")
        
        # Clear cache
        await cache.delete(portfolio_key)
        logger.info("Cleared portfolio cache")
        
        # Next call will fetch fresh data
        fresh_data = await get_portfolio_with_cache(group_id)
        logger.info("✅ Fresh data fetched after cache clear")
        
        logger.info("\n✅ All cache integration tests passed!")
        
    except Exception as e:
        logger.error(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await cache.close()
        await grpc_client.close()
        logger.info("Closed all connections")


if __name__ == "__main__":
    asyncio.run(test_cache_integration())
