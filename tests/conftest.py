import asyncio
import pytest
from unittest.mock import AsyncMock, patch

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession

from source.config import settings
from source.main import app
from source.models import Base


@pytest.fixture(scope="session")
def async_engine() -> AsyncEngine:
    _async_engine = create_async_engine(
        url=settings.database_url,
        echo=False,
        future=True,
        pool_size=50,
        max_overflow=100,
    )
    return _async_engine


@pytest.fixture(scope="session")
def async_session_maker(async_engine):
    _async_session_maker = async_sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )
    return _async_session_maker


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def setup_db(async_engine):
    assert settings.MODE == "TEST"
    async with async_engine.begin() as db_conn:
        await db_conn.run_sync(Base.metadata.drop_all)
        await db_conn.run_sync(Base.metadata.create_all)
    yield
    async with async_engine.begin() as db_conn:
        await db_conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def async_session(async_session_maker) -> AsyncSession:
    async with async_session_maker() as _async_session:
        yield _async_session


@pytest.fixture()
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def mock_redis_client():
    with patch("source.utils.cache.redis.Redis") as MockRedis:
        # Создаем AsyncMock для мока клиента Redis
        mock_client = AsyncMock()
        # Настраиваем методы mock_client как асинхронные
        MockRedis.return_value = mock_client
        mock_client.get = AsyncMock(return_value=None)  # Настроить get как асинхронный
        mock_client.set = AsyncMock(return_value=None)  # Настроить set как асинхронный
        yield mock_client
