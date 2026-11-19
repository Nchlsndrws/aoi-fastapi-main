from pydantic import BaseModel, ConfigDict

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
