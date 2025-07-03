"""FastAPI application entry point."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.middleware import add_middleware
from core.config import settings
from core.logging import setup_logging
from routers import chat, data, health, visualizations
from db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown."""
    # Startup
    setup_logging()
    await init_db()
    yield
    # Shutdown
    # Add cleanup logic here if needed


app = FastAPI(
    title="Sarna Insights API",
    version="2.0.0",
    description="AI-powered analytics for portfolio risk management",
    lifespan=lifespan
)

# Add middleware
add_middleware(app)

# Include routers
app.include_router(health.router, prefix="/api/health", tags=["health"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(data.router, prefix="/api/data", tags=["data"])
app.include_router(visualizations.router, prefix="/api/viz", tags=["visualizations"])

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Sarna Insights API v2.0"}
