from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    fullname: str
    email: EmailStr
    password: str = Field(..., min_length=4)


class UserResposne(BaseModel):
    id: int
    fullname: str
    email: EmailStr
    is_admin: bool
    created_at: datetime
