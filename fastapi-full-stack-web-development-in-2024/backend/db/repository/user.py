from typing import List

from sqlalchemy.orm import Session

from backend.core.hashing import get_password_hash
from backend.db.models import User
from backend.schemas.user import UserCreate


#  new_user = models.User(**payload.dict())


def create_new_user(user: UserCreate, db: Session) -> User:
    hash_password = get_password_hash(user.password)

    db_user = User(fullname=user.fullname, email=user.email, password=hash_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(email: str, db: Session) -> User:
    db_user = db.query(User).filter(User.email == email).first()
    return db_user


def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()
