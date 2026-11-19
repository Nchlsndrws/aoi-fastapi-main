from decimal import Decimal
from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime

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

class ModalidadeBase(BaseModel):
    nome: str
    descricao: str | None = None

class ModalidadeCreate(ModalidadeBase):
    pass

class ModalidadeUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None

class ModalidadeOut(ModalidadeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class CadastroCreate(BaseModel):
    nome: str
    telefone: str
    email: str | None = None
    objetivo: str | None = None
    observacoes: str | None = None
    plano_id: int
    modalidades_ids: list[int] = []

    @field_validator("telefone")
    @classmethod
    def validar_telefone(cls, valor: str):
        digitos = "".join(c for c in valor if c.isdigit())
        if len(digitos) not in (10, 11):
            raise ValueError("Telefone inválido: informe DDD + número (10 ou 11 dígitos)")
        return digitos

class CadastroOut(BaseModel):
    id: int
    protocolo: str
    nome: str
    telefone: str
    email: str | None
    objetivo: str | None
    observacoes: str | None
    criado_em: datetime
    plano: PlanoOut
    modalidades: list[ModalidadeOut]

    model_config = ConfigDict(from_attributes=True)