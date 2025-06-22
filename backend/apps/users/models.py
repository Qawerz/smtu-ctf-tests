from typing import Optional, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from config.settings import Base

class Users(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    team: Mapped[str]
    points: Mapped[int]

    def __str__(self) -> str:
        return self.name