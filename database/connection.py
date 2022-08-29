from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

db_user = "kailoslab"
db_pw = "Kailos0601!"
db_name = "tfdb"
engine = create_async_engine(f'mysql+aiomysql://{db_user}:{db_pw}@localhost:3306/{db_name}?charset=utf8mb4', echo=True, future=True)


async def conn():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
