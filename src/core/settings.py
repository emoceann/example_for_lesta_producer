import sys
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # kafka
    KAFKA_URL: str
    BIG_QUERY_QUEUE: str
    COUCH_DB_QUEUE: str

    model_config = SettingsConfigDict(env_file=".env")


class TestSettings(Settings):
    model_config = SettingsConfigDict(env_file="test.env")


@lru_cache
def get_settings() -> Settings:
    if "pytest" in sys.modules:
        return TestSettings()
    return Settings()
