from pydantic import BaseModel, Field,PositiveInt

#! Creamos el esquema de Libro
class Libro(BaseModel):
    id: PositiveInt|None=None 
    titulo: str = Field(..., min_length=1, max_length=100)
    autor: str = Field(..., min_length=1, max_length=50)
    isbn: str = Field(..., min_length=10, max_length=13)
    editorial: str = Field(..., min_length=1, max_length=50)
    disponible: bool = True
    categoria_id: PositiveInt

# class LibroCreate(LibroBase):
#     pass

# class LibroUpdate(LibroBase):
#     pass

# class Libro(LibroBase):
#     id: int

class Config:
    orm_mode = True
