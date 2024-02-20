from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Language(str, Enum):
    PY = "Python"
    JAVA = "Java"
    RUBY = "Ruby" 


class Comment(BaseModel):
    text: Optional[str] = None


class Blog(BaseModel):    
    title: str = Field(min_length=5)
    description: Optional[str] = None
    is_active: bool
    language: Language = Language.PY
    created_at: datetime = Field(default_factory=datetime.now)
    comments: Optional[List[Comment]] = []

b = Blog(title="My First Blog", is_active=True)
print(b)



from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    email: str
    password: str
    confirm_password: str
    
    
    @field_validator("email")
    @classmethod
    def valdiate_email(cls, value) -> str:
        if not "@" in value:
            raise ValueError("This email is not allowed")
        
        return value
    
    @model_validator(mode="after")
    def check_password(self) -> "User":
        
        if self.password != self.confirm_password:
            raise ValueError("The passwords should match")
        
        return self
    
u = User(email="jj@jj.com", password="123", confirm_password="123")
print(u)