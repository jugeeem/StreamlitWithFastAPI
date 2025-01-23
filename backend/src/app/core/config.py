from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application
    """

    # frontend settings
    FRONTEND_CONTAINER_HOST: str
    FRONTEND_LOCAL_HOST: str
    FRONTEND_CONTAINER_PORT: int
    FRONTEND_LOCAL_PORT: int
    FRONTEND_CONTAINER_PATH: str

    # backend settings
    BACKEND_TITLE: str
    BACKEND_VERSION: str
    BACKEND_CONTAINER_HOST: str
    BACKEND_LOCAL_HOST: str
    BACKEND_CONTAINER_PORT: int
    BACKEND_LOCAL_PORT: int
    BACKEND_ROOT_PATH: str
    BACKEND_SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DEFAULT_USER_ROLE: int = 3

    # database settings
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # nginx settings
    NGINX_CONTAINER_PORT: int
    NGINX_LOCAL_PORT: int

    # docker-compose.yml
    HEALTHCHCEK_INTERVAL: str
    HEALTHCHECK_TIMEOUT: str
    HEALTHCHECK_RETRIES: int
    HEALTHCHECK_START_PERIOD: str
