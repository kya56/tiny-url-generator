from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8',
                                      env_prefix="database__")
    host: str = 'localhost'
    name: str = 'tiny_url_generator'
    username: str = 'postgres'
    password: str = 'root'


@lru_cache
def get_database_config():
    return DatabaseConfig()
