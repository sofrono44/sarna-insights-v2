# Generated Protobuf Files

This directory contains the generated Python files from the Sarna proto definitions.

## Directory Structure

- `/admin/` - Admin services including AdminMarginManagerService
- `/api_hub/` - API Hub services including TimeMachineService
- `/time_machine/` - Time Machine message definitions (data structures only)
- Root directory - Common types and enums

## Key Services

1. **AdminMarginManagerService** (`admin/admin_margin_manager_service_pb2_grpc.py`)
   - Get method for fetching current margin data

2. **TimeMachineService** (`api_hub/api_hub_service_pb2_grpc.py`)
   - List and Get methods for historical data

## Import Notes

All imports have been fixed to use relative imports for proper Python module resolution.
