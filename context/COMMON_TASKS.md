# Common Tasks

This document provides quick solutions to common development tasks for the Sarna Insights v2 project.

## Starting the Application

```bash
# Start all services
docker-compose up -d

# Start with logs
docker-compose up

# Start specific service
docker-compose up backend frontend
```

## Viewing Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend

# Last N lines
docker-compose logs --tail 50 backend
```

## Testing the Application

### Quick Health Check
```bash
# Test backend
curl http://localhost:8000/api/health/

# Test frontend
curl http://localhost
```

### Test API Endpoints
```python
# Run the test script
python test_frontend_api.py
```

### Manual Testing
1. Open http://localhost in browser
2. Try these queries in the chat:
   - "What is my total margin?"
   - "Show me my buying power"
   - "Which accounts have high utilization?"
   - "How many accounts do I have?"

## Restarting Services

```bash
# Restart all
docker-compose restart

# Restart specific service
docker-compose restart backend
docker-compose restart frontend

# Full rebuild
docker-compose down
docker-compose up -d --build
```

## Debugging Issues

### Frontend Not Loading
```bash
# Check logs
docker-compose logs frontend

# Restart frontend
docker-compose restart frontend

# Check if running
docker-compose ps
```

### Backend API Errors
```bash
# Check logs
docker-compose logs backend --tail 100

# Test specific endpoint
curl http://localhost:8000/api/health/

# Check Redis
docker-compose exec redis redis-cli ping
```

### Database Issues
```bash
# Connect to database
docker-compose exec postgres psql -U sarnauser -d sarnadb

# Check tables
\dt

# Exit
\q
```

## Updating Code

### Frontend Changes
- Files in `frontend/src` auto-reload
- No restart needed
- Check browser console for errors

### Backend Changes
- Files in `backend/` auto-reload
- No restart needed
- Check logs for import errors

### Proto Changes (RARE - Only if .proto files change)
```bash
# DO NOT regenerate unless .proto files changed!
# Current proto files are fixed and committed
make proto
```

## Common Fixes

### Clear Cache
```bash
# Clear Redis cache
docker-compose exec redis redis-cli FLUSHALL

# Restart backend to reload
docker-compose restart backend
```

### Reset Database
```bash
# Full reset (WARNING: Deletes all data)
docker-compose down -v
docker-compose up -d
```

### Fix Permission Issues
```bash
# If files can't be written
sudo chown -R $USER:$USER .
```

## Performance Testing

### Monitor Resource Usage
```bash
# Check container stats
docker stats

# Check specific container
docker stats sarna-insights-v2-backend-1
```

### Test Query Performance
```bash
# Time a request
time curl http://localhost:8000/api/data/portfolio/10006
```

## Deployment Preparation

### Build for Production
```bash
# Frontend
cd frontend
npm run build

# Backend
cd backend
pip install -r requirements.txt
```

### Environment Variables
- Copy `.env.example` to `.env`
- Update all API keys
- Set `RISK_SYSTEM_USE_TLS=true` for production
- Update `SARNA_API_URL` without https://

## Troubleshooting Checklist

1. ✓ Are all containers running? (`docker-compose ps`)
2. ✓ Are there any errors in logs? (`docker-compose logs`)
3. ✓ Is Redis working? (`docker-compose exec redis redis-cli ping`)
4. ✓ Is the database accessible? (`docker-compose exec postgres pg_isready`)
5. ✓ Are API endpoints responding? (`curl http://localhost:8000/api/health/`)
6. ✓ Is the frontend building? (Check frontend logs)
7. ✓ Are environment variables set? (Check .env file)

## Quick Links

- Frontend: http://localhost
- Backend API: http://localhost:8000/api
- API Docs: http://localhost:8000/docs
- Project State: /context/PROJECT_STATE.md
- Session Notes: /context/SESSION_SUMMARY_*.md
