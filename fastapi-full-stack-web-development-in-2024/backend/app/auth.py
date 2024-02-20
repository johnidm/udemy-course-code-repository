from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.core.auth import create_access_token
from backend.db.repository.user import create_new_user
from backend.db.session import get_db
from backend.schemas.user import UserCreate


templates = Jinja2Templates(directory="backend/templates")

router = APIRouter()


@router.get("/register", response_class=HTMLResponse)
def read_item(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("auth/register.html", context)


@router.post("/register", response_class=HTMLResponse)
def create_item(
    request: Request,
    fullname: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = UserCreate(fullname=fullname, email=username, password=password)
    db_user = create_new_user(user, db)

    response = RedirectResponse("/app", status_code=status.HTTP_302_FOUND)

    access_token = create_access_token(db_user)

    response.set_cookie(key="Authorization", value=f"Bearer {access_token}")
    return response
