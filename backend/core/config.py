"""Application configuration."""
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    # API Configuration
    APP_NAME: str = "Sarna Insights"
    VERSION: str = "2.0.0"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    
    # Sarna API
    SARNA_API_URL: str
    SARNA_JWT_TOKEN: str
    RISK_SYSTEM_USE_TLS: bool = True
    
    # Database
    DATABASE_URL: str
    REDIS_URL: str
    
    # LLM Providers
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    GOOGLE_API_KEY: str = ""
    
    # Pinecone (optional)
    PINECONE_API_KEY: str = ""
    PINECONE_ENVIRONMENT: str = ""
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:80", "http://localhost:8000"]
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


# Global settings instance
settings = Settings()
