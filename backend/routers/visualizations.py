"""Visualization data endpoints with caching."""
from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any
from api.dependencies import GRPCClientDep, CacheServiceDep
from models.responses import ChartData
from services.time_machine import TimeMachineService
import logging
from datetime import datetime

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
        # Try to get from cache first
        cache_key = cache.cache_key("viz", "portfolio-overview", group_id)
        cached_data = await cache.get(cache_key)
        if cached_data:
            logger.info("Returning cached portfolio overview")
            return ChartData(**cached_data)
        
        # Get current portfolio data (this might also be cached)
        portfolio_data = await grpc_client.get_current_margin_data(group_id)
        accounts = portfolio_data.get("accounts", [])
        
        # Transform for chart
        chart_data = {
            "labels": [acc.get("account_id", f"Account {i}") for i, acc in enumerate(accounts)],
            "datasets": [{
                "label": "Margin Requirements",
                "data": [float(acc.get("margin", 0)) for acc in accounts],
                "backgroundColor": "rgba(255, 99, 132, 0.5)"
            }, {
                "label": "Buying Power",
                "data": [float(acc.get("buying_power", 0)) for acc in accounts],
                "backgroundColor": "rgba(54, 162, 235, 0.5)"
            }]
        }
        
        result = ChartData(
            title="Portfolio Overview",
            type="bar",
            data=chart_data,
            options={
                "responsive": True,
                "plugins": {
                    "title": {
                        "display": True,
                        "text": f"Account Margin & Buying Power - Group {group_id}"
                    }
                }
            }
        )
        
        # Cache for 30 seconds
        await cache.set(cache_key, result.model_dump(mode='json'), ttl=30)
        
        return result
        
    except Exception as e:
        logger.error(f"Failed to generate portfolio overview: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/pl-trends/{group_id}", response_model=ChartData)
async def get_pl_trends(
    group_id: int,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep,
    days: int = Query(default=7, ge=1, le=30)
):
    """Get P&L trends visualization data."""
    try:
        # Create time machine service
        time_machine = TimeMachineService(grpc_client, cache)
        
        # Get trend data
        trend_data = await time_machine.get_portfolio_trends(
            group_id=group_id,
            days=days,
            metric="day_pnl"
        )
        
        # Get daily summaries for aggregated view
        daily_summaries = await time_machine.get_daily_summaries(group_id, days)
        
        # Transform for chart
        chart_data = {
            "labels": [summary["date"] for summary in daily_summaries],
            "datasets": [{
                "label": "Daily P&L",
                "data": [summary["total_pnl"] for summary in daily_summaries],
                "borderColor": "rgb(75, 192, 192)",
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "tension": 0.1
            }, {
                "label": "Max P&L",
                "data": [summary["max_pnl"] for summary in daily_summaries],
                "borderColor": "rgb(54, 162, 235)",
                "backgroundColor": "rgba(54, 162, 235, 0.2)",
                "borderDash": [5, 5],
                "tension": 0.1
            }]
        }
        
        return ChartData(
            title=f"P&L Trends ({days} days)",
            type="line",
            data=chart_data,
            options={
                "responsive": True,
                "plugins": {
                    "title": {
                        "display": True,
                        "text": f"Daily P&L Performance - {trend_data['statistics']['trend_direction'].title()} {abs(trend_data['statistics']['trend_percent']):.1f}%"
                    }
                }
            }
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
        # Try cache first
        cache_key = cache.cache_key("viz", "risk-metrics", group_id)
        cached_data = await cache.get(cache_key)
        if cached_data:
            return ChartData(**cached_data)
        
        # Get current portfolio data
        portfolio_data = await grpc_client.get_current_margin_data(group_id)
        accounts = portfolio_data.get("accounts", [])
        
        # Calculate average metrics
        avg_credit_util = sum(acc.get("credit_utilization", 0) for acc in accounts) / len(accounts) if accounts else 0
        avg_excess_liq_ratio = sum(
            acc.get("excess_liquidity", 0) / acc.get("net_liquidity", 1) * 100 
            for acc in accounts
        ) / len(accounts) if accounts else 0
        
        # Risk categories
        chart_data = {
            "labels": [
                "Credit Utilization %",
                "Excess Liquidity %",
                "Account Concentration",
                "Margin Coverage"
            ],
            "datasets": [{
                "label": "Current Risk Profile",
                "data": [
                    avg_credit_util,
                    avg_excess_liq_ratio,
                    100 / len(accounts) if accounts else 0,  # Lower is better
                    100 - avg_credit_util  # Margin coverage
                ],
                "backgroundColor": 'rgba(255, 99, 132, 0.2)',
                "borderColor": 'rgba(255, 99, 132, 1)',
                "pointBackgroundColor": 'rgba(255, 99, 132, 1)',
                "pointBorderColor": '#fff',
                "pointHoverBackgroundColor": '#fff',
                "pointHoverBorderColor": 'rgba(255, 99, 132, 1)'
            }]
        }
        
        result = ChartData(
            title="Risk Metrics",
            type="radar",
            data=chart_data,
            options={
                "responsive": True,
                "scales": {
                    "r": {
                        "beginAtZero": True,
                        "max": 100
                    }
                }
            }
        )
        
        # Cache for 30 seconds
        await cache.set(cache_key, result.model_dump(mode='json'), ttl=30)
        
        return result
        
    except Exception as e:
        logger.error(f"Failed to generate risk metrics: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/liquidity-trends/{group_id}", response_model=ChartData)
async def get_liquidity_trends(
    group_id: int,
    grpc_client: GRPCClientDep,
    cache: CacheServiceDep,
    days: int = Query(default=7, ge=1, le=30)
):
    """Get liquidity trends over time."""
    try:
        # Create time machine service
        time_machine = TimeMachineService(grpc_client, cache)
        
        # Get trend data for net liquidity
        trend_data = await time_machine.get_portfolio_trends(
            group_id=group_id,
            days=days,
            metric="net_liquidity"
        )
        
        # Sample the data for visualization (max 50 points)
        all_points = trend_data["trend_data"]
        if len(all_points) > 50:
            # Sample evenly
            step = len(all_points) // 50
            sampled_points = all_points[::step]
        else:
            sampled_points = all_points
        
        # Transform for chart
        chart_data = {
            "labels": [point["timestamp"] for point in sampled_points],
            "datasets": [{
                "label": "Net Liquidity",
                "data": [point["value"] for point in sampled_points],
                "borderColor": "rgb(153, 102, 255)",
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "tension": 0.1,
                "fill": True
            }]
        }
        
        return ChartData(
            title=f"Liquidity Trends ({days} days)",
            type="line",
            data=chart_data,
            options={
                "responsive": True,
                "plugins": {
                    "title": {
                        "display": True,
                        "text": f"Net Liquidity - Avg: ${trend_data['statistics']['average']:,.0f}"
                    }
                },
                "scales": {
                    "y": {
                        "ticks": {
                            "callback": "function(value) { return '$' + value.toLocaleString(); }"
                        }
                    }
                }
            }
        )
        
    except Exception as e:
        logger.error(f"Failed to generate liquidity trends: {e}")
        raise HTTPException(status_code=500, detail=str(e))
