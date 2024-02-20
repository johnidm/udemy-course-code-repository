from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    
    
class TokenUserResponse(BaseModel):
    id: int
    fullname: str
    email: str
    