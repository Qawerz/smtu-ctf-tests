from typing import Optional, List
from fastapi import APIRouter, Depends

from .service import UsersService, get_user_service
from . import schema


app = APIRouter(prefix='/api/v1/users', tags=["Пользователи"])

@app.get("/", summary="Список пользователей",response_model=List[schema.UserInfo])
async def list(
        limit:Optional[int] = 60, 
        service:UsersService = Depends(get_user_service)
    ):
    return await service.get_list(limit)

@app.get("/{id}",summary="Один пользователь", response_model=schema.UserInfo)
async def get_one(
        id:int, 
        service:UsersService = Depends(get_user_service)
    ):
    return await service.get_one(id)

@app.post("/{id}", summary="Создание пользователя", status_code=201)
async def create(
        data:schema.UserCreateUpdate = Depends(), 
        service:UsersService = Depends(get_user_service)
    ):
    return await service.create(data)

@app.put("/{id}/update", summary="Обновить пользователя", status_code=200)
async def update(
        id:int,
        data: schema.UserCreateUpdate = Depends(),
        service: UsersService = Depends(get_user_service)
    ):
    return await service.update()

@app.delete("/{id}", summary="Удаление пользлвателя")
async def delete(
        id: int,
        service:UsersService = Depends(get_user_service)
    ):
    return await service.delete(id)