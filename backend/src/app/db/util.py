from psycopg.rows import class_row
from pydantic import BaseModel

from src.app.db.connection import pool


async def execute_read_query(
    query: str, param: list, model: BaseModel | list[BaseModel]
):
    """
    SELECT文のクエリ発行

    Args:
        query (str): クエリ文
        param (list): パラメータ
        model (BaseModel | list[BaseModel]): モデル

    Returns:
        BaseModel | list[BaseModel]: レスポンス
    """
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=class_row(model)) as cur:
            await cur.execute(query, param)
            response = await cur.fetchall()

    return response


async def execute_write_query(query: str, param: list) -> None:
    """
    INSERT/UPDATE/DELETE文のクエリ発行

    Args:
        query (str): クエリ文
        param (list): パラメータ
    """
    async with pool.connection() as conn:
        await conn.execute(query, param)
