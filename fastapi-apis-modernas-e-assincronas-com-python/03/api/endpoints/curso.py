from core.deps import get_session
from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from models.curso import CursoModel

from typing import List


router = APIRouter()

@router.post("/courses", status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def create_curso(curso: CursoModel, db: AsyncSession = Depends(get_session)):
    db.add(curso)

    await db.commit()
    return curso


@router.get("/courses", response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)

        cursos: List[CursoModel] = result.scalars().all()

        return cursos