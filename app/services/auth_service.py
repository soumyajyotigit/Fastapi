from app.db.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.password import hash_password


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
            raise ValueError(
                "Email already registered."
            )

        existing_username = await UserRepository.get_by_username(
            db,
            data.username,
        )

        if existing_username:
            raise ValueError(
                "Username already exists."
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