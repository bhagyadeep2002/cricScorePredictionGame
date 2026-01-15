import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Match(Base):
    __tablename__ = "matches"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    team1: Mapped[str] = mapped_column(String(100), nullable=False)
    team2: Mapped[str] = mapped_column(String(100), nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
    winner: Mapped[str] = mapped_column(String(100), nullable=True)
