from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.users.models import User
from app.auth.dependencies import require_role

from app.services.schemas import (
    ServiceRequestCreateSchema,
    ServiceRequestResponseSchema,
)

from app.services.service import (
    create_service_request,
    get_customer_requests,
    get_customer_request,
)


router = APIRouter(
    prefix="/services",
    tags=["Service Requests"],
)


@router.post(
    "/requests",
    response_model=ServiceRequestResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_request(
    request_data: ServiceRequestCreateSchema,
    current_user: User = Depends(
        require_role("CUSTOMER")
    ),
    db: Session = Depends(get_db),
):
    service_request, error = create_service_request(
        customer_user_id=current_user.id,
        request_data=request_data,
        db=db,
    )

    if error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )

    return service_request


@router.get(
    "/requests",
    response_model=List[ServiceRequestResponseSchema],
)
def get_my_requests(
    current_user: User = Depends(
        require_role("CUSTOMER")
    ),
    db: Session = Depends(get_db),
):
    requests = get_customer_requests(
        customer_user_id=current_user.id,
        db=db,
    )

    if requests is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer profile not found",
        )

    return requests


@router.get(
    "/requests/{request_id}",
    response_model=ServiceRequestResponseSchema,
)
def get_my_request(
    request_id: int,
    current_user: User = Depends(
        require_role("CUSTOMER")
    ),
    db: Session = Depends(get_db),
):
    service_request = get_customer_request(
        customer_user_id=current_user.id,
        request_id=request_id,
        db=db,
    )

    if service_request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service request not found",
        )

    return service_request