from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    String,
)

from app.database import Base


class RequestStatusHistory(Base):
    __tablename__ = "request_status_history"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    request_id = Column(
        Integer,
        ForeignKey(
            "service_requests.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    old_status = Column(
        String(30),
        nullable=True
    )

    new_status = Column(
        String(30),
        nullable=False
    )

    changed_by = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="RESTRICT"
        ),
        nullable=False
    )

    note = Column(
        Text,
        nullable=True
    )

    changed_at = Column(
        DateTime,
        default=datetime.utcnow
    )