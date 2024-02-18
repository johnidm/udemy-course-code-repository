from fastapi import APIRouter
from backend.api.v1 import user, blog, auth

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/api/v1/auth", tags="auth")
api_router.include_router(user.router, prefix="/api/v1/user", tags="user")
api_router.include_router(blog.router, prefix="/api/v1/blog", tags="blog")

