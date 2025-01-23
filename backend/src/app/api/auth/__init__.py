from fastapi import APIRouter

from src.app.api.auth.signup import signup_router
from src.app.api.auth.token import token_router

auth_router = APIRouter()

auth_router.include_router(signup_router)
auth_router.include_router(token_router)
