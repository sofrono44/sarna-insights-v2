"""Test script for LLM providers."""
import asyncio
import json
from services.llm_service import LLMService
from core.config import settings

SYSTEM_PROMPT = """You are a financial analyst assistant helping users understand their portfolio data. 
You have access to anonymized portfolio information including margin requirements, positions, and balances. 
Always provide clear, actionable insights based on the data provided. 
Never mention account numbers or personal information in your responses."""

async def test_llm_providers():
    """Test all available LLM providers."""
    service = LLMService()
    
    print("=" * 60)
    print("LLM Provider Test")
    print("=" * 60)
    
    # Check which providers are available
    print("\nAvailable providers:", list(service.providers.keys()))
    
    if not service.providers:
        print("\n❌ No LLM providers configured!")
        print("Please ensure you have API keys set in your .env file:")
        print("  - OPENAI_API_KEY")
        print("  - ANTHROPIC_API_KEY")
        print("  - GOOGLE_API_KEY")
        return
    
    # Sample portfolio data for context
    portfolio_data = {
        "total_margin": 350000,
        "total_buying_power": 1050000,
        "accounts": 9,
        "average_margin_utilization": 0.33
    }
    
    # Test query with context
    test_prompt = f"""Given the following portfolio data:
    - Total Margin Requirement: ${portfolio_data['total_margin']:,}
    - Total Buying Power: ${portfolio_data['total_buying_power']:,}
    - Number of Accounts: {portfolio_data['accounts']}
    - Average Margin Utilization: {portfolio_data['average_margin_utilization']:.1%}
    
    Question: What is the overall health of this portfolio? Provide a brief assessment."""
    
    # Test each available provider
    for provider_name in service.providers.keys():
        print(f"\n{'='*60}")
        print(f"Testing {provider_name.upper()} Provider")
        print(f"{'='*60}")
        
        try:
            start_time = asyncio.get_event_loop().time()
            response = await service.query(
                prompt=test_prompt,
                provider=provider_name,
                system_prompt=SYSTEM_PROMPT
            )
            end_time = asyncio.get_event_loop().time()
            
            print(f"✅ Success! Response time: {end_time - start_time:.2f}s")
            print(f"\nResponse preview:")
            print("-" * 40)
            # Show first 300 characters of response
            preview = response[:300] + "..." if len(response) > 300 else response
            print(preview)
            print("-" * 40)
            
            # Verify response quality
            if "margin" in response.lower() or "portfolio" in response.lower():
                print("✅ Response appears to address the portfolio question")
            else:
                print("⚠️  Response may not be addressing the question properly")
                
        except Exception as e:
            print(f"❌ Error: {type(e).__name__}: {str(e)}")
            
    print("\n" + "="*60)
    print("Test Complete!")
    print("="*60)
    
    # Test provider switching
    if len(service.providers) > 1:
        print("\n📝 Testing provider switching...")
        providers = list(service.providers.keys())
        
        try:
            # Quick test with first provider
            response1 = await service.query(
                "What is 2+2?",
                provider=providers[0]
            )
            print(f"✅ {providers[0]} responded correctly")
            
            # Quick test with second provider
            response2 = await service.query(
                "What is 2+2?",
                provider=providers[1]
            )
            print(f"✅ {providers[1]} responded correctly")
            print("✅ Provider switching works!")
            
        except Exception as e:
            print(f"❌ Provider switching error: {e}")

async def main():
    """Run the test."""
    await test_llm_providers()

if __name__ == "__main__":
    asyncio.run(main())
