from sqlalchemy import Column, Integer, String, DECIMAL,Enum,ForeignKey

from database import Base

class usuariosModel(Base):
    __tablename__ = "user"
    id= Column (Integer, primary_key=True, autoincrement=True)
    nombre=Column (String)
    email=Column(String)
    contraseña=Column(String)
    rol= Column(Enum("Bibliotecario","Cliente"))