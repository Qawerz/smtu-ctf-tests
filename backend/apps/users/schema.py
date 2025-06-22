from fastapi import UploadFile, File, Form

from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class UserCreateUpdate(BaseModel):
    name: str = Form(...)
    team: str = Form(...)
    points: int = Form(...)

class UserInfo(BaseModel):
    id:int
    name: str
    team: str
    points: int

    class Config:
        from_attributes = True