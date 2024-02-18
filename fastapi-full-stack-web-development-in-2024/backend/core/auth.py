from datetime import timedelta, datetime
from typing import Annotated
from fastapi import Cookie, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pytest import Session
from backend.core.config import settings
from backend.db.models import User
from backend.db.repository.user import get_user_by_email
from backend.db.session import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


def create_access_token(db_user: User) -> str:
    expires_delta = timedelta(minutes=settings.JWT_EXPIRE_MINUTES) + datetime.utcnow()

    token_data = {
        "uid": db_user.id,
        "ufn": db_user.fullname,
        "sub": db_user.email,
        "exp": expires_delta,
    }

    return jwt.encode(
        token_data,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

# 
def get_token_payload(access_token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    payload = jwt.decode(
        access_token.encode(), settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
    )
    return payload


def get_logged_user(
    payload: Annotated[dict, Depends(get_token_payload)], db: Session = Depends(get_db)
) -> User:
    email: str = payload.get("sub")
    db_user = get_user_by_email(email, db)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return db_user


