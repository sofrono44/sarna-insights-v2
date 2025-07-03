# Technical Implementation Details

## gRPC Integration

### Services We're Using
1. **AdminMarginManagerService/Get**
   - Location: `admin/admin_margin_manager_service_pb2_grpc.py`
   - Returns current margin data for all accounts
   - Single bulk call for efficiency
   - Contains: margin, buying power, excess liquidity, positions

2. **TimeMachineService/List and Get**
   - Location: `api_hub/api_hub_service_pb2_grpc.py` (NOT in time_machine!)
   - List: Browse available historical snapshots
   - Get: Download specific snapshot details
   - Data is immutable - cache forever

### Proto File Structure
```
protos/
├── admin/
│   ├── admin_margin_manager.proto
│   ├── admin_margin_manager_service.proto
│   └── [other admin protos]
├── api_hub_service.proto (contains TimeMachineService!)
└── time_machine.proto (only message definitions)
```

### Generated File Organization
```
backend/generated/
├── admin/                    # Admin services
├── api_hub/                  # API Hub services (includes TimeMachine)
└── time_machine/             # Time Machine message definitions
```

## Data Flow Architecture

```
User Query → Chat Endpoint → Data Anonymizer → LLM Service → Response
                ↓
         gRPC Client → Sarna API (TLS)
                ↓
           Redis Cache
```

## gRPC Connection Details

- **URL Format**: `api.stage.sarnafinance.com:443` (no https://)
- **Security**: TLS-enabled by default (configurable via RISK_SYSTEM_USE_TLS)
- **Authentication**: Bearer token in gRPC metadata
- **Account Group**: 10006 with 9 accounts
- **Pre-anonymized**: Account IDs come as ACCOUNT_XXXXX from API

## PII Protection Strategy

### What Gets Anonymized
- Account numbers (e.g., TS4-DU12345 → ACCOUNT_1)
- Any personal names
- Email addresses
- Phone numbers
- Tax IDs

### What Stays
- Numerical values (margin, P&L, etc.)
- Percentages
- Timestamps
- Risk metrics

### Anonymization Process
1. Create mapping table (original → anonymous)
2. Strip PII from data
3. Send to LLM
4. Restore original IDs in response

## Caching Strategy

### Historical Data (TimeMachine)
- **TTL**: None (cache forever)
- **Key**: `history:{group_id}:{days}`
- **Reason**: Data is immutable

### Current Data (Margin)
- **TTL**: 30 seconds
- **Key**: `portfolio:{group_id}`
- **Reason**: Changes frequently

### LLM Responses
- **TTL**: 5 minutes
- **Key**: `chat:{question_hash}:{provider}`
- **Reason**: Expensive to regenerate

## LLM Integration

### Providers Configuration
```python
# OpenAI (default)
Model: gpt-4-turbo-preview
Max Tokens: 2000
Temperature: 0.7

# Anthropic
Model: claude-3-opus-20240229
Max Tokens: 2000

# Google
Model: gemini-pro
Max Tokens: 2000
```

### System Prompt
"You are a financial analyst assistant helping users understand their portfolio data. You have access to anonymized portfolio information including margin requirements, positions, and balances. Always provide clear, actionable insights based on the data provided. Never mention account numbers or personal information in your responses."

## Frontend State Management

### Zustand Store Structure
```typescript
interface AppState {
  // LLM Selection
  selectedLLM: 'openai' | 'anthropic' | 'google'
  
  // Portfolio Data
  portfolioData: PortfolioData | null
  historicalData: HistoricalData | null
  
  // UI State
  isLoading: boolean
  lastRefresh: Date | null
  
  // Actions
  fetchPortfolio: () => Promise<void>
  refreshData: () => Promise<void>
  setLLMProvider: (provider: string) => void
}
```

## API Response Formats

### Portfolio Data
```json
{
  "group_id": 10006,
  "accounts": [
    {
      "account_id": "ACCOUNT_1",
      "margin": 50000.00,
      "buying_power": 150000.00,
      "excess_liquidity": 100000.00,
      "margin_utilization": 0.33
    }
  ],
  "timestamp": "2025-06-30T20:00:00Z",
  "total_margin": 350000.00
}
```

### Chat Response
```json
{
  "question": "What is my total portfolio value?",
  "answer": "Your total portfolio margin requirement is $350,000...",
  "provider": "openai",
  "timestamp": "2025-06-30T20:00:00Z"
}
```

## Spec Alignment Notes

### Current Implementation vs Spec
1. **Aligned (90%)**:
   - Core architecture matches spec
   - gRPC client implemented correctly
   - PII anonymization in place (needs refactoring)
   - Directory structure matches exactly

2. **Needs Refactoring**:
   - Move anonymization from grpc_client.py to data_anonymizer.py
   - Create separate cache_service.py for Redis
   - Create time_machine.py service wrapper
   - Implement API routers as specified

3. **Adaptations Made**:
   - TimeMachineService found in api_hub_service.proto (documented)
   - Added /generated/api_hub/ for better organization
   - Created test infrastructure not in original spec

### Service Layer Architecture (To Implement)
```
routers/          (FastAPI endpoints)
    ↓
services/         (Business logic)
    ↓
grpc_client.py    (Sarna API integration)
```

This separation ensures clean architecture and testability.

## Docker Setup Notes

### Database Connection
- Use `postgresql+asyncpg://` for async SQLAlchemy connections
- The db/session.py automatically converts `postgresql://` to `postgresql+asyncpg://`

### Proto Generation
- Run `docker-compose run --rm proto-compiler` to generate proto files
- Generated files are organized into:
  - `/backend/generated/admin/` - Admin services
  - `/backend/generated/api_hub/` - API Hub services (includes TimeMachineService)
  - `/backend/generated/time_machine/` - Time Machine message definitions
- Import paths are automatically fixed by the generation script (includes Step 7 fixes)
- **Generated files are committed to version control to preserve fixes**

### Requirements
- Use full `requirements.txt` (not requirements-minimal.txt) for complete functionality
- Includes all LLM provider libraries (openai, anthropic, google-generativeai)

### Common Issues & Solutions
1. **Import errors in generated proto files**: Run `python scripts/fix_proto_imports.py` inside the backend container
2. **psycopg2 module not found**: Ensure DATABASE_URL uses `postgresql+asyncpg://` prefix
3. **Proto files in wrong directories**: The generation script automatically organizes files into the correct subdirectories
4. **gRPC connection errors**: 
   - Ensure `SARNA_API_URL` does NOT include `https://` prefix
   - Verify `RISK_SYSTEM_USE_TLS=true` for production environments
   - Check JWT token validity
5. **Account data**: Group 10006 has 9 accounts (not 7), already anonymized as ACCOUNT_XXXXX
