from fastapi import APIRouter, status

from src.app.dependency.auth import user_depends
from src.app.db.sql import config_query
from src.app.schema.config import ReadConfig, OutReadConfig
from src.app.db.util import execute_read_query


read_router = APIRouter()


@read_router.get(
    "/config",
    status_code=status.HTTP_200_OK,
    response_model=OutReadConfig,
)
async def read_config(current_user=user_depends) -> OutReadConfig:
    """
    ユーザ情報取得

    Args:
        current_user (User): ユーザ情報

    Returns:
        OutReadConfig: 設定情報
    """
    param = [current_user.username]
    response = await execute_read_query(
        config_query.SELECT_MY_CONFIG, param, ReadConfig
    )
    result = response[0]

    return {"contents": result}
