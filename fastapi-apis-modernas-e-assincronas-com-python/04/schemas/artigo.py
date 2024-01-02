from typing import Optional

from pydantic import BaseModel as SCBaseModel, HttpUrl


class ArtigoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    url_fonte: HttpUrl
    descricao: str
    usuario_id: Optional[int]

    class Config:
        from_attributes = True
