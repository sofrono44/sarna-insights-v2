// Alert types based on backend schema
export interface Alert {
  alert_id: number;
  account_id: number;
  account_number: string;
  alert_rule_id: number;
  message: string;
  current_value: number;
  severity: 'warning' | 'critical';
  status: 'open' | 'acknowledged' | 'resolved';
  created_time: string;
  last_notification_time?: string;
  resolved_time?: string;
  acknowledged_time?: string;
  acknowledged_user_id?: number;
}

export interface AlertsResponse {
  alerts: Alert[];
  page: number;
  page_size: number;
  total_count: number;
}

// Mock data for demo purposes since backend returns UNIMPLEMENTED
export const mockAlerts: Alert[] = [
  {
    alert_id: 1,
    account_id: 10001,
    account_number: "ACCOUNT_65283",
    alert_rule_id: 101,
    message: "Margin utilization above 80%",
    current_value: 82.5,
    severity: "warning",
    status: "open",
    created_time: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(), // 2 hours ago
    last_notification_time: new Date(Date.now() - 30 * 60 * 1000).toISOString(), // 30 min ago
  },
  {
    alert_id: 2,
    account_id: 10002,
    account_number: "ACCOUNT_56453",
    alert_rule_id: 102,
    message: "Portfolio concentration risk - Single position exceeds 25% of NAV",
    current_value: 28.3,
    severity: "warning",
    status: "acknowledged",
    created_time: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(), // 1 day ago
    acknowledged_time: new Date(Date.now() - 20 * 60 * 60 * 1000).toISOString(),
    acknowledged_user_id: 1001,
  },
  {
    alert_id: 3,
    account_id: 10003,
    account_number: "ACCOUNT_29837",
    alert_rule_id: 103,
    message: "Credit limit approaching - 95% utilized",
    current_value: 95.2,
    severity: "critical",
    status: "open",
    created_time: new Date(Date.now() - 1 * 60 * 60 * 1000).toISOString(), // 1 hour ago
    last_notification_time: new Date(Date.now() - 15 * 60 * 1000).toISOString(), // 15 min ago
  },
  {
    alert_id: 4,
    account_id: 10004,
    account_number: "ACCOUNT_74231",
    alert_rule_id: 104,
    message: "Maintenance margin call imminent",
    current_value: 1.05,
    severity: "critical",
    status: "open",
    created_time: new Date(Date.now() - 30 * 60 * 1000).toISOString(), // 30 minutes ago
    last_notification_time: new Date(Date.now() - 5 * 60 * 1000).toISOString(), // 5 min ago
  },
];
