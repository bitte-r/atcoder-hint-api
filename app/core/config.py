from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(
        default="AtCoder Hint API"
    )
    API_V1_STR: str = Field(
        default = "/api/v1"
    )
    GEMINI_API_KEY: str = Field(
        ...
    )
    model_config = SettingsConfigDict(
        env_file=".env"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

