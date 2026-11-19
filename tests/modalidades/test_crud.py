from app.modalidades import crud, schemas

def test_criar_e_buscar_modalidade(db):
    criada = crud.criar_modalidade(db, schemas.ModalidadeCreate(nome="Musculação"))

    encontrada = crud.buscar_modalidade(db, criada.id)

    assert encontrada is not None
    assert encontrada.nome == "Musculação"

def test_listar_modalidades(db):
    crud.criar_modalidade(db, schemas.ModalidadeCreate(nome="Musculação"))
    crud.criar_modalidade(db, schemas.ModalidadeCreate(nome="Natação"))

    modalidades = crud.listar_modalidades(db)

    assert len(modalidades) == 2

def test_atualizar_modalidade(db):
    criada = crud.criar_modalidade(db, schemas.ModalidadeCreate(nome="Musculação"))

    atualizada = crud.atualizar_modalidade(db, criada.id, schemas.ModalidadeUpdate(descricao="Sala de peso"))

    assert atualizada.descricao == "Sala de peso"

def test_atualizar_modalidade_inexistente_retorna_none(db):
    resultado = crud.atualizar_modalidade(db, 999, schemas.ModalidadeUpdate(descricao="X"))

    assert resultado is None

def test_deletar_modalidade(db):
    criada = crud.criar_modalidade(db, schemas.ModalidadeCreate(nome="Musculação"))

    assert crud.deletar_modalidade(db, criada.id) is True
    assert crud.buscar_modalidade(db, criada.id) is None

def test_deletar_modalidade_inexistente_retorna_false(db):
    assert crud.deletar_modalidade(db, 999) is False

def test_buscar_modalidades_por_ids(db):
    m1 = crud.criar_modalidade(db, schemas.ModalidadeCreate(nome="Musculação"))
    crud.criar_modalidade(db, schemas.ModalidadeCreate(nome="Natação"))

    encontradas = crud.buscar_modalidades_por_ids(db, [m1.id])

    assert len(encontradas) == 1
    assert encontradas[0].id == m1.id

def test_buscar_modalidades_por_ids_vazio_retorna_lista_vazia(db):
    assert crud.buscar_modalidades_por_ids(db, []) == []

def test_modalidade_nao_em_uso(db):
    criada = crud.criar_modalidade(db, schemas.ModalidadeCreate(nome="Musculação"))

    assert crud.modalidade_em_uso(db, criada.id) is False
