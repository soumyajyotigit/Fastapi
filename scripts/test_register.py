import asyncio

from app.db.models.user import User
from app.db.session import AsyncSessionLocal
from app.repositories.user_repository import UserRepository
from app.utils.password import hash_password


async def main():

    async with AsyncSessionLocal() as db:

        user = User(

            full_name="Soumya Jyoti",

            username="soumya",

            email="soumya@gmail.com",

            phone="9876543210",

            password=hash_password(
                "admin123"
            ),
        )

        created = await UserRepository.create(
            db,
            user,
        )

        print(created)


asyncio.run(main())