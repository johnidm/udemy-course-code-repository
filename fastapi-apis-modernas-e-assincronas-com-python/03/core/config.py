from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL:str = "sqlite+aiosqlite:///database.db"
    
    class Config:
        case_sensitive = True
        

settings: Settings = Settings()
