from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from service.secure import decrypt
from config.settings import Settings

settings = Settings()
engine = create_async_engine(f'mysql+aiomysql://{decrypt(settings.MYSQL_USER)}:{decrypt(settings.MYSQL_PWD)}@{decrypt(settings.MYSQL_HOST)}:{settings.MYSQL_PORT}/tfdb?charset=utf8mb4', echo=True, future=True)


async def conn_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
