from typing import Optional
from pydantic import BaseModel, validator


class Course(BaseModel):
    id: Optional[int] = None
    title: str
    hours: int
    lesson: int

    @validator("title")
    def validator_titulo(cls, value):
        if len(value.split()) < 3:
            raise ValueError("titulo must be at least 3 characters")
        
        return value
            

courses = [
    Course(
        title="How to become a better student",
        hours=58,
        lesson=12,
    ),
    Course(
        title="Create a Good Box",
        hours=43,
        lesson=2,
    ),
]

