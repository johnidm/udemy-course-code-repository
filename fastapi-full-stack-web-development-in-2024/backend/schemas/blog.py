from datetime import datetime

from pydantic import BaseModel


class BlogResponse(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    created_at: datetime


class BlogCreate(BaseModel):
    title: str
    content: str


class BlogUpdate(BlogCreate):
    ...
