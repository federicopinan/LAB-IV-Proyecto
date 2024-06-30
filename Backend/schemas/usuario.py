from pydantic import BaseModel, EmailStr, Field, validator
from enum import Enum

class RolEnum(str, Enum):
    bibliotecario = "Bibliotecario"
    cliente = "Cliente"

class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=50)
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    contrasena: str = Field(..., min_length=6, max_length=100)
    rol: RolEnum

    @validator('rol')
    def validate_rol(cls, v):
        if v not in RolEnum:
            raise ValueError('El rol debe ser Bibliotecario o Cliente')
        return v

class UsuarioUpdate(UsuarioBase):
    contrasena: str = Field(None, min_length=6, max_length=100)
    rol: RolEnum

class Usuario(UsuarioBase):
    id: int
    rol: RolEnum

class Config:
    orm_mode = True
