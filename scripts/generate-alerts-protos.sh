#!/bin/bash
# Generate alert proto files

cd /protos

# Generate alert proto files
python -m grpc_tools.protoc \
    -I. \
    --python_out=/output \
    --grpc_python_out=/output \
    alerts.proto alerts_enums.proto alerts_service.proto

# Fix imports for the new files
sed -i 's/^import \(common\|search\|alerts_enums\)_pb2 as/from . import \1_pb2 as/g' /output/alerts*.py

echo "Alert proto generation complete!"
