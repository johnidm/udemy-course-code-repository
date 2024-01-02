from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.config import settings, DBBaseModel


class UsuarioModel(DBBaseModel):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True, index=True, unique=True)
    email = Column(String(256), nullable=True)
    senha = Column(String(256), nullable=False)
    eh_admin = Column(Boolean, nullable=False)

    artigos = relationship(
        "ArtigoModel",
        cascade="all, delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined",
    )
    
    
