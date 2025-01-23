from typing import Annotated

from fastapi import APIRouter, status, Form

from src.app.dependency.auth import user_depends
from src.app.db.sql import config_query
from src.app.schema.config import InConfig, OutUpdateConfig
from src.app.db.util import execute_write_query


update_router = APIRouter()


@update_router.put(
    "/config",
    status_code=status.HTTP_200_OK,
    response_model=OutUpdateConfig,
)
async def update_config(
    form_data: Annotated[InConfig, Form()],
    current_user=user_depends,
) -> OutUpdateConfig:
    """
    ユーザ情報更新

    Args:
        form_data (InConfig): 更新情報
        current_user (User): ユーザ情報

    Returns:
        OutUpdateConfig: 更新結果
    """
    param_user = {
        "username": current_user.username,
        "email": form_data.email,
    }
    param_user_info = {
        "username": current_user.username,
        "first_name": form_data.first_name,
        "first_name_ruby": form_data.first_name_ruby,
        "last_name": form_data.last_name,
        "last_name_ruby": form_data.last_name_ruby,
        "full_name": form_data.first_name + " " + form_data.last_name,
        "full_name_ruby": form_data.first_name_ruby + " " + form_data.last_name_ruby,
        "zip_code": form_data.zip_code,
        "state": form_data.state,
        "city": form_data.city,
        "address": form_data.address,
        "phone_number": form_data.phone_number,
        "birthday": form_data.birthday,
    }
    try:
        await execute_write_query(
            config_query.UPDATE_MY_CONFIG_FOR_USER,
            param_user,
        )
        await execute_write_query(
            config_query.UPDATE_MY_CONFIG_FOR_USER_INFO,
            param_user_info,
        )
    except Exception as e:
        return {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": str(e),
        }

    return {
        "status": status.HTTP_200_OK,
        "message": "success",
    }
