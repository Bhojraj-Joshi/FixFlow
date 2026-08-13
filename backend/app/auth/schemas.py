from pydantic import BaseModel, EmailStr, Field


class UserRegisterSchema(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)
    role: str

    