// Liquidation Alert types
export interface LiquidationAlert {
  alert_id: number;
  account_number: string;
  position_symbol: string;
  quantity: number;
  current_value: number;
  liquidation_time: string;
  reason: string;
  priority: 'immediate' | 'eod' | 'warning';
}

// Mock liquidation alerts
export const mockLiquidationAlerts: LiquidationAlert[] = [
  {
    alert_id: 1,
    account_number: "ACCOUNT_29837",
    position_symbol: "AAPL 250C",
    quantity: 50,
    current_value: 125000,
    liquidation_time: "3:30 PM EST",
    reason: "Insufficient margin to hold position overnight",
    priority: "eod"
  },
  {
    alert_id: 2,
    account_number: "ACCOUNT_74231",
    position_symbol: "TSLA 300P",
    quantity: 100,
    current_value: 200000,
    liquidation_time: "IMMEDIATE",
    reason: "Account in margin call - automatic liquidation initiated",
    priority: "immediate"
  },
  {
    alert_id: 3,
    account_number: "ACCOUNT_56453",
    position_symbol: "SPY 450C",
    quantity: 25,
    current_value: 62500,
    liquidation_time: "3:45 PM EST",
    reason: "Day trading buying power exceeded",
    priority: "eod"
  },
  {
    alert_id: 4,
    account_number: "ACCOUNT_85412",
    position_symbol: "NVDA 800C",
    quantity: 30,
    current_value: 90000,
    liquidation_time: "2:00 PM EST",
    reason: "Pattern day trader restriction - position must be closed",
    priority: "warning"
  }
];
