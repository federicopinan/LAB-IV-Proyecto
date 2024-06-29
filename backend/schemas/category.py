from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List


class category(BaseModel):
    id :Optional[int]=None
    nombre:str
    descripcion:str