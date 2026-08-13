from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.schemas import UserRegisterSchema
from app.auth.service import register_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserRegisterSchema,
    db: Session = Depends(get_db)
):
    user = register_user(
        user_data=user_data,
        db=db
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    return {
        "message": "User registered successfully",
        "user_id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "role": user.role,
    }
