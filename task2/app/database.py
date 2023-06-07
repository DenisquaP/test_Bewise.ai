from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
)
from settings import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session():
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
