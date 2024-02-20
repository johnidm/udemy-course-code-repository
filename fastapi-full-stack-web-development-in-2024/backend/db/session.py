from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings


engine = create_engine(settings.DB_URL, echo=True)

Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()
