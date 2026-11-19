from sqlalchemy.orm import Session
import secrets
from datetime import datetime
import models
import schemas

def criar_plano(db: Session, plano: schemas.PlanoCreate):
    novo = models.Plano(**plano.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_planos(db: Session):
    return db.query(models.Plano).all()

def buscar_plano(db: Session, plano_id: int):
    return db.query(models.Plano).filter(models.Plano.id == plano_id).first()

def atualizar_plano(db: Session, plano_id: int, dados: schemas.PlanoUpdate):
    plano = buscar_plano(db, plano_id)
    if plano is None:
        return None
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(plano, campo, valor)
    db.commit()
    db.refresh(plano)
    return plano

def deletar_plano(db: Session, plano_id: int):
    plano = buscar_plano(db, plano_id)
    if plano is None:
        return False
    db.delete(plano)
    db.commit()
    return True

def criar_modalidade(db: Session, modalidade: schemas.ModalidadeCreate):
    nova = models.Modalidade(**modalidade.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_modalidades(db: Session):
    return db.query(models.Modalidade).all()

def buscar_modalidade(db: Session, modalidade_id: int):
    return db.query(models.Modalidade).filter(models.Modalidade.id == modalidade_id).first()

def atualizar_modalidade(db: Session, modalidade_id: int, dados: schemas.ModalidadeUpdate):
    modalidade = buscar_modalidade(db, modalidade_id)
    if modalidade is None:
        return None
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(modalidade, campo, valor)
    db.commit()
    db.refresh(modalidade)
    return modalidade

def deletar_modalidade(db: Session, modalidade_id: int):
    modalidade = buscar_modalidade(db, modalidade_id)
    if modalidade is None:
        return False
    db.delete(modalidade)
    db.commit()
    return True

def gerar_protocolo():
    return f"FF-{datetime.now():%Y%m%d}-{secrets.token_hex(3).upper()}"

def buscar_modalidades_por_ids(db: Session, ids: list[int]):
    if not ids:
        return []
    return db.query(models.Modalidade).filter(models.Modalidade.id.in_(ids)).all()

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

def plano_em_uso(db: Session, plano_id: int):
    return db.query(models.Cadastro).filter(models.Cadastro.plano_id == plano_id).first() is not None

def modalidade_em_uso(db: Session, modalidade_id: int):
    return (
        db.query(models.Cadastro)
        .filter(models.Cadastro.modalidades.any(models.Modalidade.id == modalidade_id))
        .first()
        is not None
    )