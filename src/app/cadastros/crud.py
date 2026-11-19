import secrets
from datetime import datetime
from sqlalchemy.orm import Session

from app.cadastros import models, schemas

def gerar_protocolo():
    return f"FF-{datetime.now():%Y%m%d}-{secrets.token_hex(3).upper()}"

def criar_cadastro(db: Session, dados: schemas.CadastroCreate, modalidades: list):
    novo = models.Cadastro(
        nome=dados.nome,
        telefone=dados.telefone,
        email=dados.email,
        objetivo=dados.objetivo,
        observacoes=dados.observacoes,
        plano_id=dados.plano_id,
        protocolo=gerar_protocolo(),
        modalidades=modalidades,
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_cadastros(db: Session):
    return db.query(models.Cadastro).order_by(models.Cadastro.id.desc()).all()

def buscar_cadastro(db: Session, cadastro_id: int):
    return db.query(models.Cadastro).filter(models.Cadastro.id == cadastro_id).first()

def buscar_cadastro_por_protocolo(db: Session, protocolo: str):
    return db.query(models.Cadastro).filter(models.Cadastro.protocolo == protocolo).first()

def deletar_cadastro(db: Session, cadastro_id: int):
    cadastro = buscar_cadastro(db, cadastro_id)
    if cadastro is None:
        return False
    db.delete(cadastro)
    db.commit()
    return True
