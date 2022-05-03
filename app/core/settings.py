import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()
class settings(BaseSettings):
    TITLE: str = 'ToDo CRUD'
    VERSION: str = 'V1.0.0'
    API_PREFIX: str = "/api/v1"
    RELOAD: bool = os.getenv('RELOAD') or True

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ACCESS_REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    SECRET_KEY: Optional[str] = os.urandom(16).hex()
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.getenv('POSTGRES_URL')

settings = settings()
