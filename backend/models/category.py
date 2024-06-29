from sqlalchemy import Column, Integer, String, DECIMAL,Enum,ForeignKey
from database import Base

class categoryModel(Base):
    __tablaname__ = "category"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre =Column(String)
    descripcion=Column (String)

