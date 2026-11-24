from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Table, Boolean, Date
from sqlalchemy.orm import relationship
from database import Base

class Plano(Base):
    __tablename__ = "planos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False, unique=True)
    descricao = Column(String(255))
    preco = Column(Numeric(8,2), nullable=False)
    duracao_dias = Column(Integer, default=30, nullable=False)

class Modalidade(Base):
    __tablename__ = "modalidades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False, unique=True)
    descricao = Column(String(255))

cadastro_modalidade = Table(
    "cadastro_modalidade",
    Base.metadata,
    Column("cadastro_id", ForeignKey("cadastros.id"), primary_key=True),
    Column("modalidade_id", ForeignKey("modalidades.id"), primary_key=True),
)

class Cadastro(Base):
    __tablename__ = "cadastros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(120))
    objetivo = Column(String(255))
    observacoes = Column(String(500))
    protocolo = Column(String(20), unique=True, nullable=False)
    criado_em = Column(DateTime, default=datetime.now)
    ativo = Column(Boolean, default=False, nullable=False)
    data_validade = Column(Date)

    plano_id = Column(Integer, ForeignKey("planos.id"), nullable=False)
    plano = relationship("Plano")
    modalidades = relationship("Modalidade", secondary=cadastro_modalidade)

class Acesso(Base):
    __tablename__ = "acessos"

    id = Column(Integer, primary_key=True, index=True)
    protocolo = Column(String(20), nullable=False)
    liberado = Column(Boolean, nullable=False)
    motivo = Column(String(120), nullable=False)
    data_hora = Column(DateTime, default=datetime.now)
    cadastro_id = Column(Integer, ForeignKey("cadastros.id"))