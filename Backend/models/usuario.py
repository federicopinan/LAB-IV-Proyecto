from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from enum import Enum as PyEnum

# class RolEnum(PyEnum):
#     bibliotecario = "Bibliotecario"
#     cliente = "Cliente"

class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30), nullable=False)
    email = Column(String(30), unique=True, index=True, nullable=False)
    contrasena = Column(String(30), nullable=False)
    rol = Column(Enum("Bibliotecario","Cliente"), nullable=False)

    # prestamos = relationship("Prestamo", back_populates="usuario")
