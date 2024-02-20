from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.core.auth import get_logged_user
from backend.db.repository.blog import create_new_blog, delete_blog_by_id
from backend.db.repository.blog import get_all_blogs, get_blog_by_id
from backend.db.repository.blog import update_blog_by_id
from backend.db.session import get_db
from backend.schemas.blog import BlogCreate, BlogResponse


router = APIRouter()


@router.post("/", response_model=BlogResponse, status_code=status.HTTP_201_CREATED)
def crete_blog(blog: BlogCreate, db: Session = Depends(get_db), user = Depends(get_logged_user)):
    db_blog = create_new_blog(blog, db, user)
    return db_blog


@router.get("/{id}", response_model=BlogResponse)
def get_blog(id: int, db: Session = Depends(get_db)):
    db_blog = get_blog_by_id(id, db)

    if not db_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )

    return db_blog


@router.get("/", response_model=List[BlogResponse])
def get_blogs(db: Session = Depends(get_db)):
    return get_all_blogs(db)


@router.put("/{id}", response_model=BlogResponse)
def update_blog(id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    db_blog = get_blog_by_id(id, db)

    if not db_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )

    db_blog = update_blog_by_id(db_blog, blog, db)

    return db_blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    db_blog = get_blog_by_id(id, db)

    if not db_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found"
        )

    delete_blog_by_id(db_blog, db)
