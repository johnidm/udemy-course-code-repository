from core.config import settings, DBBaseModel
from sqlalchemy import Column, Integer, String


class CursoModel(DBBaseModel):
    __tablename__ = "cursoso"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)

