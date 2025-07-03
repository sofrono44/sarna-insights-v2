# Critical Fixes Applied - July 3, 2025

## 1. Environment Variable Fix
**File**: `.env`
**Change**: `SARNA_API_URL` must NOT include `https://`
- ❌ Wrong: `SARNA_API_URL=https://api.stage.sarnafinance.com:443`
- ✅ Correct: `SARNA_API_URL=api.stage.sarnafinance.com:443`
- **Note**: This is now documented in `.env.example` with clear instructions

## 2. gRPC Channel Security Fix
**File**: `backend/services/grpc_client.py`
**Change**: Now automatically uses secure/insecure channel based on `RISK_SYSTEM_USE_TLS` setting
```python
# Automatically handled based on settings.RISK_SYSTEM_USE_TLS
if self.use_tls:
    self.channel = grpc.aio.secure_channel(...)
else:
    self.channel = grpc.aio.insecure_channel(...)
```

## 3. Proto Generation Script Updates
**File**: `scripts/generate-protos.sh`
**Added**: Step 7 with additional fixes for:
- `api_hub_enums_pb2` imports in root files
- `api_hub_service_pb2*.py` imports from parent directory

## 4. Proto Files Committed to Version Control
**File**: `.gitignore`
**Change**: Added exception to commit generated proto files
```gitignore
# Exception: Include the generated proto files to prevent regeneration issues
!backend/generated/**/*.py
!backend/generated/**/*.pyi
```
This prevents loss of fixes during Docker rebuilds.

## 5. Anthropic Provider Fix
**File**: `backend/services/llm_service.py`
**Issue**: Anthropic API v0.57.1 doesn't accept `None` for system parameter
**Fix**: Only pass system parameter when it has a value
```python
kwargs = {
    "model": "claude-3-5-sonnet-20241022",
    "messages": messages,
    "max_tokens": 2000,
    "temperature": 0.7
}
# Only add system if it's provided
if system_prompt:
    kwargs["system"] = system_prompt
```

## 6. Proto Import Structure
The correct structure after generation and fixes:
```
/backend/generated/
├── *.py                    # Common protos (accounts, balances, etc.)
├── admin/
│   └── admin_*.py          # Admin-specific protos
├── api_hub/
│   └── api_hub_*.py        # API Hub protos (includes TimeMachineService)
└── time_machine/
    └── time_machine_*.py   # Time Machine message definitions
```

## 5. Testing Procedure
After any Docker rebuild or proto regeneration:
1. Run: `docker-compose run --rm proto-compiler`
2. Run: `docker-compose exec backend python scripts/fix_proto_imports.py`
3. Check backend logs: `docker-compose logs backend --tail 10`
4. Test connection: `docker-compose exec backend python test_grpc_connection.py`

## Known Issues Resolved
- Proto files in subdirectories must import from parent using `from ..`
- `api_hub_enums_pb2` is in subdirectory but needed by root files
- gRPC requires secure channel when TLS is enabled
- Account data comes pre-anonymized from API (ACCOUNT_XXXXX format)
