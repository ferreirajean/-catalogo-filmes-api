import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

engine_teste = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SessionTeste = sessionmaker(bind=engine_teste, autoflush=False, autocommit=False)


def get_db_teste():
    db = SessionTeste()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = get_db_teste

client = TestClient(app)


@pytest.fixture(autouse=True)
def banco_limpo():
    Base.metadata.drop_all(bind=engine_teste)
    Base.metadata.create_all(bind=engine_teste)

FILME_EXEMPLO = {
    "titulo": "Cidade de Deus",
    "diretor": "Fernando Meirelles",
    "ano": 2002,
    "genero": "Drama",
    "nota": 8.6,
}


def test_criar_filme():
    resposta = client.post("/filmes", json=FILME_EXEMPLO)
    assert resposta.status_code == 201
    assert resposta.json()["id"] == 1
    assert resposta.json()["titulo"] == "Cidade de Deus"


def test_listar_filmes():
    client.post("/filmes", json=FILME_EXEMPLO)
    resposta = client.get("/filmes")
    assert resposta.status_code == 200
    assert len(resposta.json()) == 1

def test_obter_filme_inexistente():
    resposta = client.get("/filmes/999")
    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Filme não encontrado"


def test_nota_invalida():
    resposta = client.post("/filmes", json={**FILME_EXEMPLO, "nota": 15})
    assert resposta.status_code == 422
    assert client.get("/filmes").json() == []


def test_remover_filme():
    client.post("/filmes", json=FILME_EXEMPLO)
    resposta = client.delete("/filmes/1")
    assert resposta.status_code == 204
    assert client.get("/filmes/1").status_code == 404

