from typing import Optional, List

from pydantic import BaseModel as SCBaseModel, EmailStr
from schemas.artigo import ArtigoSchema

class UsuarioSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        from_attributes = True


class UsuarioSchemaCreate(UsuarioSchema):
    senha: str


class UsuarioSchemaArtigos(UsuarioSchema):
    artigos: Optional[List[ArtigoSchema]]


class UsuarioSchemaUpdate(UsuarioSchema):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]
