from typing import List
from backend.db.models import Blog, User
from sqlalchemy.orm import Session
from backend.schemas.blog import BlogCreate, BlogUpdate
import secrets
from slugify import slugify


def generate_slug(title: str) -> str:
    token = secrets.token_urlsafe(16)
    slug = f"{slugify(title)}-{token}"

    return slug


def list_blogs(db: Session):
    return db.query(Blog).all()


def create_new_blog(blog: BlogCreate, db: Session, user):
    db_blog = Blog(title=blog.title, content=blog.content)
    db_blog.user_id = user.id

    db_blog.slug = generate_slug(blog.title)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def update_blog_by_id(db_blog: User, blog: BlogUpdate, db: Session):
    db_blog.title = blog.title
    db_blog.content = blog.content

    db_blog.slug = generate_slug(blog.title)

    db_blog.user_id = 1

    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)

    return db_blog


def get_all_blogs(db: Session) -> List[Blog]:
    return db.query(Blog).all()


def get_blog_by_id(id: int, db: Session) -> Blog:
    return db.query(Blog).filter(Blog.id == id).first()


def delete_blog_by_id(db_blog: User, db: Session) -> None:
    db.delete(db_blog)
    db.commit()
