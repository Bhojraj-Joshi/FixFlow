from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    CheckConstraint,
)

from app.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    request_id = Column(
        Integer,
        ForeignKey("service_requests.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id", ondelete="CASCADE"),
        nullable=False
    )

    technician_id = Column(
        Integer,
        ForeignKey("technicians.id", ondelete="CASCADE"),
        nullable=False
    )

    rating = Column(
        Integer,
        nullable=False
    )

    comment = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    __table_args__ = (
        CheckConstraint(
            "rating >= 1 AND rating <= 5",
            name="check_rating_range"
        ),
    )