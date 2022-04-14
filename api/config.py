from pydantic import BaseSettings


class Settings(BaseSettings):
    API_VERSION: str = "1.0"
    API_URL_PREFIX: str = ""
    STAGE: str = ""
    ROOT_PATH: str = ""

    SECRET_KEY: str = ""
    USE_SENTRY: bool = True
    SENTRY_DSN: str = ""

    class Config:
        env_file = ".env"


settings = Settings()

settings.ROOT_PATH = f"/{settings.STAGE}" if settings.STAGE else ""
