import os

from piccolo.conf.apps import AppConfig, table_finder

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

APP_CONFIG = AppConfig(
    app_name="default",
    migrations_folder_path=os.path.join(CURRENT_DIRECTORY, "../models/migrations"),
    table_classes=table_finder(modules=["models"]),
    migration_dependencies=[],
    commands=[],
)
