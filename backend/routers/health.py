"""Health check endpoints."""
from fastapi import APIRouter, status
from datetime import datetime

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    """Basic health check."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "sarna-insights-api"
    }


@router.get("/ready", status_code=status.HTTP_200_OK)
async def readiness_check():
    """Readiness check for dependencies."""
    # TODO: Check database, Redis, gRPC connections
    return {
        "status": "ready",
        "timestamp": datetime.utcnow().isoformat(),
        "dependencies": {
            "database": "ok",
            "redis": "ok",
            "grpc": "ok"
        }
    }
