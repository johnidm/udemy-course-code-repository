from typing import List, Optional, Any
from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException, Response

from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.usuario import UsuarioModel
from schemas.usuario import (
    UsuarioSchema,
    UsuarioSchemaArtigos,
    UsuarioSchemaCreate,
    UsuarioSchemaUpdate,
)

from core.deps import get_session, get_current_user
from core.security import gerar_hash_senha
from core.auth import autenticar, criar_token_acesso

router = APIRouter()


@router.get("/logado", response_model=UsuarioSchema)
def get_logado(usuario_logado: UsuarioModel = Depends(get_current_user)):
    return usuario_logado


@router.post(
    "/signup", response_model=UsuarioSchema, status_code=status.HTTP_201_CREATED
)
async def post_usuario(
    usuario: UsuarioSchemaCreate, db: AsyncSession = Depends(get_session)
):
    novo_usuario: UsuarioModel = UsuarioModel(
        nome=usuario.nome,
        sobrenome=usuario.sobrenome,
        email=usuario.email,
        senha=gerar_hash_senha(usuario.senha),
        eh_admin=usuario.eh_admin,
    )

    async with db as session:
        session.add(novo_usuario)
        await db.commit()

        return novo_usuario


@router.get("/", response_model=List[UsuarioSchema])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuarioSchema] = result.scalars().unique().all()

        return usuarios


@router.get("/{id}", response_model=UsuarioSchemaArtigos)
async def get_usuario(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == id)
        result = await session.execute(query)
        usuario: UsuarioSchemaArtigos = result.scalars().unique().one_or_none()

        if not usuario:
            raise HTTPException(
                detail="Usuário não encontrado", status_code=status.HTTP_404_NOT_FOUND
            )

        return usuario


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_session),
):

    usuario = await autenticar(
        email=form_data.username, senha=form_data.password, db=db
    )

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(
        content={
            "access_token": criar_token_acesso(sub=usuario.id),
            "token_type": "bearer"
        }
    )
