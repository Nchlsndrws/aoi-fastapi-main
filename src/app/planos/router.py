from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.planos import crud, schemas

router = APIRouter(prefix="/planos", tags=["Planos"])

@router.post("/", response_model=schemas.PlanoOut)
def criar(plano: schemas.PlanoCreate, db: Session = Depends(get_db)):
    return crud.criar_plano(db, plano)

@router.get("/", response_model=list[schemas.PlanoOut])
def listar(db: Session = Depends(get_db)):
    return crud.listar_planos(db)

@router.get("/{plano_id}", response_model=schemas.PlanoOut)
def buscar(plano_id: int, db: Session = Depends(get_db)):
    plano = crud.buscar_plano(db, plano_id)
    if plano is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return plano

@router.patch("/{plano_id}", response_model=schemas.PlanoOut)
def atualizar(plano_id: int, dados: schemas.PlanoUpdate, db: Session = Depends(get_db)):
    plano = crud.atualizar_plano(db, plano_id, dados)
    if plano is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    return plano

@router.delete("/{plano_id}", status_code=204)
def deletar(plano_id: int, db: Session = Depends(get_db)):
    if crud.buscar_plano(db, plano_id) is None:
        raise HTTPException(status_code=404, detail="Plano não encontrado")
    if crud.plano_em_uso(db, plano_id):
        raise HTTPException(status_code=409, detail="Plano em uso por cadastros e não pode ser apagado")
    crud.deletar_plano(db, plano_id)
