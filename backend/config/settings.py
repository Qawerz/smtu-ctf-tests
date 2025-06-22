from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url:str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings: Settings = Settings()

engine = create_async_engine(
    settings.db_url
)

async def get_session():
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
        await session.close()

class Base(DeclarativeBase):
    pass