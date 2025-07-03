# Key Project Information

## Project Goal
Build an AI-powered analytics platform for portfolio risk management that:
- Provides natural language querying of portfolio data
- Protects PII by anonymizing data before sending to LLMs
- Offers real-time and historical data visualizations
- Supports multiple LLM providers with runtime switching

## Critical Requirements
1. **NEVER send PII to LLMs** - all account numbers and personal info must be stripped
2. **Performance**: Queries must respond in 2-3 seconds
3. **Data Source**: Sarna gRPC API (AdminMarginManagerService, TimeMachineService)
4. **Account Group**: ID 10006 with 9 accounts (pre-anonymized as ACCOUNT_XXXXX)
5. **Caching**: Historical data cached forever, current data for 30 seconds

## Demo Success Criteria
- Natural language queries work smoothly
- Visualizations load quickly
- Provider switching is seamless
- No PII visible in LLM interactions
- Manual refresh updates data

## Technical Stack
- **Backend**: FastAPI + Python 3.11
- **Frontend**: React + TypeScript + Vite
- **Database**: PostgreSQL + Redis
- **LLMs**: OpenAI, Anthropic, Google
- **Infrastructure**: Docker Compose
- **Protocols**: gRPC with Protocol Buffers

## Project Structure
```
/backend - FastAPI application
/frontend - React application  
/protos - Sarna protocol buffer files
/docker - Container configurations
/context - Project documentation
/docs - Technical documentation
```

## Key Files to Know
- `.env` - All configuration and secrets
- `docker-compose.yml` - Service orchestration
- `backend/services/data_anonymizer.py` - PII protection
- `backend/services/grpc_client.py` - Sarna API integration
- `backend/services/llm_service.py` - Multi-provider LLM
- `frontend/src/App.tsx` - Main React component

## Available Commands
- `make up` - Start everything
- `make down` - Stop everything
- `make logs` - View logs
- `make proto` - Generate protobuf files
- `make test` - Run tests
- `make clean` - Reset everything

## Support Contacts
- Project questions: Check /context folder first
- Technical issues: Review /docs folder
- Proto issues: See COMMON_TASKS.md

## Notes for Future Sessions
- Always check PROJECT_STATE.md first
- Run `make logs` if something isn't working
- Frontend auto-reloads, backend auto-reloads
- Redis must be running for caching to work
- All times in UTC
