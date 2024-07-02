from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from config.database import Base
from enum import Enum as PyEnum

#! Creamos el ORM de Usuario
# class RolEnum(PyEnum):
#     bibliotecario = "Bibliotecario"
#     cliente = "Cliente"

class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer,autoincrement=True, primary_key=True)
    nombre = Column(String(30), nullable=False)
    email = Column(String(30), unique=True, index=True, nullable=False)
    password = Column(String(128), nullable=False)
    rol = Column(Enum("Bibliotecario","Cliente"), nullable=False)

    # prestamos = relationship("Prestamo", back_populates="usuario")
