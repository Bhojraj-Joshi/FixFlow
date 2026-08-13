from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(20)
    )

    address = Column(
        String(255)
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )