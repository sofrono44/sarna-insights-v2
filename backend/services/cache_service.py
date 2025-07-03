"""Redis caching service."""
import redis.asyncio as redis
import json
import logging
from typing import Any, Optional
from datetime import timedelta

logger = logging.getLogger(__name__)


class CacheService:
    """Service for Redis caching."""
    
    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        self.client = None
    
    async def connect(self):
        """Connect to Redis."""
        self.client = await redis.from_url(self.redis_url)
        logger.info("Connected to Redis")
    
    async def close(self):
        """Close Redis connection."""
        if self.client:
            await self.client.close()
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        if not self.client:
            await self.connect()
        
        value = await self.client.get(key)
        if value:
            return json.loads(value)
        return None
    
    async def set(
        self, 
        key: str, 
        value: Any, 
        ttl: Optional[int] = None
    ):
        """Set value in cache with optional TTL in seconds."""
        if not self.client:
            await self.connect()
        
        serialized = json.dumps(value)
        if ttl:
            await self.client.setex(key, ttl, serialized)
        else:
            await self.client.set(key, serialized)
    
    async def delete(self, key: str):
        """Delete key from cache."""
        if not self.client:
            await self.connect()
        
        await self.client.delete(key)
    
    def cache_key(self, prefix: str, *args) -> str:
        """Generate cache key."""
        parts = [prefix] + [str(arg) for arg in args]
        return ":".join(parts)
