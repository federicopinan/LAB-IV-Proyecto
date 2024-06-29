from datetime import datetime

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class loan(BaseModel):
    id:Optional[int]=None
    libro_id:Optional[int]=None
    usuario_id:Optional[int]=None
    fecha_prestamo:datetime
    fecha_devolucion:datetime
