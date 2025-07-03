"""Test script for gRPC client connection."""
import asyncio
import logging
import json
from services.grpc_client import get_grpc_client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_grpc_connection():
    """Test the gRPC connection and fetch sample data."""
    try:
        # Get the gRPC client
        logger.info("Getting gRPC client...")
        client = await get_grpc_client()
        
        # Test fetching current margin data for group 10006
        logger.info("Fetching current margin data for group 10006...")
        margin_data = await client.get_current_margin_data(group_id=10006)
        
        logger.info("Successfully fetched margin data!")
        logger.info(f"Number of accounts: {len(margin_data['accounts'])}")
        logger.info(f"Total margin: ${margin_data['total_margin']:,.2f}")
        logger.info(f"Total buying power: ${margin_data['total_buying_power']:,.2f}")
        logger.info(f"Total excess liquidity: ${margin_data['total_excess_liquidity']:,.2f}")
        
        # Print account summaries
        for account in margin_data['accounts']:
            logger.info(f"\nAccount {account['account_id']}:")
            logger.info(f"  - Cash: ${account.get('cash', 0):,.2f}")
            logger.info(f"  - Risk Type: {account.get('risk_type', 'N/A')}")
            logger.info(f"  - Buying Power: ${account.get('buying_power', 0):,.2f}")
        
        # Save to file for inspection
        with open('test_margin_response.json', 'w') as f:
            json.dump(margin_data, f, indent=2)
        logger.info("\nSaved response to test_margin_response.json")
        
        return True
        
    except Exception as e:
        logger.error(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    # Run the test
    success = asyncio.run(test_grpc_connection())
    
    if success:
        print("\n✅ gRPC connection test PASSED!")
    else:
        print("\n❌ gRPC connection test FAILED!")
