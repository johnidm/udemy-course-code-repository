from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from typing import List
from models.curso import CursoModel
from schema.curso import CursoSchema
from fastapi import HTTPException
from core.deps import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


router = APIRouter()


@router.get("/", response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)

        cursos: List[CursoSchema] = result.scalars().all()

        return cursos


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def create_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
    db.add(novo_curso)

    await db.commit()
    return novo_curso


@router.get("/{id}", response_model=CursoSchema)
async def get_cursos(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == id)
        result = await session.execute(query)

        curso: CursoSchema = result.scalar_one_or_none()

        if not curso:
            raise HTTPException(
                detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )

        return curso


@router.put("/{id}", response_model=CursoSchema)
async def update_course(
    id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)
):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == id)
        result = await session.execute(query)

        curso_db: CursoSchema = result.scalar_one_or_none()

        if not curso_db:
            raise HTTPException(
                detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )

        curso_db.titulo = curso.titulo
        curso_db.aulas = curso.aulas
        curso_db.horas = curso.horas

        await session.commit()

        return curso


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_course(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == id)
        result = await session.execute(query)

        curso: CursoSchema = result.scalar_one_or_none()

        if not curso:
            raise HTTPException(
                detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )

        await session.delete(curso)
        await session.commit()

        return curso
