from pydantic import BaseModel, EmailStr, Field, model_validator
from datetime import datetime



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
