from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from apps.base_repo.base_class import BaseService
from config.settings import get_session
from .models import Users

class UsersService(BaseService[Users]):
    def __init__(self, db_session: Session):
        super(UsersService, self).__init__(Users, db_session)

    
def get_user_service(db_session: AsyncSession = Depends(get_session)) -> UsersService:
    return UsersService(db_session)