from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Enum,
)

from app.database import Base


class RequestAssignment(Base):
    __tablename__ = "request_assignments"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    request_id = Column(
        Integer,
        ForeignKey("service_requests.id", ondelete="CASCADE"),
        nullable=False
    )

    technician_id = Column(
        Integer,
        ForeignKey("technicians.id", ondelete="CASCADE"),
        nullable=False
    )

    assigned_by = Column(
        Integer,
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False
    )

    status = Column(
        Enum(
            "PENDING",
            "ACCEPTED",
            "REJECTED",
            "COMPLETED",
            "CANCELLED"
        ),
        default="PENDING"
    )

    assigned_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    accepted_at = Column(
        DateTime,
        nullable=True
    )

    rejected_at = Column(
        DateTime,
        nullable=True
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )