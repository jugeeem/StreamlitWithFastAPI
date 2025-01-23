from fastapi import APIRouter


read_router = APIRouter()


@read_router.get("/config")
async def read_config():
    return {"contents": "config"}
