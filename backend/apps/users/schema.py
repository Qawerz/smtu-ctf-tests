from fastapi import Form

from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass

class UserCreateUpdate(BaseModel):
    name:str = Form(...)
    team:str = Form(...)
    points:int = Form(...)

    class Config:
        from_attributes = True

class UserInfo(UserCreateUpdate):
    id:int
