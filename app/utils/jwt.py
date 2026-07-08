from datetime import datetime, timedelta, timezone

from jose import jwt

from app.core.config import settings


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
):

    to_encode = data.copy()

    expire = (
        datetime.now(timezone.utc)
        + (
            expires_delta
            or timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        )
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def create_refresh_token(
    data: dict,
):

    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload = data.copy()

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def decode_token(
    token: str,
):

    return jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )