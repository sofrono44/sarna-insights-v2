"""Request models."""
from pydantic import BaseModel, Field
from typing import Optional, Literal


class ChatQuery(BaseModel):
    """Chat query request."""
    question: str = Field(..., description="Natural language question about portfolio")
    provider: Literal["openai", "anthropic", "google"] = Field(
        default="openai",
        description="LLM provider to use"
    )
    include_historical: bool = Field(
        default=False,
        description="Whether to include historical data in context"
    )


class RefreshRequest(BaseModel):
    """Data refresh request."""
    clear_cache: bool = Field(default=True, description="Clear cached data")
