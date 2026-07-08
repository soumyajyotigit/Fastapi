import asyncio

from sqlalchemy import text

from app.db.database import engine


async def main():

    async with engine.begin() as conn:

        result = await conn.execute(
            text("SELECT version()")
        )

        print(result.scalar())


if __name__ == "__main__":

    asyncio.run(main())