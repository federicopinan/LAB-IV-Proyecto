from pydantic import BaseModel, Field

class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=50)
    descripcion: str = Field(None, max_length=255)

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int

    class Config:
        orm_mode = True
