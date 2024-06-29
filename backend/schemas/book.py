from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List


class booksSchema(BaseModel):
    id:Optional[int]=None
    titulo:str
    autor:str
    isbn:str
    editorial:str
    categoria_id:Optional[int]=None