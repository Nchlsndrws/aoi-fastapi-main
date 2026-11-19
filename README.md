# API do Projeto FitFlow

API desenvolvida com **FastAPI** para gerenciamento de planos, modalidades e cadastros de alunos.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Funcionalidades

### Planos
- Criar planos
- Listar planos
- Buscar plano por ID
- Atualizar planos
- Excluir planos

### Modalidades
- Criar modalidades
- Listar modalidades
- Buscar modalidade por ID
- Atualizar modalidades
- Excluir modalidades

### Cadastros
- Criar cadastros de alunos
- Listar cadastros
- Buscar cadastro por ID
- Buscar cadastro por protocolo
- Excluir cadastros

## Estrutura do projeto

```text
api-fastapi/
│
├── requirements.txt
├── .gitignore
│
└── src/
    └── app/
        ├── main.py
        ├── database.py
        │
        ├── planos/
        │   ├── models.py
        │   ├── schemas.py
        │   ├── crud.py
        │   └── router.py
        │
        ├── modalidades/
        │   ├── models.py
        │   ├── schemas.py
        │   ├── crud.py
        │   └── router.py
        │
        └── cadastros/
            ├── models.py
            ├── schemas.py
            ├── crud.py
            └── router.py
```

Cada domínio (`planos`, `modalidades`, `cadastros`) concentra seus próprios modelos, schemas, regras de negócio (`crud.py`) e rotas, em vez de compartilhar um único arquivo com as outras entidades.

## Como executar o projeto

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Iniciar a API

```bash
uvicorn app.main:app --app-dir src --reload
```

### 3. Acessar a documentação

Com o servidor em execução, acesse:

```text
http://127.0.0.1:8000/docs
```

A documentação interativa permite visualizar e testar os endpoints da API.

## Banco de dados

O projeto utiliza SQLite com SQLAlchemy para gerenciamento dos dados. O banco `fitflow.db` é criado automaticamente quando a aplicação é iniciada.
