from fastapi import APIRouter

from src.app.db.connection import pool

get_user_router = APIRouter()


query = """
select
    id
    ,username
    ,password
    ,email
    ,role_id
from usr.user
"""


@get_user_router.get("/get_user")
async def get_user():
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(query)
            response = await cur.fetchall()

    return response
