// Call types
export interface Call {
  call_id: number;
  account_number: string;
  call_type: 'fed' | 'house';
  amount: number;
  due_date: string;
  created_date: string;
  status: 'pending' | 'met' | 'overdue';
  description: string;
}

// Mock calls data
export const mockCalls: Call[] = [
  {
    call_id: 1,
    account_number: "ACCOUNT_65283",
    call_type: "fed",
    amount: 25000,
    due_date: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(),
    created_date: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
    status: "pending",
    description: "Federal margin call due to overnight position changes"
  },
  {
    call_id: 2,
    account_number: "ACCOUNT_29837",
    call_type: "house",
    amount: 15000,
    due_date: new Date(Date.now() + 48 * 60 * 60 * 1000).toISOString(),
    created_date: new Date(Date.now() - 5 * 60 * 60 * 1000).toISOString(),
    status: "pending",
    description: "House call triggered by concentrated position in TSLA options"
  },
  {
    call_id: 3,
    account_number: "ACCOUNT_74231",
    call_type: "fed",
    amount: 50000,
    due_date: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
    created_date: new Date(Date.now() - 72 * 60 * 60 * 1000).toISOString(),
    status: "overdue",
    description: "Federal margin call - URGENT: Overdue by 1 day"
  }
];
