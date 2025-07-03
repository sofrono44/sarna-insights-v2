"""Shared dependencies for API endpoints."""
from typing import Annotated
from fastapi import Depends, HTTPException, status
from services.grpc_client import SarnaGRPCClient
from services.llm_service import LLMService
from services.cache_service import CacheService
from core.config import settings


async def get_grpc_client() -> SarnaGRPCClient:
    """Get gRPC client instance."""
    client = SarnaGRPCClient(
        url=settings.SARNA_API_URL,
        jwt_token=settings.SARNA_JWT_TOKEN
    )
    try:
        await client.connect()
        yield client
    finally:
        await client.close()


async def get_llm_service() -> LLMService:
    """Get LLM service instance."""
    return LLMService()


async def get_cache_service() -> CacheService:
    """Get cache service instance."""
    return CacheService(settings.REDIS_URL)


# Type aliases for dependency injection
GRPCClientDep = Annotated[SarnaGRPCClient, Depends(get_grpc_client)]
LLMServiceDep = Annotated[LLMService, Depends(get_llm_service)]
CacheServiceDep = Annotated[CacheService, Depends(get_cache_service)]
