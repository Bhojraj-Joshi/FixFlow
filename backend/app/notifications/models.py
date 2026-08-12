from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey,
    Enum,
)

from app.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    request_id = Column(
        Integer,
        ForeignKey("service_requests.id", ondelete="CASCADE"),
        nullable=True
    )

    title = Column(
        String(150),
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )

    notification_type = Column(
        Enum(
            "REQUEST_ASSIGNED",
            "REQUEST_ACCEPTED",
            "REQUEST_STARTED",
            "REQUEST_COMPLETED",
            "REQUEST_CANCELLED",
            "PAYMENT_SUCCESS",
            "PAYMENT_FAILED",
            "GENERAL"
        ),
        default="GENERAL"
    )

    is_read = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )