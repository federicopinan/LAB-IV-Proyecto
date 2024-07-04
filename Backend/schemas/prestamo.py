from pydantic import BaseModel, Field,PositiveInt
from datetime import datetime

#! Creamos el esquema de Prestamo
class Prestamo(BaseModel):
    id: PositiveInt|None=None
    libro_id: PositiveInt
    usuario_id: PositiveInt
    fecha_prestamo: datetime
    fecha_devolucion: datetime = None

# class PrestamoCreate(PrestamoBase):
#     pass

# class PrestamoUpdate(BaseModel):
#     fecha_devolucion: datetime = None

# class Prestamo(PrestamoBase):
#     id: int
#     fecha_devolucion: datetime = None

class Config:
    orm_mode = True
