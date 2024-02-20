from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.base import api_router
from backend.app.base import app_router
from backend.db.models import Base
from backend.db.session import engine

from .core.config import settings


Base.metadata.create_all(engine)


app: FastAPI = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

app.include_router(api_router)
app.include_router(app_router)


@app.get("/")
def home():
    return f"{app.title} - {app.version}"
