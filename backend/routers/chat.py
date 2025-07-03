"""Chat/NLP endpoints with caching."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from api.dependencies import LLMServiceDep, GRPCClientDep, CacheServiceDep
from services.data_anonymizer import DataAnonymizer
from models.requests import ChatQuery
from models.responses import ChatResponse
import logging
import hashlib
import json

logger = logging.getLogger(__name__)
router = APIRouter()

# System prompt for portfolio queries
SYSTEM_PROMPT = """You are a financial analyst assistant helping users understand their portfolio data.
You have access to anonymized portfolio information including margin requirements, positions, and balances.
Always provide clear, actionable insights based on the data provided.
Never mention account numbers or personal information in your responses.
When discussing specific accounts, refer to them by their anonymized IDs (e.g., ACCOUNT_XXXXX)."""


def generate_query_hash(question: str, provider: str, include_historical: bool) -> str:
    """Generate a stable hash for the query to use as cache key."""
    content = f"{question}:{provider}:{include_historical}"
    return hashlib.md5(content.encode()).hexdigest()[:12]


@router.post("/query", response_model=ChatResponse)
async def query_portfolio(
    query: ChatQuery,
    llm_service: LLMServiceDep,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep
):
    """Process natural language query about portfolio."""
    try:
        # Generate cache key based on query content
        query_hash = generate_query_hash(query.question, query.provider, query.include_historical)
        cache_key = cache.cache_key("chat", query_hash)
        
        # Check cache first (5 minute TTL for chat responses)
        cached_response = await cache.get(cache_key)
        if cached_response:
            logger.info(f"Cache HIT for chat query: {query.question[:50]}...")
            return ChatResponse(**cached_response)
        
        logger.info(f"Cache MISS for chat query: {query.question[:50]}...")
        
        # Initialize anonymizer (though data comes pre-anonymized)
        anonymizer = DataAnonymizer()
        
        # Fetch current portfolio data (this might also hit cache)
        portfolio_data = await grpc_client.get_current_margin_data(10006)
        
        # Optionally include historical data
        historical_context = ""
        if query.include_historical:
            try:
                historical_data = await grpc_client.get_historical_data(10006, days=7)
                if historical_data:
                    # Summarize historical trends
                    historical_context = f"\n\nHistorical data (last 7 days): {len(historical_data)} data points available."
                    # Could add more sophisticated trend analysis here
            except Exception as e:
                logger.warning(f"Failed to fetch historical data: {e}")
        
        # Create context for LLM (data is already anonymized from API)
        portfolio_context = {
            "total_accounts": len(portfolio_data.get("accounts", [])),
            "total_margin": sum(acc.get("margin", 0) for acc in portfolio_data.get("accounts", [])),
            "total_buying_power": sum(acc.get("buying_power", 0) for acc in portfolio_data.get("accounts", [])),
            "total_excess_liquidity": sum(acc.get("excess_liquidity", 0) for acc in portfolio_data.get("accounts", [])),
            "accounts": [
                {
                    "id": acc.get("account_id"),
                    "margin": acc.get("margin"),
                    "buying_power": acc.get("buying_power"),
                    "excess_liquidity": acc.get("excess_liquidity"),
                    "credit_utilization": acc.get("credit_utilization"),
                    "risk_type": acc.get("risk_type")
                }
                for acc in portfolio_data.get("accounts", [])
            ]
        }
        
        # Construct prompt
        prompt = f"""Portfolio Data:
{json.dumps(portfolio_context, indent=2)}
{historical_context}

User Question: {query.question}

Please provide a clear, helpful response based on the portfolio data above. Be specific and actionable."""
        
        # Query LLM
        response = await llm_service.query(
            prompt=prompt,
            provider=query.provider,
            system_prompt=SYSTEM_PROMPT
        )
        
        # Create response
        result = ChatResponse(
            question=query.question,
            answer=response,
            provider=query.provider
        )
        
        # Cache response (5 minute TTL)
        await cache.set(cache_key, result.model_dump(mode='json'), ttl=300)
        
        logger.info(f"Chat response cached with key: {cache_key}")
        return result
        
    except Exception as e:
        logger.error(f"Chat query failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/examples")
async def get_example_queries():
    """Get example queries for the UI."""
    return {
        "examples": [
            "What is my total portfolio value?",
            "Show me accounts with margin over $100,000",
            "What are my current margin requirements?",
            "Show me P&L trends for the last week",
            "Which accounts have the highest margin utilization?"
        ]
    }
