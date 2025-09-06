"""
FastAPI Application Configuration
"""
import os
from typing import Optional

class Settings:
    """Application configuration"""
    
    # Basic application information
    APP_NAME: str = "FastAPI Simple Project"
    APP_DESCRIPTION: str = "A simple and straightforward FastAPI application"
    APP_VERSION: str = "0.1.0"
    
    # Server configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # Environment variables (optional)
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    
    # CORS settings
    ALLOWED_ORIGINS: list = ["*"]  # In production, specify allowed domains
    
    def __init__(self):
        """Initialize configuration with environment variables"""
        # Load from environment variables if they exist
        self.APP_NAME = os.getenv("APP_NAME", self.APP_NAME)
        self.DEBUG = os.getenv("DEBUG", "true").lower() == "true"
        self.HOST = os.getenv("HOST", self.HOST)
        self.PORT = int(os.getenv("PORT", self.PORT))

# Create global configuration instance
settings = Settings()
