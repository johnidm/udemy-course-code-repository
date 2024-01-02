from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


DBBaseModel = declarative_base()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "sqlite+aiosqlite:///.database.sqlite"
        # ////absolute/path/to/file.db
    JWT_SECRET: str = "1234qwer"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings = Settings()
