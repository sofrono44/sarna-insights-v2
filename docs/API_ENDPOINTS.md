# API Endpoints Summary

## Base URL: http://localhost:8000

### Health Checks
- GET /api/health/ - Basic health check
- GET /api/health/ready - Readiness check with dependencies

### Chat API
- POST /api/chat - Send natural language query
  ```json
  {
    "question": "What is my total margin?",
    "provider": "google"  // optional: "openai", "anthropic", "google"
  }
  ```

### Data API
- GET /api/data/portfolio/current - Current portfolio data (cached 30s)
- GET /api/data/portfolio/historical?days=7 - Historical snapshots
- GET /api/data/accounts - List all accounts
- POST /api/data/refresh - Force refresh all cached data

### Visualization API
- GET /api/viz/margin-utilization - Margin utilization by account
- GET /api/viz/portfolio-summary - Summary statistics
- GET /api/viz/historical-trends?days=30 - Historical trend data

### LLM Management
- GET /api/chat/providers - List available LLM providers
- POST /api/chat/provider - Set default provider
  ```json
  {
    "provider": "google"
  }
  ```

## Example Usage

### Test Chat Endpoint
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is my total margin requirement?"}'
```

### Get Current Portfolio
```bash
curl http://localhost:8000/api/data/portfolio/current
```

### Force Refresh Data
```bash
curl -X POST http://localhost:8000/api/data/refresh
```

## Notes
- All responses include timestamps in UTC
- Account IDs are pre-anonymized (ACCOUNT_XXXXX)
- Historical data is cached forever (immutable)
- Current data is cached for 30 seconds
- Chat responses are cached for 5 minutes
