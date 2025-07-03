# Common Tasks & Solutions

## Protobuf Related

### After Adding New Proto Files
```bash
# Regenerate Python files
make proto

# Or manually for specific files:
docker run --rm -v C:\Development\sarna-insights-v2\protos:/protos -v C:\Development\sarna-insights-v2\backend\generated:/output python:3.11-slim bash -c "apt-get update -qq && apt-get install -y -qq protobuf-compiler > /dev/null && pip install -q grpcio-tools==1.60.0 && cd /protos && python -m grpc_tools.protoc -I. --python_out=/output --grpc_python_out=/output [PROTO_FILE]"

# Fix imports if needed
find backend/generated -name "*.py" -exec sed -i 's/^import /from . import /g' {} \;
```

### Important Proto Notes
- **TimeMachineService is in api_hub_service.proto**, not time_machine.proto!
- Services and messages can be in different files
- Always check for service definitions in "api" or "hub" proto files

### Common Proto Errors
- **"Module not found"**: Check generated files exist in backend/generated/
- **"Import error"**: Proto might have circular dependencies, check imports
- **"Field not accessible"**: Use string representation fallback

## gRPC Connection

### Test Connection
```bash
# Use the test script
cd backend
python test_grpc_connection.py
```

### Quick Connection Test
```python
# Quick test script
import grpc
from backend.core.config import settings

channel = grpc.insecure_channel(settings.SARNA_API_URL)
try:
    grpc.channel_ready_future(channel).result(timeout=10)
    print("Connected!")
except grpc.FutureTimeoutError:
    print("Connection failed")
```

### Auth Issues
- Check JWT token hasn't expired
- Verify token format: "Bearer {token}" in metadata
- Check SARNA_API_URL includes port if needed

## Database Operations

### Create New Migration
```bash
docker-compose exec backend alembic revision -m "description"
docker-compose exec backend alembic upgrade head
```

### Reset Database
```bash
docker-compose down -v
docker-compose up -d postgres
docker-compose exec backend alembic upgrade head
```

## Frontend Development

### Add New Component
1. Create component file in appropriate folder
2. Export from index if creating folder
3. Import in parent component
4. Add to router if new page

### Common React Patterns
```typescript
// Query with error handling
const { data, error, isLoading } = useQuery({
  queryKey: ['portfolio', groupId],
  queryFn: () => api.getPortfolio(groupId),
  retry: 1,
  onError: (error) => {
    toast.error('Failed to load portfolio');
  }
});

// Mutation with optimistic update
const mutation = useMutation({
  mutationFn: api.refreshData,
  onMutate: async () => {
    // Optimistic update
    queryClient.setQueryData(['portfolio'], null);
  },
  onSuccess: () => {
    queryClient.invalidateQueries(['portfolio']);
  }
});
```

## Debugging

### Backend Debugging
```python
# Add to any endpoint
import logging
logger = logging.getLogger(__name__)

# In your function
logger.info(f"Received request: {request}")
logger.error(f"Error occurred: {str(e)}")

# Check logs
make logs
```

### Frontend Debugging
```typescript
// Add to any component
console.log('Component rendered with props:', props);

// Network debugging
window.DEBUG_API = true; // Enable in console

// React Query devtools
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
// Add <ReactQueryDevtools /> to App.tsx
```

### Docker Issues
```bash
# Rebuild everything
docker-compose down
docker-compose build --no-cache
docker-compose up

# Check container status
docker-compose ps

# Enter container
docker-compose exec backend bash
docker-compose exec frontend sh

# View specific service logs
docker-compose logs -f backend
docker-compose logs -f frontend
```

## Performance Optimization

### Slow Queries
1. Check Redis is working: `docker-compose exec redis redis-cli ping`
2. Verify cache keys are being set
3. Check gRPC call timing in logs
4. Consider implementing pagination

### Memory Issues
1. Check Docker memory allocation
2. Reduce Redis max memory if needed
3. Implement streaming for large datasets

## Environment Variables

### Adding New Variable
1. Add to `.env`
2. Add to `.env.example` with placeholder
3. Add to `backend/core/config.py`
4. Add to `docker-compose.yml` if needed
5. Restart services

### Secret Rotation
1. Update in `.env`
2. Restart only affected service:
   ```bash
   docker-compose restart backend
   ```
