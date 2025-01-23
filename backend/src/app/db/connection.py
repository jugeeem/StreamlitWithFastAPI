from functools import lru_cache

from psycopg_pool import AsyncConnectionPool

from src.app.core import settings

conninfo = f"dbname={settings.POSTGRES_DB} user={settings.POSTGRES_USER} password={settings.POSTGRES_PASSWORD} host={settings.POSTGRES_HOST} port={settings.POSTGRES_PORT}"


@lru_cache
def get_async_pool() -> AsyncConnectionPool:
    return AsyncConnectionPool(conninfo=conninfo, open=False)


pool = get_async_pool()
