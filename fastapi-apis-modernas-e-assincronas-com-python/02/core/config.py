from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


DBBaseModel = declarative_base()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # DB_URL: str = "postgres+asyncpg://geek:university@localhost:5432/faculdade"
    DB_URL:str = "sqlite+aiosqlite:///database.sqlite"
    

    class Config:
        case_sensitive = True


settings = Settings()
