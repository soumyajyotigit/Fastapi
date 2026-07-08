from fastapi import Request


async def auth_middleware(
    request: Request,
    call_next
):
    """
    Placeholder middleware.

    JWT Authentication
    will be added in Phase 3.
    """

    response = await call_next(request)

    return response