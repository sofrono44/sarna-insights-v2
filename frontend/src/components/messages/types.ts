// Message types
export interface Message {
  message_id: number;
  from: string;
  subject: string;
  preview: string;
  full_content: string;
  timestamp: string;
  read: boolean;
  category: 'compliance' | 'risk' | 'operations' | 'general';
  priority: 'high' | 'normal' | 'low';
}

export interface MessagesResponse {
  messages: Message[];
  unread_count: number;
  total_count: number;
}

// Mock messages data
export const mockMessages: Message[] = [
  {
    message_id: 1,
    from: "Risk Management",
    subject: "Daily Risk Report - Elevated VaR",
    preview: "Today's portfolio VaR has increased to $125,000...",
    full_content: "Today's portfolio VaR has increased to $125,000, representing a 15% increase from yesterday. This is primarily driven by increased volatility in tech sector holdings. Please review position sizes in AAPL and MSFT options.",
    timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
    read: false,
    category: "risk",
    priority: "high"
  },
  {
    message_id: 2,
    from: "Compliance",
    subject: "Reg T Margin Requirements Update",
    preview: "New regulatory requirements effective next week...",
    full_content: "New regulatory requirements effective next week will change initial margin requirements for certain option strategies. Please review the attached documentation and ensure all accounts remain compliant.",
    timestamp: new Date(Date.now() - 5 * 60 * 60 * 1000).toISOString(),
    read: false,
    category: "compliance",
    priority: "high"
  },
  {
    message_id: 3,
    from: "Operations",
    subject: "System Maintenance - Saturday 2AM EST",
    preview: "Scheduled maintenance window this Saturday...",
    full_content: "Scheduled maintenance window this Saturday from 2AM to 6AM EST. Trading systems will be unavailable during this time. Please ensure all critical orders are placed before the maintenance window.",
    timestamp: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
    read: true,
    category: "operations",
    priority: "normal"
  },
  {
    message_id: 4,
    from: "Risk Management",
    subject: "Options Expiry Alert - 45 Positions",
    preview: "You have 45 option positions expiring this Friday...",
    full_content: "You have 45 option positions expiring this Friday across 7 accounts. Total notional value: $2.3M. Please review and take appropriate action before expiry.",
    timestamp: new Date(Date.now() - 3 * 60 * 60 * 1000).toISOString(),
    read: false,
    category: "risk",
    priority: "high"
  },
  {
    message_id: 5,
    from: "Trading Desk",
    subject: "Market Alert - Volatility Spike",
    preview: "VIX has spiked 25% in the last hour...",
    full_content: "VIX has spiked 25% in the last hour following Fed announcement. Consider reviewing portfolio hedges and adjusting position sizes accordingly.",
    timestamp: new Date(Date.now() - 1 * 60 * 60 * 1000).toISOString(),
    read: false,
    category: "general",
    priority: "high"
  },
  {
    message_id: 6,
    from: "Compliance",
    subject: "Monthly Compliance Review Complete",
    preview: "Your monthly compliance review has been completed...",
    full_content: "Your monthly compliance review has been completed. All accounts are in good standing. No violations detected. Next review scheduled for March 15th.",
    timestamp: new Date(Date.now() - 48 * 60 * 60 * 1000).toISOString(),
    read: true,
    category: "compliance",
    priority: "low"
  }
];
