from datetime import date, time, datetime

from pydantic import BaseModel, Field


class ServiceRequestCreateSchema(BaseModel):
    category_id: int
    title: str = Field(min_length=3, max_length=150)
    description: str = Field(min_length=5)
    location: str = Field(min_length=2, max_length=255)
    preferred_date: date | None = None
    preferred_time: time | None = None


class ServiceRequestResponseSchema(BaseModel):
    id: int
    customer_id: int
    category_id: int
    title: str
    description: str
    location: str
    preferred_date: date | None
    preferred_time: time | None
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True