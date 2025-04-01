import pytest
from config import settings
from piccolo.engine.postgres import PostgresEngine, asyncpg
from models import User
from starlette.testclient import TestClient
from app import app


@pytest.fixture(scope="session")
async def _create_test_db():
    conn = await asyncpg.connect(
        user=settings.DB_USER_TEST,
        password=settings.DB_PASS_TEST,
        host=settings.DB_HOST_TEST,
        database=settings.DB_DATABASE_TEST,
    )

    test_db_name = "postgres"

    try:
        await conn.execute(f"CREATE DATABASE {test_db_name}")
    except asyncpg.DuplicateDatabaseError:
        await conn.execute(f"DROP DATABASE {test_db_name}")
        await conn.execute(f"CREATE DATABASE {test_db_name}")
    finally:
        await conn.close()

    yield test_db_name

    conn = await asyncpg.connect(
        user=settings.DB_USER_TEST,
        password=settings.DB_PASS_TEST,
        host=settings.DB_HOST_TEST,
        database=settings.DB_DATABASE_TEST,
    )
    await conn.execute(f"DROP DATABASE {test_db_name}")
    await conn.close()


@pytest.fixture()
async def postgres_engine():
    engine = PostgresEngine(
        config={
            "host": settings.DB_HOST_TEST,
            "database": settings.DB_NAME_TEST,
            "user": settings.DB_USER_TEST,
            "password": settings.DB_PASS_TEST,
        }
    )
    yield engine
    await engine.close_connection_pool()


@pytest.fixture(autouse=True)
async def setup_db(postgres_engine):
    for table in [User]:
        table._meta.db = postgres_engine

    await User.create_table(if_not_exists=True)

    yield

    await User.alter().drop_table(if_exists=True).run()


@pytest.fixture()
async def client():
    return TestClient(app, base_url="http://0.0.0.0:8000")


@pytest.fixture()
async def user():
    return await User.objects().create(
        name="test", role="USER", api_key="key-da230cf1-f07e-4934-bdb0-0e6959999c37"
    )
