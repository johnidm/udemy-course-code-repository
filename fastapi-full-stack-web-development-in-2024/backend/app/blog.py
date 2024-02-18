from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from backend.db.repository.blog import get_blog_by_id, list_blogs
from backend.db.session import get_db


templates = Jinja2Templates(directory="backend/templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def read_item(request: Request, db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    context = {"request": request, "blogs": blogs}
    return templates.TemplateResponse("blog/home.html", context)


@router.get("/{id}", response_class=HTMLResponse)
def read_item(request: Request, id: int, db: Session = Depends(get_db)):
    blog = get_blog_by_id(id=id, db=db)
    context = {"request": request, "blog": blog}
    return templates.TemplateResponse("blog/detail.html", context)
