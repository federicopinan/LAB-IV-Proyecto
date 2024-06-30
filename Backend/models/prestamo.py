from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Prestamo(Base):
    __tablename__ = "Prestamo"

    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey('Libro.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('Usuario.id'), nullable=False)
    fecha_prestamo = Column(DateTime, nullable=False)
    fecha_devolucion = Column(DateTime, nullable=True)

    usuario = relationship("Usuario", back_populates="Prestamo")
    libro = relationship("Libro", back_populates="Prestamo")
