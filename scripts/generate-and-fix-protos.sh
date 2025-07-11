#!/bin/bash
# Generate and fix all proto files - permanent solution

echo "Generating proto files..."
cd /protos

# Generate all proto files
python -m grpc_tools.protoc \
    -I. \
    --python_out=/output \
    --grpc_python_out=/output \
    $(find . -name "*.proto")

echo "Applying permanent fixes..."

# Fix 1: Convert absolute imports to relative imports in root files
find /output -maxdepth 1 -name "*.py" -type f -exec sed -i 's/^import \([a-zA-Z0-9_]*_pb2\) as/from . import \1 as/g' {} \;

# Fix 2: Fix imports in subdirectories to use parent imports
for dir in admin api_hub time_machine; do
    if [ -d "/output/$dir" ]; then
        find "/output/$dir" -name "*.py" -type f -exec sed -i 's/^import \(common\|accounts\|balances\|positions\|orders\|bp\|pmbp\|quotes\|securities_master\|search\|sessions\|subscriptions\|trading\|user_data\|ux_messages\|order_execution_logs\|account_application\|account_ach\|glossary\|commissions\|market_data_entitlement\|trading_level_change\|time_machine\|api_hub\|user\|pmbp_groups\|execution_api_hub\|alerts\|alerts_enums\)_pb2 as/from .. import \1_pb2 as/g' {} \;
        find "/output/$dir" -name "*.py" -type f -exec sed -i 's/^import \([a-zA-Z0-9_]*_enums\)_pb2 as/from .. import \1_pb2 as/g' {} \;
    fi
done

# Fix 3: Fix grpc imports (should never be relative)
find /output -name "*_pb2_grpc.py" -type f -exec sed -i 's/^from \. import grpc$/import grpc/g' {} \;

# Fix 4: Fix api_hub_enums imports in root files (it's in subdirectory)
find /output -maxdepth 1 -name "*.py" -type f -exec sed -i 's/from \. import api_hub_enums_pb2/from .api_hub import api_hub_enums_pb2/g' {} \;

# Fix 5: Don't modify google imports
find /output -name "*.py" -type f -exec sed -i 's/from \. import google\./import google./g' {} \;
find /output -name "*.py" -type f -exec sed -i 's/from \.\+ import google\./import google./g' {} \;

echo "Proto generation and fixes complete!"
echo "IMPORTANT: These files should be committed to git to make fixes permanent."
