# 🎬 Catálogo de Filmes API

API REST para cadastrar, consultar, atualizar e remover filmes, construída com **FastAPI**, **SQLAlchemy** e **SQLite**.

> Projeto de portfólio para praticar os fundamentos de desenvolvimento web com Python: rotas, validação de dados, banco de dados e testes automatizados.

## 📸 Documentação interativa

![Documentação Swagger](docs/swagger.png)

## ✨ Funcionalidades

- CRUD completo de filmes
- Validação automática dos dados (ex.: nota entre 0 e 10)
- Filtro por gênero e paginação
- Documentação interativa gerada automaticamente (Swagger)
- Testes automatizados com Pytest

## 🛠️ Tecnologias

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- SQLite
- Pytest

## 🚀 Como rodar

```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/catalogo-filmes-api.git
cd catalogo-filmes-api

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor
uvicorn app.main:app --reload
```

Acesse a documentação interativa em **http://127.0.0.1:8000/docs**.

## 📌 Endpoints

| Método | Rota             | Descrição                              |
|--------|------------------|----------------------------------------|
| GET    | `/`              | Verifica se a API está no ar           |
| POST   | `/filmes`        | Cadastra um filme                      |
| GET    | `/filmes`        | Lista filmes (`genero`, `skip`, `limit`) |
| GET    | `/filmes/{id}`   | Busca um filme pelo id                 |
| PUT    | `/filmes/{id}`   | Atualiza um filme                      |
| DELETE | `/filmes/{id}`   | Remove um filme                        |

### Exemplo

```bash
curl -X POST http://127.0.0.1:8000/filmes \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Cidade de Deus", "diretor": "Fernando Meirelles", "ano": 2002, "genero": "Drama", "nota": 8.6}'
```

## 🧪 Testes

```bash
pytest
```

## 📁 Estrutura

```
├── app/
│   ├── main.py       # rotas da API
│   ├── models.py     # tabelas do banco
│   ├── schemas.py    # validação dos dados
│   └── database.py   # conexão com o banco
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
```

## 🔮 Próximos passos

- [ ] Autenticação com JWT
- [ ] Migrações com Alembic
- [ ] Trocar SQLite por PostgreSQL
- [ ] Deploy (Render/Railway)
- [ ] Dockerfile

## 👤 Autor

Feito por **SEU NOME** — [LinkedIn](https://linkedin.com/in/seu-perfil) · [GitHub](https://github.com/SEU-USUARIO)
