# Sarna Insights v2

AI-powered analytics platform for portfolio risk management with natural language querying capabilities.

## Quick Start

1. **Prerequisites**
   - Docker and Docker Compose
   - Copy `.env.example` to `.env` and update with your credentials
     - **Important**: `SARNA_API_URL` should NOT include `https://` prefix
     - Example: `api.stage.sarnafinance.com:443`
   - Sarna proto files should be in `./protos/` directory

2. **Start the application**
   ```bash
   make up
   ```

3. **Access the application**
   - Frontend: http://localhost
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Available Commands

- `make up` - Start all services
- `make down` - Stop all services
- `make logs` - View logs
- `make proto` - Compile protobuf files
- `make test` - Run all tests
- `make clean` - Remove all data and generated files

## Architecture

- **Backend**: FastAPI with secure gRPC client for Sarna API
- **Frontend**: React + TypeScript with Vite
- **Database**: PostgreSQL for app data, Redis for caching
- **AI**: Multi-provider LLM support (OpenAI, Anthropic, Google)
- **Security**: TLS-enabled gRPC connections, PII anonymization

## Key Features

- Natural language portfolio queries
- Real-time and historical data visualization
- PII protection for all LLM interactions (data anonymized before processing)
- Multi-provider LLM support with runtime switching
- Aggressive caching for optimal performance
- Support for 9 accounts under group 10006

## Project Structure

```
/backend       - FastAPI backend with gRPC integration
  /generated   - Pre-generated and fixed proto files (committed to git)
  /services    - Business logic and integrations
  /routers     - API endpoints
/frontend      - React TypeScript frontend
/protos        - Protocol buffer definitions
/scripts       - Build and utility scripts
/context       - Project documentation and state tracking
/docs          - Technical documentation
```

## Development Setup

1. **Verify Backend is Running**
   ```bash
   docker-compose logs backend
   ```
   Look for "Application startup complete"

2. **Test gRPC Connection**
   ```bash
   docker-compose exec backend python test_grpc_connection.py
   ```

3. **Development Features**
   - Backend auto-reloads on code changes
   - Frontend uses Vite for fast HMR
   - Proto files are pre-generated and committed to version control
   - TLS/non-TLS support based on `RISK_SYSTEM_USE_TLS` setting

## Troubleshooting

- **Proto import errors**: 
  1. Run: `docker-compose run --rm proto-compiler`
  2. Run: `docker-compose exec backend python scripts/fix_proto_imports.py`
  3. Restart backend: `docker-compose restart backend`

- **gRPC connection errors**:
  - Ensure `SARNA_API_URL` in `.env` does NOT include `https://`
  - Check that `RISK_SYSTEM_USE_TLS=true` for secure connections
  - Verify JWT token is valid and not expired

- **Database connection errors**: 
  - DATABASE_URL is automatically converted to async format
  - Use `postgresql://` in .env (converted to `postgresql+asyncpg://` internally)

For detailed fixes and explanations, see `/context/CRITICAL_FIXES_2025-07-03.md`

## Documentation

- `/context/PROJECT_INFO.md` - Project overview and requirements
- `/context/TECHNICAL_DETAILS.md` - Architecture and implementation details
- `/context/PROJECT_STATE.md` - Current development status
- `/context/ROADMAP.md` - Development roadmap and priorities
- `/backend/GRPC_INTEGRATION.md` - gRPC integration guide
