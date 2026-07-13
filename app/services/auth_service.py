from app.db.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.password import hash_password
from app.utils.password import verify_password
from app.utils.jwt import (
    create_access_token,
    create_refresh_token,
)
from app.schemas.auth import TokenResponse
from datetime import datetime, timedelta, timezone

from app.db.models.refresh_token import RefreshToken
from app.repositories.refresh_token_repository import (
    RefreshTokenRepository,
)
from app.core.config import settings
from app.exceptions.custom import AppException

class AuthService:

    @staticmethod
    async def register(
        db,
        data,
    ):

        existing_email = await UserRepository.get_by_email(
            db,
            data.email,
        )

        if existing_email:
            raise AppException(
                "Email already registered.",
                status_code=409,
            )

        existing_username = await UserRepository.get_by_username(
            db,
            data.username,
        )

        if existing_username:
            raise AppException(
                "Username already exists.",
                status_code=409,
            )

        user = User(

            full_name=data.full_name,

            username=data.username,

            email=data.email,

            phone=data.phone,

            password=hash_password(
                data.password
            ),
        )

        return await UserRepository.create(
            db,
            user,
        )

    @staticmethod
    async def login(
            db,
            data,
    ):

        user = await UserRepository.authenticate(
            db,
            data.username,
        )

        if not user:
            raise AppException(
                "Invalid email or password",
                status_code=401,
            )

        if not verify_password(
                data.password,
                user.password,
        ):
            raise AppException(
                "Invalid email or password",
                status_code=401,
            )

        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
            }
        )

        refresh_token = create_refresh_token(
            {
                "sub": str(user.id),
            }
        )
        refresh_token_db = RefreshToken(
            token=refresh_token,
            user_id=user.id,
            expires_at=datetime.now(timezone.utc)
                       + timedelta(
                days=settings.REFRESH_TOKEN_EXPIRE_DAYS
            ),
        )

        await RefreshTokenRepository.create(
            db,
            refresh_token_db,
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )
