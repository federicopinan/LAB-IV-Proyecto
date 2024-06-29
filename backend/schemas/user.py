from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List


class userSchema(BaseModel):
    id:Optional[int]=None
    nombre:str
    email:EmailStr
    contrasena:str
    rol:str