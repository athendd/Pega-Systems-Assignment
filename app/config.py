"""
Application configuration module.
"""

from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Defines application configuration using Pydantic BaseSettings.

    Settings are loaded from environment variables and optionally
    from a .env file. Environment variables override default values.
    """

    database_url: str
    debug: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'