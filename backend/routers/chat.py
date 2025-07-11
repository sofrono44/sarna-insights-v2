"""Chat/NLP endpoints with caching and visualization support."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Literal
from api.dependencies import LLMServiceDep, GRPCClientDep, CacheServiceDep
from services.data_anonymizer import DataAnonymizer
from models.requests import ChatQuery
from models.responses import ChatResponse
import logging
import hashlib
import json
import re

logger = logging.getLogger(__name__)
router = APIRouter()

# Enhanced system prompt for portfolio queries with visualization capabilities
SYSTEM_PROMPT = """You are a financial analyst assistant helping users understand their portfolio data.
You have access to anonymized portfolio information including margin requirements, positions, and balances.
Always provide clear, actionable insights based on the data provided.
Never mention account numbers or personal information in your responses.
When discussing specific accounts, refer to them by their anonymized IDs (e.g., ACCOUNT_XXXXX).

IMPORTANT: When the user asks for visualizations, charts, or to "show" data visually, 
you should respond with structured JSON that includes visualization instructions.
Format your response as:
{
  "text": "Your explanation here",
  "visualization": {
    "type": "chart|table|risk-matrix",
    "title": "Title for the visualization",
    "description": "Brief description",
    "data": { ... }
  }
}

For regular text responses without visualizations, just return plain text."""
class VisualizationData(BaseModel):
    type: Literal["chart", "table", "risk-matrix", "custom"]
    title: str
    description: Optional[str] = None
    data: Dict[str, Any]
    config: Optional[Dict[str, Any]] = None

class EnhancedChatResponse(BaseModel):
    question: str
    answer: str
    provider: str
    visualization: Optional[VisualizationData] = None


def generate_query_hash(question: str, provider: str, include_historical: bool) -> str:
    """Generate a stable hash for the query to use as cache key."""
    content = f"{question}:{provider}:{include_historical}"
    return hashlib.md5(content.encode()).hexdigest()[:12]


def clean_json_string(json_str: str) -> str:
    """Clean up common JSON formatting issues from LLM responses."""
    # Remove markdown code block markers
    json_str = re.sub(r'^```json\s*', '', json_str.strip())
    json_str = re.sub(r'```$', '', json_str.strip())
    
    # Fix single quotes to double quotes, but preserve escaped quotes
    # First, temporarily replace escaped quotes
    json_str = json_str.replace(r'\"', '<<<ESCAPED_QUOTE>>>')
    json_str = json_str.replace(r"\'", '<<<ESCAPED_SINGLE>>>')
    
    # Replace single quotes with double quotes
    # This regex matches single quotes that are not part of the content
    json_str = re.sub(r"(?<![\\])'([^']*?)(?<![\\])'", r'"\1"', json_str)
    
    # Restore escaped quotes
    json_str = json_str.replace('<<<ESCAPED_QUOTE>>>', r'\"')
    json_str = json_str.replace('<<<ESCAPED_SINGLE>>>', r"\'")
    
    # Fix common trailing commas
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*]', ']', json_str)
    
    # Fix unquoted keys (basic approach)
    json_str = re.sub(r'(\w+):', r'"\1":', json_str)
    # But don't double-quote already quoted keys
    json_str = re.sub(r'"\"(\w+)\"":', r'"\1":', json_str)
    
    return json_str

def normalize_visualization_type(viz_type: str) -> str:
    """Normalize visualization type to expected values."""
    viz_type = viz_type.lower().strip()
    
    # Map common variations to standard types
    type_mapping = {
        'bar': 'chart',
        'bar_chart': 'chart',
        'barchart': 'chart',
        'line': 'chart',
        'line_chart': 'chart',
        'linechart': 'chart',
        'pie': 'chart',
        'pie_chart': 'chart',
        'piechart': 'chart',
        'scatter': 'chart',
        'area': 'chart',
        'risk_matrix': 'risk-matrix',
        'riskmatrix': 'risk-matrix',
        'matrix': 'risk-matrix',
        'data_table': 'table',
        'datatable': 'table',
        'grid': 'table'
    }
    
    return type_mapping.get(viz_type, viz_type)

def extract_json_from_text(text: str) -> Optional[Dict[str, Any]]:
    """Extract JSON from text using multiple strategies."""
    # Strategy 1: Look for ```json blocks
    json_block_match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL | re.IGNORECASE)
    if json_block_match:
        json_str = json_block_match.group(1)
        cleaned = clean_json_string(json_str)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError as e:
            logger.debug(f"Failed to parse JSON block: {e}")
    
    # Strategy 2: Look for any JSON-like structure
    # This regex looks for a top-level object {...}
    json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
    matches = re.findall(json_pattern, text, re.DOTALL)
    
    for match in reversed(matches):  # Start from the end (likely the main response)
        try:
            cleaned = clean_json_string(match)
            data = json.loads(cleaned)
            if isinstance(data, dict) and ('visualization' in data or 'text' in data):
                return data
        except json.JSONDecodeError:
            continue
    
    # Strategy 3: Try the entire text as JSON
    try:
        cleaned = clean_json_string(text)
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass
    
    return None

def parse_llm_response(response: str) -> tuple[str, Optional[VisualizationData]]:
    """Parse LLM response to extract text and visualization data."""
    try:
        # Extract JSON data from response
        json_data = extract_json_from_text(response)
        
        if json_data and isinstance(json_data, dict):
            # Check if it has visualization data
            if 'visualization' in json_data:
                viz_data = json_data['visualization']
                
                # Normalize the visualization type
                if 'type' in viz_data:
                    viz_data['type'] = normalize_visualization_type(viz_data['type'])
                
                # Extract text content
                text_content = json_data.get('text', '')
                
                # If no text in JSON, try to extract from original response
                if not text_content:
                    # Remove the JSON part from response to get text
                    json_match = re.search(r'```json.*?```', response, re.DOTALL)
                    if json_match:
                        text_content = response.replace(json_match.group(0), '').strip()
                    else:
                        # Try to find where JSON starts
                        json_start = response.find('{')
                        if json_start > 0:
                            text_content = response[:json_start].strip()
                
                # Create visualization object
                try:
                    visualization = VisualizationData(
                        type=viz_data.get('type', 'chart'),
                        title=viz_data.get('title', 'Visualization'),
                        description=viz_data.get('description'),
                        data=viz_data.get('data', {}),
                        config=viz_data.get('config')
                    )
                    return text_content, visualization
                except Exception as e:
                    logger.warning(f"Failed to create VisualizationData: {e}")
                    logger.debug(f"Visualization data: {viz_data}")
            
            # JSON found but no visualization
            return json_data.get('text', response), None
        
        # No JSON found, return as plain text
        return response, None
        
    except Exception as e:
        logger.error(f"Error parsing LLM response: {e}")
        logger.debug(f"Response was: {response[:500]}...")
        return response, None

def create_visualization_for_query(question: str, portfolio_data: dict) -> Optional[VisualizationData]:
    """Generate visualization based on query type."""
    lower_q = question.lower()
    
    # Top risky positions
    if any(term in lower_q for term in ["risky", "risk", "volatile", "dangerous"]):
        # Extract positions with highest margin requirements
        positions = []
        for acc in portfolio_data.get("accounts", []):
            if "positions" in acc:
                for pos in acc["positions"]:
                    positions.append({
                        "account": acc["account_id"],
                        "symbol": pos.get("symbol", "Unknown"),
                        "margin": pos.get("margin_requirement", 0),
                        "value": pos.get("market_value", 0)
                    })
        
        # Sort by margin requirement
        positions.sort(key=lambda x: x["margin"], reverse=True)
        top_5 = positions[:5]
        
        if top_5:
            return VisualizationData(
                type="chart",
                title="Top 5 Riskiest Positions by Margin Requirement",
                description="Positions requiring the highest margin",
                data={
                    "labels": [f"{p['symbol']} ({p['account']})" for p in top_5],
                    "datasets": [{
                        "label": "Margin Requirement",
                        "data": [p["margin"] for p in top_5],
                        "backgroundColor": "rgba(255, 99, 132, 0.5)",
                        "borderColor": "rgba(255, 99, 132, 1)",
                        "borderWidth": 1
                    }]
                }
            )    
    # Margin calls table
    elif any(term in lower_q for term in ["margin call", "calls", "margin requirements"]):
        accounts_with_calls = []
        for acc in portfolio_data.get("accounts", []):
            if acc.get("margin", 0) > acc.get("equity", 0) * 0.3:  # Example threshold
                accounts_with_calls.append({
                    "account": acc["account_id"],
                    "margin": acc.get("margin", 0),
                    "equity": acc.get("equity", 0),
                    "ratio": acc.get("margin", 0) / max(acc.get("equity", 1), 1)
                })
        
        if accounts_with_calls:
            return VisualizationData(
                type="table",
                title="Accounts with Potential Margin Calls",
                description="Accounts where margin exceeds safe thresholds",
                data={
                    "headers": ["Account", "Margin Required", "Equity", "Margin Ratio"],
                    "rows": [
                        [
                            acc["account"],
                            f"${acc['margin']:,.0f}",
                            f"${acc['equity']:,.0f}",
                            f"{acc['ratio']:.1%}"
                        ]
                        for acc in accounts_with_calls
                    ],
                    "sortable": True
                }
            )
    
    # Portfolio comparison across scenarios
    elif any(term in lower_q for term in ["compare", "scenarios", "stress test"]):
        # This would need actual scenario data from the backend
        return VisualizationData(
            type="chart",
            title="Portfolio Value Across Risk Scenarios",
            description="How your portfolio performs under different market conditions",
            data={
                "labels": ["Current", "-5% Market", "-10% Market", "+5% Market", "+10% Market"],
                "datasets": [{
                    "label": "Portfolio Value",
                    "data": [1000000, 950000, 900000, 1050000, 1100000],  # Example data
                    "borderColor": "rgb(75, 192, 192)",
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "tension": 0.1
                }]
            },
            config={
                "type": "line"
            }
        )
    
    return None

@router.post("/query", response_model=EnhancedChatResponse)
async def query_portfolio(
    query: ChatQuery,
    llm_service: LLMServiceDep,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep
):
    """Process natural language query about portfolio with visualization support."""
    try:
        # Generate cache key based on query content
        query_hash = generate_query_hash(query.question, query.provider, query.include_historical)
        cache_key = cache.cache_key("chat", query_hash)
        
        # Check cache first (5 minute TTL for chat responses)
        cached_response = await cache.get(cache_key)
        if cached_response:
            logger.info(f"Cache HIT for chat query: {query.question[:50]}...")
            return EnhancedChatResponse(**cached_response)
        
        logger.info(f"Cache MISS for chat query: {query.question[:50]}...")
        
        # Initialize anonymizer (though data comes pre-anonymized)
        anonymizer = DataAnonymizer()
        
        # Fetch current portfolio data with positions (this might also hit cache)
        portfolio_data = await grpc_client.get_portfolio_with_risk_profile(10006)
        
        # Check if we can generate a visualization directly
        visualization = create_visualization_for_query(query.question, portfolio_data)        
        # Optionally include historical data
        historical_context = ""
        if query.include_historical:
            try:
                historical_data = await grpc_client.get_historical_data(10006, days=7)
                if historical_data:
                    historical_context = f"\n\nHistorical data (last 7 days): {len(historical_data)} data points available."
            except Exception as e:
                logger.warning(f"Failed to fetch historical data: {e}")
        
        # Create context for LLM - include positions detail
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
                    "risk_type": acc.get("risk_type"),
                    "positions_count": len(acc.get("positions", [])),
                    "positions": [
                        {
                            "symbol": pos.get("symbol"),
                            "quantity": pos.get("quantity"),
                            "market_value": pos.get("market_value"),
                            "cost_basis": pos.get("cost_basis"),
                            "unrealized_pnl": pos.get("unrealized_pnl"),
                            "margin_requirement": pos.get("margin_requirement")
                        }
                        for pos in acc.get("positions", [])[:5]  # Limit to first 5 positions per account for context size
                    ] if acc.get("positions") else []
                }
                for acc in portfolio_data.get("accounts", [])
            ]
        }        
        # Enhanced prompt that encourages visualization
        visualization_hint = """
Remember: If the user asks to "show", "visualize", "chart", or "display" data, 
respond with JSON that includes a visualization object.
""" if any(word in query.question.lower() for word in ["show", "chart", "visualize", "display", "graph"]) else ""
        
        # Construct prompt
        prompt = f"""Portfolio Data:
{json.dumps(portfolio_context, indent=2)}
{historical_context}

User Question: {query.question}

{visualization_hint}

Please provide a clear, helpful response based on the portfolio data above. Be specific and actionable."""
        
        # Query LLM
        response = await llm_service.query(
            prompt=prompt,
            provider=query.provider,
            system_prompt=SYSTEM_PROMPT
        )
        
        # Parse response for visualization
        text_response, llm_visualization = parse_llm_response(response)
        
        # Use LLM visualization if provided, otherwise use our generated one
        final_visualization = llm_visualization or visualization
        
        # Create response
        result = EnhancedChatResponse(
            question=query.question,
            answer=text_response or response,
            provider=query.provider,
            visualization=final_visualization
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
            "Show me accounts with margin calls",
            "Chart my top 5 riskiest positions",
            "Visualize portfolio performance across scenarios",
            "Display a table of accounts approaching PDT limits",
            "What are my current margin requirements?",
            "Show me P&L trends for the last week",
            "Which accounts have the highest margin utilization?",
            "Create a risk matrix for my portfolio",
            "Graph the concentration of my positions"
        ]
    }
