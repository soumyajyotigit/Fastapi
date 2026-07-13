from datetime import datetime, timezone

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.refresh_token import RefreshToken


class RefreshTokenRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        token: RefreshToken,
    ):

        db.add(token)

        await db.commit()

        await db.refresh(token)

        return token

    @staticmethod
    async def get_token(
        db: AsyncSession,
        token: str,
    ):

        result = await db.execute(
            select(RefreshToken).where(
                RefreshToken.token == token
            )
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def delete_token(
        db: AsyncSession,
        token: str,
    ):

        await db.execute(
            delete(RefreshToken).where(
                RefreshToken.token == token
            )
        )

        await db.commit()

    @staticmethod
    async def delete_all_user_tokens(
        db: AsyncSession,
        user_id,
    ):

        await db.execute(
            delete(RefreshToken).where(
                RefreshToken.user_id == user_id
            )
        )

        await db.commit()

    @staticmethod
    async def delete_expired_tokens(
        db: AsyncSession,
    ):

        await db.execute(
            delete(RefreshToken).where(
                RefreshToken.expires_at < datetime.now(timezone.utc)
            )
        )

        await db.commit()