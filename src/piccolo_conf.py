from piccolo.engine.postgres import PostgresEngine
from piccolo.conf.apps import AppRegistry
from config import settings

APP_REGISTRY = AppRegistry(apps=["config.piccolo_app"])
DB = PostgresEngine(
    config={
        "host": settings.DB_HOST,
        "port": settings.DB_PORT,
        "user": settings.DB_USER,
        "password": settings.DB_PASS,
        "database": settings.DB_NAME,
    }
)
