from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from config.database import Session
from models.prestamo import Prestamo
from services.prestamo import PrestamoServicio
from schemas.prestamo import Prestamo as PrestamoSchema
from middlewares.jwt_manager import JWTBearer

prestamo_router = APIRouter()

@prestamo_router.get('/loans', tags=['loan'],response_model=List[PrestamoSchema])#,dependencies=[Depends(JWTBearer())])
def get_loans()-> List[PrestamoSchema]:
    db = Session()
    result = PrestamoServicio(db).get_loans()
    return result

@prestamo_router.get('/loans/{id}', tags=['loan'])
def get_loan(id: int) -> PrestamoSchema:
    db = Session()
    result = PrestamoServicio(db).get_loan(id)
    return result


@prestamo_router.post('/loans', tags=['loan'], response_model=dict, status_code=201)
def create_loan(prestamo: PrestamoSchema) -> dict:
    db = Session()
    PrestamoServicio(db).create_loan(prestamo)
    return ({"Mensaje": "Se ha registrado el prestamo "})

@prestamo_router.put('/loans/{id}',tags=["loan"])
def update_loan(id:int,prestamo:PrestamoSchema):
    db=Session()
    result=PrestamoServicio(db).get_loan(id)
    if not result:
        return("No se encontro el prestamo especificado")

    PrestamoServicio(db).update_loan(id,prestamo)
    return {"Mensaje":"Se ha modificado el prestamo con el id "+str(id)}


@prestamo_router.delete('/loans/{id}',tags=["loan"])
def delete_loan(id: int)-> dict:
    db = Session()
    result: Prestamo=db.query(Prestamo).filter(Prestamo.id == id).first()
    if not result:
        return {"message": "No se encontró"}
    PrestamoServicio(db).delete_loan(id)
    return {"message": "Se ha eliminado el libro"}

# Obtener la lista de préstamos activos de un usuario.
@prestamo_router.get("/loans/prestamosactivos/{id}",tags=["loan"])
def Get_Active_Loans_ByUser(id:int) ->PrestamoSchema:
    db = Session()
    result = PrestamoServicio(db).get_prestamos_activos(id)
    return result

#Obtener el historial de préstamos de un usuario
@prestamo_router.get("/loans/prestamoshistorial/{id}",tags=["loan"])
def Get_LoanHistory_ByUser(id:int) ->PrestamoSchema:
    db=Session()
    result = PrestamoServicio(db).get_historial_prestamos(id)
    return result

            
                     