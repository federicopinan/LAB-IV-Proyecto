from sqlalchemy import Column, Integer, String, DECIMAL,Enum,ForeignKey,DateTime
from database import Base

class loanModel(Base):
    id=Column(Integer, primary_key=True,autoincrement=True)
    libro_id =Column(Integer,ForeignKey )
    usuario_id=Column (Integer,ForeignKey)
    fecha_prestamo= Column(DateTime)
    fecha_devolucion= Column(DateTime)

