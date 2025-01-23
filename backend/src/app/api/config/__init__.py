from fastapi import APIRouter

from src.app.api.config.read import read_router
from src.app.api.config.update import update_router


config_router = APIRouter()

config_router.include_router(read_router)
config_router.include_router(update_router)
