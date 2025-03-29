from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2025-03-30T02:55:37:856061"
VERSION = "1.24.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(migration_id=ID, app_name="", description=DESCRIPTION)

    def run():
        print(f"running {ID}")

    manager.add_raw(run)

    return manager
