from sqlalchemy import Column, Integer, String
from app.database import Base

class Modalidade(Base):
    __tablename__ = "modalidades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False, unique=True)
    descricao = Column(String(255))
