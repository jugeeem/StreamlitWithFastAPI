from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.app.api import router
from src.app.core import settings
from src.app.db.util import pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    await pool.open()
    yield
    await pool.close()


app = FastAPI(
    title=settings.BACKEND_TITLE,
    version=settings.BACKEND_VERSION,
    root_path=settings.BACKEND_ROOT_PATH,
    lifespan=lifespan,
)

# origins = [
#     settings.FRONTEND_CONTAINER_PATH,
# ]
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}
