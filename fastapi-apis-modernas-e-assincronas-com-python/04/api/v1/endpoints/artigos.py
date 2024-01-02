from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.artigo import ArtigoModel
from models.usuario import UsuarioModel

from schemas.artigo import ArtigoSchema
from core.deps import get_session, get_current_user

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ArtigoSchema)
async def post_artigo(
    artigo: ArtigoSchema,
    usuario_logado: UsuarioModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    novo_artigo: ArtigoModel = ArtigoModel(
        titulo=artigo.titulo,
        descricao=artigo.descricao,
        url_fonte=artigo.url_fonte,
        usuario_id=artigo.usuario_id,
    )

    db.add(novo_artigo)
    db.commit()

    return novo_artigo


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ArtigoSchema])
async def get_artigos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel)

        result = await session.execute(query)

        artigos: List[ArtigoModel] = result.scalars().unique().all()

        return artigos


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ArtigoSchema)
async def get_artigos(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel).filter(ArtigoModel.id == id)

        result = await session.execute(query)

        artigo: ArtigoModel = result.scalars().unique().one_or_none()

        if not artigo:
            raise HTTPException(
                detail="Artigo não encontrado", status_code=status.HTTP_404_NOT_FOUND
            )

        return artigo
