from sqlalchemy import Column, Integer, String, DECIMAL,Enum,ForeignKey,DateTime
from database import Base

class loanModel(Base):
    __tablename__ = "loan"
    id=Column(Integer, primary_key=True,autoincrement=True)
    libro_id =Column(Integer,ForeignKey("book.id"))
    usuario_id=Column (Integer,ForeignKey("user.id"))
    fecha_prestamo= Column(DateTime)
    fecha_devolucion= Column(DateTime)

