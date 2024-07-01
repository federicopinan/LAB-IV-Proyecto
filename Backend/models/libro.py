from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from config.database import Base

#! Creamos el ORM de Libro
class Libro(Base):
    __tablename__ = "Libro"

    id = Column(Integer,autoincrement=True, primary_key=True)  
    titulo = Column(String(30), nullable=False)
    autor = Column(String(30), nullable=False)
    isbn = Column(String(30), unique=True, nullable=False)
    editorial = Column(String(30), nullable=False)
    disponible = Column(Boolean,default=True)
    categoria_id = Column(Integer, ForeignKey('Categoria.id'), nullable=False)

    # categoria = relationship("Categoria", back_populates="Libro")
    # prestamos = relationship("Prestamo", back_populates="Libro")
