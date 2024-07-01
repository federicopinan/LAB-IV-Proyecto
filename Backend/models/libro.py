from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Libro(Base):
    __tablename__ = "Libro"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(30), nullable=False)
    autor = Column(String(30), nullable=False)
    isbn = Column(String(30), unique=True, nullable=False)
    editorial = Column(String(30), nullable=False)
    categoria_id = Column(Integer, ForeignKey('Categoria.id'), nullable=False)

    categoria = relationship("Categoria", back_populates="Libro")
    prestamos = relationship("Prestamo", back_populates="Libro")
