"""Simple test script to verify gRPC connection without imports."""
import os
import sys
import grpc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get configuration
api_url = os.getenv('SARNA_API_URL', os.getenv('RISK_SYSTEM_HOST'))
if not api_url:
    print("ERROR: No API URL found in environment variables")
    sys.exit(1)

token = os.getenv('SARNA_JWT_TOKEN', os.getenv('RISK_API_KEY'))
if not token:
    print("ERROR: No JWT token found in environment variables")
    sys.exit(1)

print(f"API URL: {api_url}")
print(f"Token length: {len(token)}")

# Parse URL to get host and port
if api_url.startswith('https://'):
    host = api_url[8:]
    use_ssl = True
elif api_url.startswith('http://'):
    host = api_url[7:]
    use_ssl = False
else:
    host = api_url
    use_ssl = True

# Handle port
if ':' in host:
    host, port = host.split(':')
    port = int(port)
else:
    port = 443 if use_ssl else 80

print(f"\nConnection details:")
print(f"Host: {host}")
print(f"Port: {port}")
print(f"SSL: {use_ssl}")

# Try to create a gRPC channel
try:
    if use_ssl:
        # Create SSL channel
        channel = grpc.secure_channel(f"{host}:{port}", grpc.ssl_channel_credentials())
    else:
        # Create insecure channel
        channel = grpc.insecure_channel(f"{host}:{port}")
    
    print("\n[SUCCESS] Channel created successfully!")
    
    # Test if we can list methods (this won't work without proper service stubs)
    # but at least we know the channel creation worked
    
except Exception as e:
    print(f"\n[ERROR] Failed to create channel: {e}")
    import traceback
    traceback.print_exc()
