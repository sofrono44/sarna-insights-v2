# Quick Start Guide

## 🚀 Starting a New Session

### 1. Check Current State
```bash
# Read the current project state
cat C:\Development\sarna-insights-v2\context\PROJECT_STATE.md
```

### 2. Start Services
```bash
cd C:\Development\sarna-insights-v2
docker-compose up -d

# Verify all services are running
docker-compose ps
```

### 3. Test the Application
- Frontend: http://localhost
- Backend API: http://localhost:8000/api
- API Docs: http://localhost:8000/docs

### 4. Quick Health Check
```powershell
# Test backend API
curl http://localhost:8000/api/health/

# Test portfolio data endpoint
curl http://localhost:8000/api/data/portfolio/10006/risk-matrix

# Check position counts
$response = Invoke-WebRequest -Uri http://localhost:8000/api/data/portfolio/10006/risk-matrix -Method GET
$data = $response.Content | ConvertFrom-Json
$data.accounts | ForEach-Object { Write-Host "$($_.account_number): $($_.positions_count) positions" }
```

## 🔧 Common Tasks

### View Logs
```bash
# All services
docker-compose logs -f

# Backend only
docker-compose logs -f backend

# Search for specific patterns
docker-compose logs backend | Select-String "position"
```

### Clear Cache
```bash
docker-compose exec redis redis-cli FLUSHALL
```

### Rebuild After Code Changes
```bash
# Backend changes require rebuild
docker-compose build backend
docker-compose up -d backend
```

### Stop Everything
```bash
docker-compose down
```

## 📊 Current Status (Jan 5, 2025)
- ✅ All 33 positions loading correctly
- ✅ Expandable rows working
- ✅ UI fully functional
- ⚠️ Risk calculations using placeholder values
- ⚠️ Credit utilization showing 0%

## 🎯 Next Priority
Implement real risk calculations - see NEXT_SESSION_RISK_CALCULATIONS.md

## 💡 Tips
- Always check PROJECT_STATE.md first
- Clear Redis cache when debugging data issues
- Rebuild containers after backend changes
- Use browser DevTools to inspect API responses
- Monitor logs while testing changes