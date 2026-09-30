from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models
from app.database import Base, engine, get_db
from app.schemas import FilmeCreate, FilmeResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Catálogo de Filmes API")

def buscar_filme_ou_404(db: Session, filme_id: int) -> models.Filme:
    filme = db.get(models.Filme, filme_id)
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

filmes: list[dict] = []
proximo_id = 1


@app.get("/")
def raiz():
    return {"mensagem": "Minha primeira API está no ar!"}


@app.post("/filmes", response_model=FilmeResponse, status_code=201)
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):
    novo_filme = models.Filme(**filme.model_dump())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme


@app.get("/filmes", response_model=list[FilmeResponse])
def listar_filmes(
    genero: str | None = Query(default=None, description="Filtra por gênero"),
    skip: int = Query(default=0, ge=0, description="Quantos filmes pular"),
    limit: int = Query(default=10, ge=1, le=100, description="Máximo de filmes"),
    db: Session = Depends(get_db),
):
    consulta = select(models.Filme)
    if genero:
        consulta = consulta.where(models.Filme.genero.ilike(genero))
    consulta = consulta.offset(skip).limit(limit)
    return db.scalars(consulta).all()

@app.get("/filmes/{filme_id}", response_model=FilmeResponse)
def obter_filme(filme_id: int, db: Session = Depends(get_db)):
    return buscar_filme_ou_404(db, filme_id)

@app.put("/filmes/{filme_id}", response_model=FilmeResponse)
def atualizar_filme(
        filme_id: int, dados: FilmeCreate, db: Session = Depends(get_db)
):
    filme = buscar_filme_ou_404(db, filme_id)
    for campo, valor in dados.model_dump().items():
        setattr(filme, campo, valor)
    db.commit()
    db.refresh(filme)
    return filme

@app.delete("/filmes/{filme_id}", status_code=204)
def remover_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = buscar_filme_ou_404(db, filme_id)
    db.delete(filme)
    db.commit()