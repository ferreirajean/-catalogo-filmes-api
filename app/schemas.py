from pydantic import BaseModel, ConfigDict, Field

class FilmeCreate(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    diretor: str = Field(min_length=1, max_length=100)
    ano: int = Field(ge=1888, le=2100)
    genero: str = Field(min_length=1, max_length=50)
    nota: float | None = Field(default=None, ge=0, le=10)


class FilmeResponse(FilmeCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int