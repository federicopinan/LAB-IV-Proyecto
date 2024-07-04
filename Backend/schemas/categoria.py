from pydantic import BaseModel, Field,PositiveInt

#! Creamos el esquema de Categoría
class Categoria(BaseModel):
    id: PositiveInt|None=None
    nombre: str = Field( min_length=1, max_length=50)
    descripcion: str = Field(None, max_length=255)

# class CategoriaCreate(CategoriaBase):
#     pass

# class CategoriaUpdate(CategoriaBase):
#     pass

# class Categoria(CategoriaBase):
    

class Config:
    orm_mode = True
