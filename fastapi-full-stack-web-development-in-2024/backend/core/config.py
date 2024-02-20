import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    PROJECT_TITLE: str = "My Blog 🚀"
    PROJECT_VERSION: str = "1.0.0"
    DB_URL: str = os.getenv("DB_URL")
    
    JWT_ALGORITHM = "HS256"
    JWT_SECRET_KEY = "4f1feeca525de4cdb064656007da3edac7895a87ff0ea865693300fb8b6e8f9c"
    JWT_EXPIRE_MINUTES = 30



settings: Settings = Settings()
