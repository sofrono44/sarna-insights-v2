"""Visualization data endpoints."""
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from api.dependencies import GRPCClientDep, CacheServiceDep
from models.responses import ChartData
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/portfolio-overview/{group_id}", response_model=ChartData)
async def get_portfolio_overview(
    group_id: int,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep
):
    """Get data for portfolio overview visualization."""
    try:
        # Get current portfolio data
        portfolio_data = await grpc_client.get_current_margin_data(group_id)
        
        # Transform for chart
        accounts = portfolio_data.get("accounts", [])
        
        chart_data = {
            "labels": [acc.get("id", f"Account {i}") for i, acc in enumerate(accounts)],
            "datasets": [{
                "label": "Margin Requirements",
                "data": [acc.get("margin", 0) for acc in accounts]
            }, {
                "label": "Buying Power",
                "data": [acc.get("buying_power", 0) for acc in accounts]
            }]
        }
        
        return ChartData(
            title="Portfolio Overview",
            type="bar",
            data=chart_data
        )
        
    except Exception as e:
        logger.error(f"Failed to generate portfolio overview: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/pl-trends/{group_id}", response_model=ChartData)
async def get_pl_trends(
    group_id: int,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep,
    days: int = 7
):
    """Get P&L trends visualization data."""
    try:
        # Get historical data
        historical = await grpc_client.get_historical_data(group_id, days)
        
        # Transform for chart
        timestamps = []
        pl_values = []
        
        for snapshot in historical:
            timestamps.append(snapshot["timestamp"])
            # Calculate total P&L from snapshot data
            total_pl = sum(
                acc.get("unrealized_pl", 0) + acc.get("realized_pl", 0)
                for acc in snapshot.get("data", {}).get("accounts", [])
            )
            pl_values.append(total_pl)
        
        chart_data = {
            "labels": timestamps,
            "datasets": [{
                "label": "Total P&L",
                "data": pl_values,
                "borderColor": "rgb(75, 192, 192)",
                "tension": 0.1
            }]
        }
        
        return ChartData(
            title=f"P&L Trends ({days} days)",
            type="line",
            data=chart_data
        )
        
    except Exception as e:
        logger.error(f"Failed to generate P&L trends: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/risk-metrics/{group_id}", response_model=ChartData)
async def get_risk_metrics(
    group_id: int,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep
):
    """Get risk metrics visualization data."""
    try:
        # Get current portfolio data
        portfolio_data = await grpc_client.get_current_margin_data(group_id)
        accounts = portfolio_data.get("accounts", [])
        
        # Calculate risk metrics
        chart_data = {
            "labels": ["Margin Utilization", "Leverage", "Risk Score"],
            "datasets": [{
                "label": "Portfolio Risk Metrics",
                "data": [
                    # Average margin utilization
                    sum(acc.get("margin_utilization", 0) for acc in accounts) / len(accounts) if accounts else 0,
                    # Average leverage
                    sum(acc.get("leverage", 1) for acc in accounts) / len(accounts) if accounts else 1,
                    # Risk score (placeholder calculation)
                    sum(acc.get("risk_score", 50) for acc in accounts) / len(accounts) if accounts else 50
                ],
                "backgroundColor": [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)'
                ]
            }]
        }
        
        return ChartData(
            title="Risk Metrics",
            type="radar",
            data=chart_data
        )
        
    except Exception as e:
        logger.error(f"Failed to generate risk metrics: {e}")
        raise HTTPException(status_code=500, detail=str(e))
