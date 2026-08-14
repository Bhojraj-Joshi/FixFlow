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
from app.auth.routes import router as auth_router
from app.services.routes import router as services_router


app = FastAPI(
    title="FixFlow API",
    description="Service and Maintenance Management System",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(services_router)


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