"""Response models."""
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class ChatResponse(BaseModel):
    """Chat query response."""
    question: str
    answer: str
    provider: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AccountData(BaseModel):
    """Individual account data."""
    account_id: str
    margin: float
    buying_power: float
    excess_liquidity: float
    margin_utilization: float
    unrealized_pl: float = 0
    realized_pl: float = 0
    positions_count: int = 0


class PortfolioData(BaseModel):
    """Portfolio data response."""
    group_id: int
    accounts: List[AccountData]
    timestamp: datetime
    total_margin: float
    total_buying_power: Optional[float] = None
    total_pl: Optional[float] = None


class HistoricalSnapshot(BaseModel):
    """Historical data snapshot."""
    timestamp: str
    data: Dict[str, Any]


class HistoricalData(BaseModel):
    """Historical data response."""
    group_id: int
    days: int
    snapshots: List[HistoricalSnapshot]
    data_points: int


class ChartData(BaseModel):
    """Visualization chart data."""
    title: str
    type: str  # 'line', 'bar', 'radar', 'pie'
    data: Dict[str, Any]  # Chart.js compatible data
    options: Optional[Dict[str, Any]] = None
