from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.logging import logger

from app.exceptions.custom import AppException
from app.exceptions.handlers import (
    app_exception_handler,
    http_exception_handler,
    validation_exception_handler,
    unhandled_exception_handler
)

from app.middleware.logging import log_requests
from app.middleware.request_id import (
    request_id_middleware
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info(
        "Starting Enterprise FastAPI..."
    )

    yield

    logger.info(
        "Stopping Enterprise FastAPI..."
    )


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)

app.middleware("http")(request_id_middleware)

app.middleware("http")(log_requests)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(
    AppException,
    app_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler
)

app.add_exception_handler(
    Exception,
    unhandled_exception_handler
)

app.include_router(
    api_router,
    prefix=f"/api/{settings.API_VERSION}"
)


@app.get("/")
async def root():

    return {
        "success": True,
        "message": "Enterprise FastAPI Running"
    }