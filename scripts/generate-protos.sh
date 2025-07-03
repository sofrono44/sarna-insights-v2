#!/bin/bash
# Generate protobuf files with proper Python imports and directory structure

echo "Generating Python code from proto files..."

# Output directory
OUTPUT_DIR="/output"
PROTO_DIR="/protos"

# Create output directories
mkdir -p $OUTPUT_DIR
mkdir -p $OUTPUT_DIR/admin
mkdir -p $OUTPUT_DIR/api_hub
mkdir -p $OUTPUT_DIR/time_machine

# Step 1: Generate all proto files
echo "Step 1: Generating all proto files..."

# Find all proto files and generate them
find $PROTO_DIR -name "*.proto" -type f | while read proto_file; do
    echo "  Processing: $(basename $proto_file)"
    python -m grpc_tools.protoc \
        -I$PROTO_DIR \
        --python_out=$OUTPUT_DIR \
        --pyi_out=$OUTPUT_DIR \
        --grpc_python_out=$OUTPUT_DIR \
        "$proto_file" 2>/dev/null || true
done

# Step 2: Move admin files to the admin directory
echo "Step 2: Organizing admin files..."
for file in $OUTPUT_DIR/admin_*.py*; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        mv "$file" "$OUTPUT_DIR/admin/$filename"
        echo "  Moved: $filename to admin/"
    fi
done

# Also move files from admin/ proto directory if they ended up in admin/
if [ -d "$OUTPUT_DIR/admin" ]; then
    for file in $OUTPUT_DIR/admin/*.py*; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            if [[ ! "$filename" =~ ^admin_ ]]; then
                # This file came from admin/ directory but doesn't have admin_ prefix
                echo "  File $filename is already in admin/"
            fi
        fi
    done
fi

# Step 3: Move api_hub files if they were generated in root
echo "Step 3: Organizing api_hub files..."
for file in api_hub_service_pb2.py api_hub_service_pb2_grpc.py api_hub_service_pb2.pyi api_hub_pb2.py api_hub_enums_pb2.py; do
    if [ -f "$OUTPUT_DIR/$file" ]; then
        mv "$OUTPUT_DIR/$file" "$OUTPUT_DIR/api_hub/"
        echo "  Moved: $file to api_hub/"
    fi
done

# Step 4: Move time_machine files if they exist
echo "Step 4: Organizing time_machine files..."
# Move time_machine files from root to time_machine directory
for file in time_machine_pb2.py time_machine_pb2_grpc.py time_machine_pb2.pyi time_machine_enums_pb2.py time_machine_enums_pb2_grpc.py time_machine_enums_pb2.pyi; do
    if [ -f "$OUTPUT_DIR/$file" ]; then
        mv "$OUTPUT_DIR/$file" "$OUTPUT_DIR/time_machine/"
        echo "  Moved: $file to time_machine/"
    fi
done

# Step 5: Fix all imports - COMPREHENSIVE FIX
echo "Step 5: Fixing imports comprehensively..."

# List of common proto files that need to be imported from parent
COMMON_PROTOS="common|accounts|balances|positions|orders|bp|pmbp|quotes|securities_master|search|sessions|subscriptions|trading|user_data|ux_messages|order_execution_logs|account_application|account_ach|glossary|commissions|market_data_entitlement|trading_level_change"
ENUM_PROTOS="common_enums|accounts_enums|bp_enums|positions_enums|orders_enums|quotes_enums|search_enums|sessions_enums|trading_enums|user_data_enums|commissions_enums|market_data_entitlement_enums|api_hub_enums|time_machine_enums"

# Fix imports in root files
echo "  - Fixing root level imports..."
for file in $OUTPUT_DIR/*.py; do
    if [ -f "$file" ]; then
        # Change 'import X_pb2 as' to 'from . import X_pb2 as'
        sed -i 's/^import \([a-zA-Z0-9_]*_pb2\) as/from . import \1 as/g' "$file"
        # Change 'from X_pb2 import' to 'from .X_pb2 import'
        sed -i 's/^from \([a-zA-Z0-9_]*_pb2\) import/from .\1 import/g' "$file"
    fi
done

# Fix imports in admin files
echo "  - Fixing admin directory imports..."
for file in $OUTPUT_DIR/admin/*.py; do
    if [ -f "$file" ]; then
        # For files that should be imported from parent directory
        sed -i "s/^import \($COMMON_PROTOS\)_pb2 as/from .. import \1_pb2 as/g" "$file"
        sed -i "s/^import \($ENUM_PROTOS\)_pb2 as/from .. import \1_pb2 as/g" "$file"
        sed -i "s/^from \($COMMON_PROTOS\)_pb2 import/from ..\1_pb2 import/g" "$file"
        
        # For admin files importing other admin files in same directory
        sed -i 's/^import admin_\([a-zA-Z0-9_]*\) as admin/from . import admin_\1 as admin/g' "$file"
    fi
done

# Fix imports in api_hub files - THIS IS THE CRITICAL PART
echo "  - Fixing api_hub directory imports..."
for file in $OUTPUT_DIR/api_hub/*.py; do
    if [ -f "$file" ]; then
        # For ALL files that should be imported from parent directory
        sed -i "s/^import \($COMMON_PROTOS\)_pb2 as/from .. import \1_pb2 as/g" "$file"
        sed -i "s/^import \($ENUM_PROTOS\)_pb2 as/from .. import \1_pb2 as/g" "$file"
        sed -i "s/^from \($COMMON_PROTOS\)_pb2 import/from ..\1_pb2 import/g" "$file"
        
        # Special handling for time_machine imports
        sed -i 's/^import time_machine_pb2 as/from .. import time_machine_pb2 as/g' "$file"
        sed -i 's/^from time_machine_pb2 import/from ..time_machine_pb2 import/g' "$file"
        
        # Fix any remaining proto imports that don't have paths
        sed -i 's/^import \([a-zA-Z0-9_]*\)_pb2 as/from .. import \1_pb2 as/g' "$file"
    fi
done

# Fix imports in time_machine files
echo "  - Fixing time_machine directory imports..."
for file in $OUTPUT_DIR/time_machine/*.py; do
    if [ -f "$file" ]; then
        # For files that should be imported from parent directory
        sed -i "s/^import \($COMMON_PROTOS\)_pb2 as/from .. import \1_pb2 as/g" "$file"
        sed -i "s/^import \($ENUM_PROTOS\)_pb2 as/from .. import \1_pb2 as/g" "$file"
    fi
done

# Step 6: Create __init__.py files
echo "Step 6: Creating __init__.py files..."
echo "# Generated protobuf modules" > $OUTPUT_DIR/__init__.py
echo "# Admin protobuf modules" > $OUTPUT_DIR/admin/__init__.py
echo "# API Hub protobuf modules" > $OUTPUT_DIR/api_hub/__init__.py
echo "# Time Machine protobuf modules" > $OUTPUT_DIR/time_machine/__init__.py

# Step 7: Create a README documenting the structure
cat > $OUTPUT_DIR/README.md << 'EOF'
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
EOF

# Step 7: Apply additional critical fixes that were discovered
echo "Step 7: Applying additional critical fixes..."

# Fix api_hub_enums import in root files
echo "  - Fixing api_hub_enums imports in root files..."
for file in $OUTPUT_DIR/*.py; do
    if [ -f "$file" ]; then
        # Fix files that try to import api_hub_enums from current directory
        sed -i 's/from \. import api_hub_enums_pb2/from .api_hub import api_hub_enums_pb2/g' "$file"
    fi
done

# Fix api_hub service files that use relative imports incorrectly
echo "  - Fixing api_hub service file imports..."
# List of imports that api_hub service files need from parent
API_HUB_PARENT_IMPORTS="account_ach|account_application|accounts|balances|bp|commissions|glossary|market_data_entitlement|order_execution_logs|orders|positions|quotes|search|securities_master|sessions|subscriptions|time_machine|trading|trading_level_change|user_data|user|ux_messages"

for file in $OUTPUT_DIR/api_hub/api_hub_service_pb2*.py; do
    if [ -f "$file" ]; then
        # Change from . import X to from .. import X for parent imports
        sed -i "s/from \. import \($API_HUB_PARENT_IMPORTS\)_pb2/from .. import \1_pb2/g" "$file"
    fi
done

echo "  - Additional fixes complete!"

# Summary
echo ""
echo "Generation complete! Summary:"
echo "- Root files: $(ls -1 $OUTPUT_DIR/*.py 2>/dev/null | wc -l)"
echo "- Admin files: $(ls -1 $OUTPUT_DIR/admin/*.py 2>/dev/null | wc -l)"
echo "- API Hub files: $(ls -1 $OUTPUT_DIR/api_hub/*.py 2>/dev/null | wc -l)"
echo "- Time Machine files: $(ls -1 $OUTPUT_DIR/time_machine/*.py 2>/dev/null | wc -l)"

echo ""
echo "Protobuf generation complete!"
