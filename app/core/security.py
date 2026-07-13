from app.utils.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token,
)

from app.utils.password import (
    hash_password,
    verify_password,
)

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)

__all__ = [
    "oauth2_scheme",
    "hash_password",
    "verify_password",
    "create_access_token",
    "create_refresh_token",
    "decode_token",
]