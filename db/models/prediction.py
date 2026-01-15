import uuid
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Prediction(Base):
    __tablename__ = "predictions"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(String(36), nullable=False)
    match_id: Mapped[str] = mapped_column(String(36), nullable=False)
    winner: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.utcnow
    )
