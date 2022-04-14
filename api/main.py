# flake8: noqa E402
import os

import django

# Django settings must be loaded before the FastAPI app
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DDD.settings")
django.setup(set_prefix=False)
from typing import Any
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mangum import Mangum
from starlette.requests import Request
from business_logic.exceptions import IlegalStateException
from api.config import settings
from api.routes import router

app: Any = FastAPI(
    title="E2E API",
    version=settings.API_VERSION,
    root_path=settings.ROOT_PATH,
)

general_exception = {
    "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
    "error_message": "An unexpected internal error ocurred",
    "error_code": "DDD000",
}


@app.exception_handler(IlegalStateException)
def talma_exception_handler(request: Request, cmd_exception: IlegalStateException):
    return JSONResponse(
        status_code=cmd_exception.status_code,
        content=cmd_exception.detail,
    )


@app.middleware("http")
def check_exception_handler(request: Request, call_next):
    try:
        response = call_next(request)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=general_exception
        )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if settings.USE_SENTRY:
    import sentry_sdk
    from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        environment=settings.STAGE or "local",
    )

    app.add_middleware(SentryAsgiMiddleware)


@app.get("/", tags=["Health Check"])
def health_check():
    return {"message": f"It Works! (v{settings.API_VERSION})"}


app.include_router(router, prefix=settings.API_URL_PREFIX)

# For deployment via AWS Lambda
handler = Mangum(app)
