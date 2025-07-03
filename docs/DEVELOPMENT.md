# Development Guide

## Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local frontend development)
- Python 3.11+ (for local backend development)

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd sarna-insights-v2
   ```

2. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

3. **Copy proto files**
   ```bash
   # Copy your Sarna proto files to ./protos/
   ```

4. **Start services**
   ```bash
   make up
   ```

## Development Workflow

### Backend Development

1. **Make changes** to backend code
2. **Hot reload** automatically applies changes
3. **Run tests** with `make test`

### Frontend Development

1. **Make changes** to frontend code
2. **Hot reload** automatically applies changes
3. **Check browser** at http://localhost

### Adding New Features

1. **Backend endpoint**: Add router in `backend/routers/`
2. **Frontend component**: Add in `frontend/src/components/`
3. **Update API docs** in `docs/API.md`

## Common Tasks

### Regenerate Protobuf Files
```bash
make proto
```

### View Logs
```bash
make logs
```

### Clean Everything
```bash
make clean
```

## Code Style

- Backend: Black + isort
- Frontend: ESLint + Prettier
- Commit messages: Conventional Commits

## Testing

### Backend Tests
```bash
docker-compose run backend pytest tests/
```

### Frontend Tests
```bash
cd frontend && npm test
```

## Debugging

### Backend
- Add `import pdb; pdb.set_trace()` for breakpoints
- Check logs with `docker-compose logs backend`

### Frontend
- Use browser DevTools
- React Developer Tools extension
