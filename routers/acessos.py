from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(prefix="/acessos", tags=["Acessos"])

@router.post("/validar", response_model=schemas.AcessoResposta)
def validar(dados: schemas.AcessoValidar, db: Session = Depends(get_db)):
    liberado, motivo, nome = crud.validar_acesso(db, dados.protocolo)
    return schemas.AcessoResposta(liberado=liberado, motivo=motivo, nome=nome)

@router.get("/", response_model=list[schemas.AcessoOut])
def listar(db: Session = Depends(get_db)):
    return crud.listar_acessos(db)