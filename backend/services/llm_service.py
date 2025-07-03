"""Multi-provider LLM service with Anthropic fix for v0.8.0."""
import logging
from typing import Dict, Any, Optional
from abc import ABC, abstractmethod
import openai
import anthropic
import google.generativeai as genai
from core.config import settings

logger = logging.getLogger(__name__)


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    @abstractmethod
    async def query(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Send query to LLM and return response."""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI GPT provider."""
    
    def __init__(self):
        self.client = openai.AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    
    async def query(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            temperature=0.7,
            max_tokens=2000
        )
        
        return response.choices[0].message.content


class AnthropicProvider(LLMProvider):
    """Anthropic Claude provider."""
    
    def __init__(self):
        self.client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
    
    async def query(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        messages = [{"role": "user", "content": prompt}]
        
        # Prepare kwargs for the API call
        kwargs = {
            "model": "claude-3-5-sonnet-20241022",  # Latest Claude 3.5 Sonnet
            "messages": messages,
            "max_tokens": 2000,
            "temperature": 0.7
        }
        
        # Only add system if it's provided
        if system_prompt:
            kwargs["system"] = system_prompt
        
        response = await self.client.messages.create(**kwargs)
        
        return response.content[0].text


class GoogleProvider(LLMProvider):
    """Google Gemini provider."""
    
    def __init__(self):
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')  # Updated to available model
    
    async def query(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        full_prompt = prompt
        if system_prompt:
            full_prompt = f"{system_prompt}\n\n{prompt}"
        
        response = await self.model.generate_content_async(full_prompt)
        return response.text


class LLMService:
    """Service for managing multiple LLM providers."""
    
    def __init__(self):
        self.providers = {}
        
        # Initialize available providers
        if settings.OPENAI_API_KEY and settings.OPENAI_API_KEY != 'your-openai-key-here':
            self.providers['openai'] = OpenAIProvider()
            
        if settings.ANTHROPIC_API_KEY and settings.ANTHROPIC_API_KEY != 'your-anthropic-key-here':
            self.providers['anthropic'] = AnthropicProvider()
            
        if settings.GOOGLE_API_KEY and settings.GOOGLE_API_KEY != 'your-google-key-here':
            self.providers['google'] = GoogleProvider()
    
    async def query(
        self, 
        prompt: str, 
        provider: str = 'openai',
        system_prompt: Optional[str] = None
    ) -> str:
        """Query the specified LLM provider."""
        if provider not in self.providers:
            available = list(self.providers.keys())
            raise ValueError(f"Provider '{provider}' not available. Available: {available}")
        
        try:
            return await self.providers[provider].query(prompt, system_prompt)
        except Exception as e:
            logger.error(f"LLM query failed with {provider}: {e}")
            raise
