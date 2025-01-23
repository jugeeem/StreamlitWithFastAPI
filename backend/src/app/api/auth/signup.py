from fastapi import APIRouter, Form, HTTPException, status

from src.app import auth
from src.app.core import settings
from src.app.schema.auth import InSignup, OutSignup

signup_router = APIRouter()


@signup_router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=OutSignup
)
async def signup(form_data: InSignup) -> OutSignup:
    """
    /auth/signup route

    Args:
        form_data (InSignup): リクエスト ペイロード

    Returns:
        OutSignup: レスポンス ペイロード
    """
    exists_flag: bool = await auth.exists_user(form_data.username)
    if exists_flag:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User already exists",
        )
    hashed_password = auth.get_password_hash(form_data.password)
    param_insert_user = [
        form_data.email,
        form_data.username,
        hashed_password,
        settings.DEFAULT_USER_ROLE,
    ]
    param_insert_user_info = [form_data.username]
    await auth.register_user(param_insert_user, param_insert_user_info)

    return {
        "message": "User registration completed",
    }
