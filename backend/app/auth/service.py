from sqlalchemy.orm import Session

from app.users.models import User
from app.customers.models import Customer
from app.technicians.models import Technician

from app.auth.schemas import UserRegisterSchema


def hash_password(password: str) -> str:
    import bcrypt

    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def register_user(
    user_data: UserRegisterSchema,
    db: Session,
):
    # 1. Check if email already exists
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        return None

    # 2. Hash password
    hashed_password = hash_password(user_data.password)

    # 3. Create User
    user = User(
        name=user_data.full_name,
        email=user_data.email,
        password_hash=hashed_password,
        role=user_data.role,
    )

    db.add(user)
    db.flush()

    # 4. Create role-specific profile
    if user_data.role == "CUSTOMER":

        customer = Customer(
            user_id=user.id
        )

        db.add(customer)

    elif user_data.role == "TECHNICIAN":

        technician = Technician(
            user_id=user.id
        )

        db.add(technician)

    # 5. Save everything
    db.commit()
    db.refresh(user)

    return user


def verify_password(
    password: str,
    hashed_password: str
) -> bool:
    import bcrypt

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def login_user(
    email: str,
    password: str,
    db: Session,
):
    # 1. Find user by email
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    # 2. User not found
    if not user:
        return None

    # 3. Verify password
    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    # 4. Return authenticated user
    return user