from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from enum import Enum as PyEnum

class RolEnum(PyEnum):
    bibliotecario = "Bibliotecario"
    cliente = "Cliente"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    contrasena = Column(String, nullable=False)
    rol = Column(Enum(RolEnum), nullable=False)

    prestamos = relationship("Prestamo", back_populates="usuario")
