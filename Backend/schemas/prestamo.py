from pydantic import BaseModel, Field
from datetime import datetime

class PrestamoBase(BaseModel):
    libro_id: int
    usuario_id: int
    fecha_prestamo: datetime

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoUpdate(BaseModel):
    fecha_devolucion: datetime = None

class Prestamo(PrestamoBase):
    id: int
    fecha_devolucion: datetime = None

class Config:
    orm_mode = True
