from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    Text,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    Enum,
    Time,
)

from app.database import Base


class Technician(Base):
    __tablename__ = "technicians"

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

    experience_years = Column(
        Integer,
        default=0
    )

    is_approved = Column(
        Boolean,
        default=False
    )

    bio = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class TechnicianSkill(Base):
    __tablename__ = "technician_skills"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    technician_id = Column(
        Integer,
        ForeignKey("technicians.id", ondelete="CASCADE"),
        nullable=False
    )

    category_id = Column(
        Integer,
        ForeignKey("service_categories.id", ondelete="CASCADE"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    __table_args__ = (
        UniqueConstraint(
            "technician_id",
            "category_id"
        ),
    )


class TechnicianAvailability(Base):
    __tablename__ = "technician_availability"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    technician_id = Column(
        Integer,
        ForeignKey("technicians.id", ondelete="CASCADE"),
        nullable=False
    )

    day_of_week = Column(
        Enum(
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY"
        ),
        nullable=False
    )

    start_time = Column(
        Time,
        nullable=False
    )

    end_time = Column(
        Time,
        nullable=False
    )

    is_available = Column(
        Boolean,
        default=True
    )