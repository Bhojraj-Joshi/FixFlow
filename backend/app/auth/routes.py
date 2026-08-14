from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.schemas import UserRegisterSchema, UserLoginSchema
from app.auth.service import register_user, login_user
from app.auth.security import create_access_token
from app.auth.dependencies import get_current_user
from app.users.models import User


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
@router.post("/login")
def login(
    user_data: UserLoginSchema,
    db: Session = Depends(get_db)
):
    user = login_user(
        email=user_data.email,
        password=user_data.password,
        db=db
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        user_id=user.id,
        role=user.role
    )

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
    }
@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user),
):
    return {
        "user_id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role,
    }