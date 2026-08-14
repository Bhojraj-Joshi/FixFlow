from sqlalchemy.orm import Session

from app.services.models import ServiceRequest, ServiceCategory
from app.customers.models import Customer
from app.requests.models import RequestStatusHistory


def create_service_request(
    customer_user_id: int,
    request_data,
    db: Session,
):
    # 1. Find customer profile
    customer = (
        db.query(Customer)
        .filter(Customer.user_id == customer_user_id)
        .first()
    )

    if not customer:
        return None, "Customer profile not found"

    # 2. Check service category
    category = (
        db.query(ServiceCategory)
        .filter(
            ServiceCategory.id == request_data.category_id,
            ServiceCategory.is_active == True,
        )
        .first()
    )

    if not category:
        return None, "Service category not found or inactive"

    # 3. Create service request
    service_request = ServiceRequest(
        customer_id=customer.id,
        category_id=request_data.category_id,
        title=request_data.title,
        description=request_data.description,
        location=request_data.location,
        preferred_date=request_data.preferred_date,
        preferred_time=request_data.preferred_time,
        status="PENDING",
    )

    db.add(service_request)
    db.flush()

    # 4. Create initial status history
    history = RequestStatusHistory(
        request_id=service_request.id,
        old_status=None,
        new_status="PENDING",
        changed_by=customer_user_id,
        note="Service request created",
    )

    db.add(history)

    # 5. Save everything
    db.commit()
    db.refresh(service_request)

    return service_request, None

def get_customer_requests(
    customer_user_id: int,
    db: Session,
):
    customer = (
        db.query(Customer)
        .filter(Customer.user_id == customer_user_id)
        .first()
    )

    if not customer:
        return None

    return (
        db.query(ServiceRequest)
        .filter(
            ServiceRequest.customer_id == customer.id
        )
        .order_by(ServiceRequest.created_at.desc())
        .all()
    )


def get_customer_request(
    customer_user_id: int,
    request_id: int,
    db: Session,
):
    customer = (
        db.query(Customer)
        .filter(Customer.user_id == customer_user_id)
        .first()
    )

    if not customer:
        return None

    return (
        db.query(ServiceRequest)
        .filter(
            ServiceRequest.id == request_id,
            ServiceRequest.customer_id == customer.id,
        )
        .first()
    )