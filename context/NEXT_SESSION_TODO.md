# Next Session TODO - Test Alerts & Complete Frontend

## Priority 1: Test Alert Endpoints
```bash
# Test the new alerts endpoint
curl http://localhost/api/data/alerts?page=1&page_size=10

# Or in browser:
http://localhost/api/data/alerts
```

Expected response structure:
```json
{
  "alerts": [
    {
      "alert_id": 123,
      "account_number": "ACCOUNT_12345",
      "message": "Margin utilization above 80%",
      "severity": "warning",
      "status": "open",
      "current_value": 85.5,
      ...
    }
  ],
  "page": 1,
  "page_size": 10,
  "total_count": 25
}
```

## Priority 2: Complete Risk Matrix Frontend

### Add 15 Risk Scenario Columns
```typescript
const riskScenarioColumns = [
  { id: 'scenario_1', label: 'S1: -15%', description: 'Px -15%, IV +50%/-20%' },
  { id: 'scenario_2', label: 'S2: -12%', description: 'Px -12%' },
  { id: 'scenario_3', label: 'S3: -10%', description: 'Px -10%, IV +40%/-15%' },
  // ... etc for all 15
];
```

### Implement 3-Row Display for Options
- Main row: white background, shows symbol
- Volatility Up row: light green background (bg-green-50)
- Volatility Down row: light red background (bg-red-50)

## Priority 3: Add Alerts to Frontend

### Create Alert Component
```typescript
interface Alert {
  alert_id: number;
  account_number: string;
  message: string;
  severity: 'warning' | 'critical';
  status: 'open' | 'acknowledged' | 'resolved';
  current_value: number;
}

// Fetch alerts
const { data: alerts } = await fetch('/api/data/alerts');
```

### Display Options
1. Alert badge in header showing count
2. Alert icon next to affected accounts
3. Dedicated alerts panel/drawer
4. Color code by severity (yellow for warning, red for critical)

## Testing Checklist
- [ ] Verify alerts endpoint returns data
- [ ] Check alert caching (5 min TTL)
- [ ] Test pagination parameters
- [ ] Verify 15 risk columns display
- [ ] Check options 3-row format
- [ ] Test column selector with new columns
- [ ] Ensure proper color coding

## Key Files Changed This Session
- `/protos/alerts*.proto` - New alert proto files
- `/protos/common.proto` - Updated with DurationValue
- `/backend/services/grpc_client.py` - Added get_alerts()
- `/backend/routers/data.py` - Added /alerts endpoint
- `/backend/generated/alerts*.py` - Generated alert Python files