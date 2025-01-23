from fastapi import APIRouter

from src.app.api.check.get_user import get_user_router

check_router = APIRouter()

check_router.include_router(get_user_router)
