# Quick Start Guide

## Prerequisites Check
- [ ] Docker Desktop running
- [ ] .env file has all required values
- [ ] Proto files are in /protos folder

## Start Development

### 1. First Time Setup
```bash
cd C:\Development\sarna-insights-v2

# Generate protobuf files
docker-compose run --rm proto-compiler

# Start all services
docker-compose up -d

# Check logs
docker-compose logs -f backend
```

### 2. Verify Services
- Frontend: http://localhost
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### 3. Common Issues & Solutions

**Proto generation fails**
- Check Docker is running
- Run `docker-compose build proto-compiler` if image is missing
- Ensure proto files have correct syntax

**Import errors in backend**
```bash
# Run the import fix script
docker-compose exec backend python scripts/fix_proto_imports.py
```

**Database connection errors**
- The system automatically converts postgresql:// to postgresql+asyncpg://
- If issues persist, check DATABASE_URL in .env

**Can't connect to Sarna API**
- Verify SARNA_API_URL in .env
- Check SARNA_JWT_TOKEN is valid
- Ensure network connectivity

**Frontend not loading**
- Check browser console for errors
- Verify CORS settings include your domain
- Check API is running on port 8000

## Development Workflow

### Backend Changes
1. Edit files in /backend
2. Changes auto-reload (watch logs)
3. Test via API docs

### Frontend Changes
1. Edit files in /frontend/src
2. Changes auto-reload
3. Check browser

### Adding New Features
1. Create API endpoint in /backend/routers
2. Add service logic in /backend/services
3. Create UI component in /frontend/src/components
4. Update types in /frontend/src/types

## Testing

### Quick API Test
```bash
# From outside Docker
curl http://localhost:8000/api/health

# Or using PowerShell
Invoke-WebRequest -Uri http://localhost:8000/api/health -Method GET
```

### Test Chat Endpoint (once implemented)
```bash
curl -X POST http://localhost:8000/api/chat/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is my total portfolio value?", "provider": "openai"}'
```

## Makefile Commands
- `make up` - Start all services
- `make down` - Stop all services
- `make logs` - View logs
- `make proto` - Generate protobuf files
- `make test` - Run tests
- `make clean` - Reset everything