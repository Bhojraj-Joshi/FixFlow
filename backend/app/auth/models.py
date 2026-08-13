from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Enum,
)

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    role = Column(
        Enum(
            "CUSTOMER",
            "TECHNICIAN",
            "ADMIN"
        ),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

created_at = Column(
    DateTime,
    default=lambda: datetime.now(timezone.utc)
)

updated_at = Column(
    DateTime,
    default=lambda: datetime.now(timezone.utc),
    onupdate=lambda: datetime.now(timezone.utc)
)