# gRPC Integration Quick Reference

## Key Files and Locations

### 1. gRPC Client Implementation
**File**: `/backend/services/grpc_client.py`
- Main client class: `SarnaGRPCClient`
- Automatically uses secure/insecure channel based on `RISK_SYSTEM_USE_TLS` setting
- Key methods:
  - `get_current_margin_data(group_id)` - Fetches current portfolio data
  - `get_historical_data(group_id, days)` - Lists historical snapshots
  - `get_time_machine_snapshot(file_name)` - Downloads specific snapshot

### 2. Generated Protobuf Files
**Directory**: `/backend/generated/`
- `admin/` - Admin services (margin manager)
- `api_hub/` - API hub services (includes time machine)
- `time_machine/` - Time machine message definitions
- `README.md` - Detailed structure documentation
- **Note**: These files are committed to version control to preserve import fixes

### 3. Sample Response Data
**File**: `/backend/tests/fixtures/MarginManagerResponse.txt`
- Real response structure from AdminMarginManagerService/Get
- Use as reference for data parsing
- Account group 10006 has 9 accounts (not 7 as originally documented)

### 4. Test Script
**File**: `/backend/test_grpc_connection.py`
- Tests gRPC connection
- Fetches data for account group 10006
- Saves response to `test_margin_response.json`
- Accounts come pre-anonymized as `ACCOUNT_XXXXX`

### 5. Configuration
**File**: `/backend/core/config.py`
- Reads from `.env` file
- Required variables:
  - `SARNA_API_URL` (format: `api.stage.sarnafinance.com:443` - NO https://)
  - `SARNA_JWT_TOKEN`
  - `RISK_SYSTEM_USE_TLS` (true/false)

## Common Tasks

### Test the Connection
```bash
docker-compose exec backend python test_grpc_connection.py
```

### Regenerate Protobuf Files
```bash
docker-compose run --rm proto-compiler
# Then fix imports:
docker-compose exec backend python scripts/fix_proto_imports.py
```

### Check Service Logs
```bash
docker-compose logs backend --tail 20
```

### Troubleshooting Connection Issues
1. Check URL format - must not include `https://`
2. Verify TLS setting matches server requirements
3. Ensure JWT token is valid and not expired
4. Check Docker networking if IPv6 errors occur

## Data Flow

1. **Request**: Client app → FastAPI endpoint → gRPC Client → Sarna API
2. **Response**: Sarna API → gRPC Client → Data Anonymizer → FastAPI → Client app

## Important Notes

- Account IDs come pre-anonymized from API as `ACCOUNT_XXXXX`
- Historical data is cached forever (immutable)
- Current data is cached for 30 seconds
- The TimeMachineService is in api_hub_service.proto, not time_machine.proto
- Proto generation script includes Step 7 for critical import fixes
- Use secure channel when `RISK_SYSTEM_USE_TLS=true`
