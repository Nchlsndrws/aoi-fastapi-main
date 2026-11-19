from app.cadastros import crud, schemas
from app.planos import crud as planos_crud, schemas as planos_schemas
from app.modalidades import crud as modalidades_crud, schemas as modalidades_schemas

def _criar_plano(db):
    return planos_crud.criar_plano(db, planos_schemas.PlanoCreate(nome="Mensal", preco="99.90"))

def _criar_modalidade(db):
    return modalidades_crud.criar_modalidade(db, modalidades_schemas.ModalidadeCreate(nome="Musculação"))

def test_criar_e_buscar_cadastro(db):
    plano = _criar_plano(db)
    modalidade = _criar_modalidade(db)
    dados = schemas.CadastroCreate(
        nome="Teste",
        telefone="11999999999",
        plano_id=plano.id,
        modalidades_ids=[modalidade.id],
    )

    criado = crud.criar_cadastro(db, dados, [modalidade])

    assert criado.protocolo.startswith("FF-")
    assert crud.buscar_cadastro(db, criado.id) is not None

def test_buscar_cadastro_por_protocolo(db):
    plano = _criar_plano(db)
    dados = schemas.CadastroCreate(nome="Teste", telefone="11999999999", plano_id=plano.id)

    criado = crud.criar_cadastro(db, dados, [])

    encontrado = crud.buscar_cadastro_por_protocolo(db, criado.protocolo)

    assert encontrado is not None
    assert encontrado.id == criado.id

def test_listar_cadastros_ordem_mais_recente_primeiro(db):
    plano = _criar_plano(db)
    dados = schemas.CadastroCreate(nome="Primeiro", telefone="11999999999", plano_id=plano.id)
    dados2 = schemas.CadastroCreate(nome="Segundo", telefone="11999999998", plano_id=plano.id)

    crud.criar_cadastro(db, dados, [])
    crud.criar_cadastro(db, dados2, [])

    cadastros = crud.listar_cadastros(db)

    assert [c.nome for c in cadastros] == ["Segundo", "Primeiro"]

def test_deletar_cadastro(db):
    plano = _criar_plano(db)
    dados = schemas.CadastroCreate(nome="Teste", telefone="11999999999", plano_id=plano.id)
    criado = crud.criar_cadastro(db, dados, [])

    assert crud.deletar_cadastro(db, criado.id) is True
    assert crud.buscar_cadastro(db, criado.id) is None

def test_deletar_cadastro_inexistente_retorna_false(db):
    assert crud.deletar_cadastro(db, 999) is False

def test_plano_em_uso_apos_cadastro(db):
    plano = _criar_plano(db)
    dados = schemas.CadastroCreate(nome="Teste", telefone="11999999999", plano_id=plano.id)
    crud.criar_cadastro(db, dados, [])

    assert planos_crud.plano_em_uso(db, plano.id) is True

def test_modalidade_em_uso_apos_cadastro(db):
    plano = _criar_plano(db)
    modalidade = _criar_modalidade(db)
    dados = schemas.CadastroCreate(nome="Teste", telefone="11999999999", plano_id=plano.id)
    crud.criar_cadastro(db, dados, [modalidade])

    assert modalidades_crud.modalidade_em_uso(db, modalidade.id) is True
