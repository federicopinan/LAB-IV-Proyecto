from sqlalchemy import Column, Integer, String, DECIMAL,Enum,ForeignKey
from database import Base

class booksmodel(Base):
    __tablename__ ="book"
    id =Column(Integer, primary_key=True,autoincrement=True)
    titulo =Column(String(50))
    autor= Column(String(50))
    isbn =Column(String(50))
    editorial =Column(String(50))
    categoria_id =Column(Integer,ForeignKey("category.id"))
