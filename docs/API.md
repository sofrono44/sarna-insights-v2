# API Documentation

## Base URL
- Development: `http://localhost:8000`
- Production: TBD

## Authentication
Currently using static JWT token in environment variables. Future versions will implement proper auth flow.

## Endpoints

### Health Check
```
GET /api/health/
```
Returns service health status.

### Chat/NLP

#### Query Portfolio
```
POST /api/chat/query
Content-Type: application/json

{
  "question": "What is my total portfolio value?",
  "provider": "openai"  // or "anthropic", "google"
}
```

#### Get Example Queries
```
GET /api/chat/examples
```

### Data

#### Get Portfolio Data
```
GET /api/data/portfolio/{group_id}
```

#### Get Historical Data
```
GET /api/data/history/{group_id}?days=30
```

#### Refresh Data
```
POST /api/data/refresh/{group_id}
```

### Visualizations

#### Portfolio Overview
```
GET /api/viz/portfolio-overview/{group_id}
```

#### P&L Trends
```
GET /api/viz/pl-trends/{group_id}?days=7
```

#### Risk Metrics
```
GET /api/viz/risk-metrics/{group_id}
```

## Response Format

All endpoints return JSON responses with appropriate HTTP status codes.

### Success Response
```json
{
  "data": { ... },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Error Response
```json
{
  "detail": "Error message",
  "status_code": 400
}
```
