import time

from fastapi import Request

from app.core.logging import logger


async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = round(
        time.time() - start_time,
        4
    )

    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"{response.status_code} "
        f"{process_time}s"
    )

    return response