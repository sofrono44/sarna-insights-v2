"""Chat/NLP endpoints."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from api.dependencies import LLMServiceDep, GRPCClientDep, CacheServiceDep
from services.data_anonymizer import DataAnonymizer
from models.requests import ChatQuery
from models.responses import ChatResponse
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

# System prompt for portfolio queries
SYSTEM_PROMPT = """You are a financial analyst assistant helping users understand their portfolio data.
You have access to anonymized portfolio information including margin requirements, positions, and balances.
Always provide clear, actionable insights based on the data provided.
Never mention account numbers or personal information in your responses."""


@router.post("/query", response_model=ChatResponse)
async def query_portfolio(
    query: ChatQuery,
    llm_service: LLMServiceDep,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep
):
    """Process natural language query about portfolio."""
    try:
        # Initialize anonymizer
        anonymizer = DataAnonymizer()
        
        # Check cache first
        cache_key = cache.cache_key("chat", query.question, query.provider)
        cached_response = await cache.get(cache_key)
        if cached_response:
            return ChatResponse(**cached_response)
        
        # Fetch current portfolio data
        portfolio_data = await grpc_client.get_current_margin_data(10006)
        
        # Anonymize data
        anon_context = anonymizer.get_context_for_llm(portfolio_data)
        
        # Construct prompt
        prompt = f"""Portfolio Data:
{anon_context}

User Question: {query.question}

Please provide a clear, helpful response based on the portfolio data above."""
        
        # Query LLM
        response = await llm_service.query(
            prompt=prompt,
            provider=query.provider,
            system_prompt=SYSTEM_PROMPT
        )
        
        # Restore identifiers in response
        final_response = anonymizer.restore_identifiers(response)
        
        # Cache response (5 minute TTL)
        result = {
            "question": query.question,
            "answer": final_response,
            "provider": query.provider
        }
        await cache.set(cache_key, result, ttl=300)
        
        return ChatResponse(**result)
        
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
