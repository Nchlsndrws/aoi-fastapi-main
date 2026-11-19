from decimal import Decimal

from app.planos import crud, schemas

def test_criar_e_buscar_plano(db):
    criado = crud.criar_plano(db, schemas.PlanoCreate(nome="Mensal", preco="99.90"))

    encontrado = crud.buscar_plano(db, criado.id)

    assert encontrado is not None
    assert encontrado.nome == "Mensal"

def test_listar_planos(db):
    crud.criar_plano(db, schemas.PlanoCreate(nome="Mensal", preco="99.90"))
    crud.criar_plano(db, schemas.PlanoCreate(nome="Anual", preco="899.90"))

    planos = crud.listar_planos(db)

    assert len(planos) == 2

def test_atualizar_plano(db):
    criado = crud.criar_plano(db, schemas.PlanoCreate(nome="Mensal", preco="99.90"))

    atualizado = crud.atualizar_plano(db, criado.id, schemas.PlanoUpdate(preco="79.90"))

    assert atualizado.preco == Decimal("79.90")

def test_atualizar_plano_inexistente_retorna_none(db):
    resultado = crud.atualizar_plano(db, 999, schemas.PlanoUpdate(preco="79.90"))

    assert resultado is None

def test_deletar_plano(db):
    criado = crud.criar_plano(db, schemas.PlanoCreate(nome="Mensal", preco="99.90"))

    assert crud.deletar_plano(db, criado.id) is True
    assert crud.buscar_plano(db, criado.id) is None

def test_deletar_plano_inexistente_retorna_false(db):
    assert crud.deletar_plano(db, 999) is False

def test_plano_nao_em_uso(db):
    criado = crud.criar_plano(db, schemas.PlanoCreate(nome="Mensal", preco="99.90"))

    assert crud.plano_em_uso(db, criado.id) is False
