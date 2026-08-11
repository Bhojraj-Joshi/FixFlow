from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Text,
    Date,
    Time,
    DateTime,
    ForeignKey,
    Enum,
)

from app.database import Base


class ServiceCategory(Base):
    __tablename__ = "service_categories"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    description = Column(
        Text
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class ServiceRequest(Base):
    __tablename__ = "service_requests"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id", ondelete="CASCADE"),
        nullable=False
    )

    category_id = Column(
        Integer,
        ForeignKey("service_categories.id", ondelete="RESTRICT"),
        nullable=False
    )

    title = Column(
        String(150),
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    location = Column(
        String(255),
        nullable=False
    )

    preferred_date = Column(
        Date
    )

    preferred_time = Column(
        Time
    )

    status = Column(
        Enum(
            "PENDING",
            "ASSIGNED",
            "ACCEPTED",
            "IN_PROGRESS",
            "COMPLETED",
            "CANCELLED"
        ),
        default="PENDING"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )