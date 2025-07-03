#!/usr/bin/env python3
"""Fix all import statements in generated protobuf files."""
import os
import re
from pathlib import Path

def fix_imports_in_file(filepath):
    """Fix imports in a single file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern to match import statements
    import_pattern = r'^import ([a-zA-Z0-9_]+_pb2) as'
    from_pattern = r'^from ([a-zA-Z0-9_]+_pb2) import'
    
    # Determine the directory of the file
    file_dir = os.path.dirname(filepath)
    file_name = os.path.basename(filepath)
    
    # Files that should use parent imports (from ..)
    parent_imports = [
        'common', 'accounts', 'balances', 'positions', 'orders', 'bp', 'pmbp',
        'quotes', 'securities_master', 'search', 'sessions', 'subscriptions',
        'trading', 'user_data', 'ux_messages', 'order_execution_logs',
        'account_application', 'account_ach', 'glossary', 'commissions',
        'market_data_entitlement', 'trading_level_change', 'time_machine',
        'api_hub', 'user', 'pmbp_groups', 'execution_api_hub',
        # Enums
        'common_enums', 'accounts_enums', 'bp_enums', 'positions_enums',
        'orders_enums', 'quotes_enums', 'search_enums', 'sessions_enums',
        'trading_enums', 'user_data_enums', 'commissions_enums',
        'market_data_entitlement_enums', 'api_hub_enums', 'time_machine_enums',
        'account_application_enums', 'account_ach_enums', 'glossary_enums',
        'trading_level_change_enums', 'dividends_enums', 'notifications_enums',
        'execution_api_hub_enums', 'common_bp_enums', 'options_en_a_enums',
        'bh_accounts_enums', 'account_cash_transactions_enums',
        'account_ach_sdr_enums', 'account_maintenance_fee_enums',
        'execution_acceptor_enums', 'pmbp_enums'
    ]
    
    # Check if file is in a subdirectory
    if 'admin' in file_dir or 'api_hub' in file_dir or 'time_machine' in file_dir:
        # Fix imports to use parent directory
        for proto in parent_imports:
            # Fix import X_pb2 as
            content = re.sub(
                f'^import {proto}_pb2 as',
                f'from .. import {proto}_pb2 as',
                content,
                flags=re.MULTILINE
            )
            # Fix from X_pb2 import
            content = re.sub(
                f'^from {proto}_pb2 import',
                f'from ..{proto}_pb2 import',
                content,
                flags=re.MULTILINE
            )
        
        # For admin files importing other admin files
        if 'admin' in file_dir:
            content = re.sub(
                r'^import (admin_[a-zA-Z0-9_]*) as admin',
                r'from . import \1 as admin',
                content,
                flags=re.MULTILINE
            )
            # Fix service files importing from admin directory
            content = re.sub(
                r'^from admin import (admin_[a-zA-Z0-9_]*) as',
                r'from . import \1 as',
                content,
                flags=re.MULTILINE
            )
    else:
        # Root directory files - use relative imports
        content = re.sub(
            r'^import ([a-zA-Z0-9_]*_pb2) as',
            r'from . import \1 as',
            content,
            flags=re.MULTILINE
        )
        content = re.sub(
            r'^from ([a-zA-Z0-9_]*_pb2) import',
            r'from .\1 import',
            content,
            flags=re.MULTILINE
        )
    
    # Don't modify google imports
    content = re.sub(
        r'from \. import (google\.[a-zA-Z0-9_.]*) as',
        r'import \1 as',
        content,
        flags=re.MULTILINE
    )
    content = re.sub(
        r'from \.+ import (google\.[a-zA-Z0-9_.]*) as',
        r'import \1 as',
        content,
        flags=re.MULTILINE
    )
    
    # Write back if changed
    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed imports in: {filepath}")
        return True
    return False

def main():
    """Fix all imports in generated directory."""
    generated_dir = Path('/app/generated')
    
    if not generated_dir.exists():
        print(f"Error: {generated_dir} does not exist!")
        return
    
    fixed_count = 0
    
    # Process all Python files
    for py_file in generated_dir.rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue
        if py_file.name == '__init__.py':
            continue
            
        if fix_imports_in_file(py_file):
            fixed_count += 1
    
    print(f"\nFixed imports in {fixed_count} files.")

if __name__ == '__main__':
    main()
