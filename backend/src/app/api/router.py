from fastapi import APIRouter

from src.app.api.auth import auth_router
from src.app.api.check import check_router
from src.app.api.config import config_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(check_router, prefix="/check", tags=["check"])
router.include_router(config_router, tags=["config"])
