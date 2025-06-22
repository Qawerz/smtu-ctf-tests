from typing import Generic, Type, TypeVar, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from config.settings import Base
from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy import update, delete

ModelType = TypeVar("ModelType", bound=Base)

class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self.table = model
        self.db_session = db_session

    async def get_list(self, limit: Optional[int] = None):
        async with self.db_session as session:
            
            query = await session.execute(
                select(self.table).limit(limit).order_by(-self.table.id.desc())
            )
            return query.scalars().all()

    async def get_one(self, id):
        async with self.db_session as session:
            
            db_item = await session.execute(
                select(self.table).filter(self.table.id == id)
            )
            db_item = db_item.scalar()
            if not db_item:
                raise HTTPException(status_code=404, detail="Страница не найдена")
            return db_item

    async def create(self, data):

        async with self.db_session as session:
            item = self.table(**data.dict())
            session.add(item)
            await session.commit()
        return item

        async def update(self, id, data):
            async with self.db_session as session:
                db_item = await session.execute(
                    select(self.table).filter(self.table.id == id)
                )
                if not db_item.scalar():
                    raise HTTPException(status_code=404, detail="Страница не найдена")
                
                # Perform the update
                await session.execute(
                    update(self.table)
                    .where(self.table.id == id)
                    .values(**data.dict(exclude_unset=True))
                )
                await session.commit()
                
                updated_item = await session.execute(
                    select(self.table).filter(self.table.id == id)
                )
                return updated_item.scalar()

    async def delete(self, id):
        async with self.db_session as session:
            await session.execute(delete(self.table).filter(self.table.id == id))
            await session.commit()
        return None