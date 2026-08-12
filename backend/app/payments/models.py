from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    DateTime,
    ForeignKey,
    Enum,
    String,
)

from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    request_id = Column(
        Integer,
        ForeignKey("service_requests.id", ondelete="RESTRICT"),
        unique=True,
        nullable=False
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id", ondelete="RESTRICT"),
        nullable=False
    )

    amount = Column(
        Numeric(10, 2),
        nullable=False
    )

    payment_method = Column(
        Enum(
            "CASH",
            "CARD",
            "ONLINE"
        ),
        nullable=False
    )

    status = Column(
        Enum(
            "PENDING",
            "PAID",
            "FAILED",
            "REFUNDED"
        ),
        default="PENDING"
    )

    transaction_id = Column(
        String(100),
        unique=True,
        nullable=True
    )

    paid_at = Column(
        DateTime,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )