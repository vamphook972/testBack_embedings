from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # MySQL para datos principales
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://admin:5123@localhost:5432/winedb",
        description="URL de conexión a PostgreSQL"
    )
    
    APP_NAME: str = Field(default="Wine Reviews API")
    APP_VERSION: str = Field(default="1.0.0")
    DEBUG: bool = Field(default=False)
    # Orígenes permitidos para CORS. Se puede configurar en .env como
    # una lista JSON o dejar el valor por defecto (permitir todo) para desarrollo.
    ALLOWED_ORIGINS: List[str] = Field(default=["*"], description="Orígenes permitidos CORS")
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()