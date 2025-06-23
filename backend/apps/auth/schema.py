from fastapi import Form

from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass

class UserLoginSchema(BaseModel):
    name: str
    password: str
