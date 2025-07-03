# Quick Start - Next Session

## 🚀 Verify Everything is Working

```bash
# 1. Start all services
cd C:\Development\sarna-insights-v2
docker-compose up -d

# 2. Check services are running
docker-compose ps

# 3. Test backend is responding
curl http://localhost:8000/api/health/

# 4. Test gRPC connection
docker-compose exec backend python test_grpc_connection.py

# 5. Test cache is working
docker-compose exec backend python test_cache_service.py

# 6. Test API endpoints
docker-compose exec backend python test_api_cache.py
```

## 📊 Current State Summary

### What's Working:
- ✅ gRPC connection to Sarna API
- ✅ Redis caching (102x performance improvement)
- ✅ All data endpoints (`/api/data/*`)
- ✅ All visualization endpoints (`/api/viz/*`)
- ✅ Historical data retrieval
- ✅ Time machine service

### What Needs Work:
- ❌ LLM service not tested
- ❌ Frontend not connected to backend
- ❌ Chat endpoint needs LLM service

## 🔧 Key Endpoints

### Data Endpoints:
- `GET /api/data/portfolio/10006` - Current portfolio (cached 30s)
- `GET /api/data/history/10006?days=7` - Historical data (cached forever)
- `POST /api/data/refresh/10006` - Clear cache

### Visualization Endpoints:
- `GET /api/viz/portfolio-overview/10006` - Bar chart of accounts
- `GET /api/viz/pl-trends/10006?days=7` - P&L line chart
- `GET /api/viz/risk-metrics/10006` - Risk radar chart
- `GET /api/viz/liquidity-trends/10006?days=7` - Liquidity trends

### Chat Endpoint (needs LLM):
- `POST /api/chat/query` - Natural language queries

## 🎯 Next Steps Priority

### 1. Test LLM Service (30 mins)
```python
# Quick test in backend shell
docker-compose exec backend python
>>> from services.llm_service import LLMService
>>> llm = LLMService()
>>> await llm.query("What is 2+2?", provider="openai")
```

### 2. Connect Frontend (1 hour)
- Update frontend API client to use correct endpoints
- Test portfolio display
- Test one visualization
- Implement refresh button

### 3. Implement Chat UI (1 hour)
- Create chat component
- Connect to `/api/chat/query`
- Add provider selector
- Test with sample queries

## 📝 Important Notes

1. **Accounts are pre-anonymized**: ACCOUNT_XXXXX format from API
2. **Group 10006 has 9 accounts**: Not 7 as documented
3. **Historical data is metadata**: Contains metrics, not full files
4. **Cache keys follow pattern**: `type:id:params`

## 🐛 Common Issues & Fixes

### Backend Won't Start
```bash
# Check logs
docker-compose logs backend

# Rebuild if needed
docker-compose build backend
docker-compose up -d
```

### Cache Not Working
```bash
# Check Redis
docker-compose exec redis redis-cli ping
# Should return: PONG

# Clear all cache
docker-compose exec redis redis-cli FLUSHALL
```

### gRPC Connection Failed
- Check SARNA_JWT_TOKEN hasn't expired
- Verify SARNA_API_URL format (no https://)
- Check network connectivity

## 📞 Key Files to Reference

- `/context/CRITICAL_FIXES_2025-07-03.md` - Proto fixes
- `/backend/test_*.py` - All test files for verification
- `/backend/services/` - All service implementations
- `/backend/routers/` - All API endpoints

## ✅ Definition of Done

The backend is ready when:
1. LLM service tested and working
2. Frontend displays portfolio data
3. At least one visualization works
4. Chat interface processes queries
5. Manual refresh updates data
