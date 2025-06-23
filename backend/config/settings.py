from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pydantic_settings import BaseSettings

from authx import AuthX, AuthXConfig

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



config = AuthXConfig(
     JWT_ALGORITHM = "HS256",
     JWT_SECRET_KEY = "kek",
     JWT_TOKEN_LOCATION = ["headers"],
)

auth = AuthX(config=config)