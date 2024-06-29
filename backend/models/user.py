from sqlalchemy import Column, Integer, String, DECIMAL,Enum,ForeignKey

from database import Base

class usuariosModel(Base):
    id= Column (Integer, primary_key=True, autoincrement=True)
    nombre=Column (String)
    email=Column(String)
    contraseña= (String)
    rol= Column(Enum("Bibliotecario","Cliente"))