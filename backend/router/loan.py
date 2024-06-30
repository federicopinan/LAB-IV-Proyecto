from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from app.database import Session
from models.loan import Prestamo
from services.loan import loanService
from schemas.loan import PrestamoBase,PrestamoUpdate,PrestamoCreate,Prestamo
#from middleware.jwtbearer import JWTBearer

loan_router = APIRouter()

@loan_router.get('/loans', tags=['loan'],response_model=List[Prestamo])#,dependencies=[Depends(JWTBearer())])
def get_loans()-> List[Prestamo]:
    db = Session()
    result = loanService(db).get_loans()
    return result

@loan_router.get('/loans/{id}', tags=['loan'])
def get_loan(id: int) -> Prestamo:
    db = Session()
    result = loanService(db).get_loans(id)
    return result


@loan_router.post('/loans', tags=['loan'], response_model=dict, status_code=201)
def create_loan(prestamo: Prestamo) -> dict:
    db = Session()
    loanService(db).create_loan(prestamo)
    return ({"Mensaje": "Se ha registrado el prestamo "})

@loan_router.put('/loans/{id}',tags=["loan"])
def update_loan(id:int,prestamo:Prestamo):
    db=Session()
    result=loanService(db).get_loans(id)
    if not result:
        return("No se encontro el prestamo especificado")

    loanService(db).update_loan(id,prestamo)
    return {"Mensaje":"Se ha modificado el prestamo con el id "+str(id)}


@loan_router.delete('/loans/{id}',tags=["loan"])
def delete_loan(id: int)-> dict:
    db = Session()
    result: Prestamo=db.query(Prestamo).filter(Prestamo.id == id).first()
    if not result:
        return {"message": "No se encontró"}
    loanService(db).delete_loan(id)
    return {"message": "Se ha eliminado el libro"}