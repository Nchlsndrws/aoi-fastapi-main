from decimal import Decimal
from pydantic import BaseModel, ConfigDict

class PlanoBase(BaseModel):
    nome: str
    descricao: str | None = None
    preco: Decimal

class PlanoCreate(PlanoBase):
    pass

class PlanoOut(PlanoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class PlanoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    preco: Decimal | None = None
