from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from backend.db.repository.user import create_new_user, get_user_by_email, get_all_users
from backend.db.session import get_db
from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate, UserResposne


router = APIRouter()


@router.post("/", response_model=UserResposne, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(user.email, db)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        )

    db_user = create_new_user(user, db)
    return db_user


@router.get("/", response_model=List[UserResposne])
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)
