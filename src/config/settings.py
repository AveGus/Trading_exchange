from pydantic_settings import BaseSettings, SettingsConfigDict
from piccolo.conf.apps import AppRegistry


APP_REGISTRY = AppRegistry(apps=["config.piccolo_app"])


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    DB_HOST: str = "127.0.0.1"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "postgres"
