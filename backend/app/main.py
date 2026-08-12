from fastapi import FastAPI

from app.users.models import User
from app.customers.models import Customer
from app.technicians.models import (
    Technician,
    TechnicianSkill,
    TechnicianAvailability,
)
from app.services.models import ServiceCategory, ServiceRequest
from app.assignments.models import RequestAssignment
from app.requests.models import RequestStatusHistory
from app.payments.models import Payment
from app.notifications.models import Notification
from app.reviews.models import Review


app = FastAPI(
    title="FixFlow API",
    description="Service and Maintenance Management System",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to FixFlow API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }