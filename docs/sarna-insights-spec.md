# Sarna Insights v2.0 - Complete Project Specification

## Project Overview
AI-powered analytics platform that provides natural language querying and intelligent visualizations for portfolio risk data via Sarna's gRPC API.

## Core Architecture Principles

### 1. **Security First**
- **Zero PII to LLMs**: All account numbers, names, and identifying info stripped before LLM processing
- **JWT auth** for Sarna API stored securely
- **Data anonymization layer** between gRPC responses and AI services

### 2. **Performance Optimized**
- **Aggressive caching** for historical data (immutable)
- **Redis** for hot data and session state
- **Bulk API calls** to minimize gRPC overhead
- **PostgreSQL** for query history and user preferences

### 3. **Developer Experience**
- **Docker Compose** for one-command startup
- **Hot reload** for frontend and backend
- **Automatic protobuf compilation**
- **Clear separation of concerns**

## Project Directory Structure

```
sarna-insights-v2/
├── .github/
│   └── workflows/
│       ├── ci.yml                 # Continuous Integration
│       └── deploy.yml             # Deployment pipeline
├── docker/
│   ├── backend/
│   │   └── Dockerfile
│   ├── frontend/
│   │   └── Dockerfile
│   └── nginx/
│       ├── Dockerfile
│       └── nginx.conf
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py               # FastAPI app entry
│   │   ├── dependencies.py       # Shared dependencies
│   │   └── middleware.py         # CORS, auth, logging
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── chat.py              # NLP endpoints
│   │   ├── data.py              # Data fetch endpoints
│   │   ├── health.py            # Health checks
│   │   └── visualizations.py    # Chart data endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── grpc_client.py       # Sarna gRPC client
│   │   ├── data_anonymizer.py   # PII stripping service
│   │   ├── llm_service.py       # Multi-provider LLM
│   │   ├── cache_service.py     # Redis caching
│   │   └── time_machine.py      # Historical data service
│   ├── models/
│   │   ├── __init__.py
│   │   ├── domain.py            # Business models
│   │   ├── requests.py          # API request models
│   │   └── responses.py         # API response models
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py            # Settings management
│   │   ├── security.py          # Auth helpers
│   │   └── logging.py           # Structured logging
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py              # SQLAlchemy base
│   │   ├── models.py            # DB models
│   │   └── session.py           # DB session management
│   ├── tests/
│   │   ├── integration/
│   │   └── e2e/
│   ├── alembic/                  # DB migrations
│   ├── requirements.txt
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── chat/
│   │   │   │   ├── ChatInterface.tsx
│   │   │   │   ├── MessageList.tsx
│   │   │   │   └── QueryInput.tsx
│   │   │   ├── visualizations/
│   │   │   │   ├── PortfolioOverview.tsx
│   │   │   │   ├── PLTrends.tsx
│   │   │   │   ├── RiskMetrics.tsx
│   │   │   │   └── CustomViz.tsx
│   │   │   ├── common/
│   │   │   │   ├── RefreshButton.tsx
│   │   │   │   ├── LLMSelector.tsx
│   │   │   │   └── LoadingStates.tsx
│   │   │   └── layout/
│   │   │       ├── Header.tsx
│   │   │       ├── Sidebar.tsx
│   │   │       └── Layout.tsx
│   │   ├── hooks/
│   │   │   ├── useWebSocket.ts
│   │   │   ├── useQuery.ts
│   │   │   └── useCache.ts
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── dataTransform.ts
│   │   │   └── chartConfig.ts
│   │   ├── store/
│   │   │   ├── index.ts         # Zustand store
│   │   │   └── slices/
│   │   ├── types/
│   │   │   └── index.ts
│   │   ├── utils/
│   │   │   └── index.ts
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── protos/                       # Your Sarna proto files go here
│   ├── admin/
│   │   └── margin_manager.proto
│   ├── time_machine/
│   │   └── time_machine.proto
│   └── compile.sh               # Proto compilation script
├── scripts/
│   ├── setup.sh                 # First-time setup
│   ├── generate-protos.sh       # Protobuf generation
│   └── seed-db.sh              # Database seeding
├── docs/
│   ├── API.md
│   ├── DEPLOYMENT.md
│   └── DEVELOPMENT.md
├── docker-compose.yml           # Full stack
├── docker-compose.dev.yml      # Dev overrides
├── .env.example
├── .gitignore
├── Makefile                    # Common commands
└── README.md
```

## Docker Compose Configuration

```yaml
# docker-compose.yml
version: '3.9'

services:
  backend:
    build:
      context: .
      dockerfile: docker/backend/Dockerfile
    volumes:
      - ./backend:/app
      - ./protos:/protos
    environment:
      - SARNA_API_URL=${SARNA_API_URL}
      - SARNA_JWT_TOKEN=${SARNA_JWT_TOKEN}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - DATABASE_URL=postgresql://sarna:sarna@postgres:5432/sarna
      - REDIS_URL=redis://redis:6379
      - PINECONE_API_KEY=${PINECONE_API_KEY}
      - PINECONE_ENVIRONMENT=${PINECONE_ENVIRONMENT}
    depends_on:
      - postgres
      - redis
    command: uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    build:
      context: .
      dockerfile: docker/frontend/Dockerfile
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - VITE_API_URL=http://localhost:8000
    command: npm run dev

  nginx:
    build:
      context: .
      dockerfile: docker/nginx/Dockerfile
    ports:
      - "80:80"
      - "8000:8000"
    depends_on:
      - backend
      - frontend

  postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=sarna
      - POSTGRES_PASSWORD=sarna
      - POSTGRES_DB=sarna
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

  proto-compiler:
    build:
      context: .
      dockerfile: docker/proto/Dockerfile
    volumes:
      - ./protos:/protos
      - ./backend/generated:/output
    command: /protos/compile.sh

volumes:
  postgres_data:
  redis_data:
```

## Key Implementation Details

### 1. **Data Anonymization Service**
```python
# backend/services/data_anonymizer.py
class DataAnonymizer:
    """Strips all PII before sending to LLMs"""
    
    def anonymize_account(self, account_data: dict) -> dict:
        """Replace account numbers with generic IDs"""
        # TS4-DU12345 -> ACCOUNT_1
        # Personal names -> removed
        # Keep only numerical metrics
        
    def create_context_mapping(self, data: dict) -> dict:
        """Create reversible mapping for response reconstruction"""
```

### 2. **Multi-Provider LLM Service**
```python
# backend/services/llm_service.py
class LLMService:
    """Abstracted interface for multiple LLM providers"""
    
    def __init__(self):
        self.providers = {
            'openai': OpenAIProvider(),
            'anthropic': AnthropicProvider(),
            'google': GoogleProvider()
        }
    
    async def query(self, prompt: str, provider: str = 'openai'):
        """Route to selected provider"""
```

### 3. **Efficient Data Fetching**
```python
# backend/services/grpc_client.py
class SarnaGRPCClient:
    """Optimized gRPC client with caching"""
    
    async def get_current_data(self, group_id: int):
        """Fetch from AdminMarginManagerService"""
        # Single bulk call for all accounts
        
    async def get_historical_data(self, group_id: int, days: int = 30):
        """Fetch from TimeMachineService with aggressive caching"""
        # Check Redis first
        # If miss, fetch and cache (immutable data)
```

### 4. **Frontend State Management**
```typescript
// frontend/src/store/index.ts
interface AppState {
  selectedLLM: 'openai' | 'anthropic' | 'google'
  portfolioData: PortfolioData | null
  historicalData: TimeSeriesData | null
  isLoading: boolean
  lastRefresh: Date | null
}
```

## Development Workflow

### Initial Setup
```bash
# 1. Clone and setup
git clone <repo>
cd sarna-insights-v2
cp .env.example .env
# Add your credentials to .env

# 2. Copy proto files
cp -r /path/to/sarna/protos/* ./protos/

# 3. Start everything
make up

# 4. View logs
make logs

# 5. Access application
# Frontend: http://localhost
# API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Common Commands (Makefile)
```makefile
.PHONY: up down logs proto test

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

proto:
	docker-compose run proto-compiler

test-integration:
	docker-compose run backend pytest tests/integration

test-e2e:
	docker-compose run e2e-tests

clean:
	docker-compose down -v
	rm -rf backend/generated/*
```

## CI/CD Pipeline

### GitHub Actions
```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          docker-compose -f docker-compose.test.yml up --abort-on-container-exit

  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build images
        run: |
          docker-compose build
```

## Security Considerations

1. **Environment Variables**: Never commit .env file
2. **PII Protection**: Audit all LLM calls for data leakage
3. **API Security**: Rate limiting, request validation
4. **CORS**: Restrict to specific origins in production

## Performance Optimizations

1. **Redis Caching Strategy**:
   - Historical data: Cache forever (immutable)
   - Current data: 30-second TTL
   - LLM responses: 5-minute TTL

2. **Database Indexes**:
   - Query history by timestamp
   - User preferences by ID

3. **Frontend Optimization**:
   - React Query for request deduplication
   - Virtualized lists for large datasets
   - Lazy loading for visualizations

## Monitoring & Observability

1. **Structured Logging**: JSON logs with correlation IDs
2. **Metrics**: Prometheus-compatible endpoints
3. **Error Tracking**: Sentry integration
4. **Health Checks**: Comprehensive health endpoints

## Next Steps After Setup

1. **Verify Proto Compilation**: Ensure generated Python files are correct
2. **Test gRPC Connection**: Verify JWT auth works
3. **Implement Core Features**: Start with basic data fetch
4. **Add Visualizations**: One at a time, test thoroughly
5. **Integrate LLMs**: Start with OpenAI, add others
6. **Performance Testing**: Ensure 2-3 second response times

This architecture is designed for rapid development while maintaining production quality. The Docker-first approach ensures consistency across environments, and the modular structure allows for easy feature additions.