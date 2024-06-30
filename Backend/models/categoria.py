from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Categoria(Base):
    __tablename__ = "Categoria"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30), unique=True, nullable=False)
    descripcion = Column(String(30), nullable=True)

    libros = relationship("Libro", back_populates="Categoria")