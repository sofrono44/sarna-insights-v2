// Pattern Day Trader Alert types
export interface PDTAlert {
  alert_id: number;
  account_number: string;
  day_trades_count: number;
  rolling_5_day_count: number;
  status: 'approaching' | 'flagged' | 'restricted';
  last_trade_date: string;
  equity: number;
  minimum_equity_required: number;
}

// Mock PDT alerts
export const mockPDTAlerts: PDTAlert[] = [
  {
    alert_id: 1,
    account_number: "ACCOUNT_56453",
    day_trades_count: 3,
    rolling_5_day_count: 3,
    status: "approaching",
    last_trade_date: new Date().toISOString(),
    equity: 28000,
    minimum_equity_required: 25000
  },
  {
    alert_id: 2,
    account_number: "ACCOUNT_65283",
    day_trades_count: 4,
    rolling_5_day_count: 4,
    status: "flagged",
    last_trade_date: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
    equity: 23000,
    minimum_equity_required: 25000
  },
  {
    alert_id: 3,
    account_number: "ACCOUNT_85412",
    day_trades_count: 5,
    rolling_5_day_count: 5,
    status: "restricted",
    last_trade_date: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
    equity: 22000,
    minimum_equity_required: 25000
  }
];
