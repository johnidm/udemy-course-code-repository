import datetime
from typing import List

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


Base = declarative_base()


class ModelMixin:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class Blog(Base, ModelMixin):
    __tablename__ = "blog"

    title: Mapped[str] = mapped_column(String(80), nullable=False)
    slug: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="blogs")

    def __repr__(self) -> str:
        return f"Blog(id={self.id!r}, name={self.title!r})"


class User(Base, ModelMixin):
    __tablename__ = "user"

    fullname: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)

    blogs: Mapped[List["Blog"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.fullname!r})"
