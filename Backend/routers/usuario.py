from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from app.database import Session
from models.user import Usuario
from services.user import userService
from schemas.user import UsuarioBase,UsuarioCreate,UsuarioUpdate,Usuario
#from middleware.jwtbearer import JWTBearer

user_router = APIRouter()

@user_router.get('/users', tags=['user'],response_model=List[Usuario])#,dependencies=[Depends(JWTBearer())])
def get_users()-> List[Usuario]:
    db = Session()
    result = userService(db).get_users()
    return result

@user_router.get('/users/{id}', tags=['user'])
def get_user(id: int) -> Usuario:
    db = Session()
    result = userService(db).get_users(id)
    return result


@user_router.post('/users', tags=['user'], response_model=dict, status_code=201)
def create_user(user: Usuario) -> dict:
    db = Session()
    userService(db).create_user(user)
    return ({"Mensaje": "Se ha registrado al usuario "+user.nombre})

@user_router.put('/users/{id}',tags=["user"])
def update_user(id:int,user:Usuario):
    db=Session()
    result=userService(db).get_users(id)
    if not result:
        return("No se encontro la usuario especificado")

    userService(db).update_user(id,user)
    return {"Mensaje":"Se ha modificado al usuario con el id "+str(id)}


@user_router.delete('/users/{id}',tags=["user"])
def delete_user(id: int)-> dict:
    db = Session()
    result: Usuario=db.query(Usuario).filter(Usuario.id== id).first()
    if not result:
        return {"message": "No se encontró"}
    userService(db).delete_user(id)
    return {"message": "Se ha eliminado al usuario"}