from fastapi import APIRouter

from backend.app import auth, blog


app_router = APIRouter()

app_router.include_router(blog.router, prefix="/app", tags="app")
app_router.include_router(auth.router, prefix="/app/auth", tags="app_auth")
