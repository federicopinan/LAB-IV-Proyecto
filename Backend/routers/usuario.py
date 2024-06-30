from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from app.database import Session
from models.usuario import Usuario
from services.usuario import UsuarioServicio
from schemas.usuario import Usuario as UsuarioSchema
from middlewares.jwt_manager import JWTBearer

usuario_router = APIRouter()

@usuario_router.get('/users', tags=['user'],response_model=List[UsuarioSchema])#,dependencies=[Depends(JWTBearer())])
def get_users()-> List[UsuarioSchema]:
    db = Session()
    result = userService(db).get_users()
    return result

@usuario_router.get('/users/{id}', tags=['user'])
def get_user(id: int) -> UsuarioSchema:
    db = Session()
    result = userService(db).get_users(id)
    return result


@usuario_router.post('/users', tags=['user'], response_model=dict, status_code=201)
def create_user(user: UsuarioSchema) -> dict:
    db = Session()
    userService(db).create_user(user)
    return ({"Mensaje": "Se ha registrado al usuario "+user.nombre})

@usuario_router.put('/users/{id}',tags=["user"])
def update_user(id:int,user:UsuarioSchema):
    db=Session()
    result=userService(db).get_users(id)
    if not result:
        return("No se encontro la usuario especificado")

    userService(db).update_user(id,user)
    return {"Mensaje":"Se ha modificado al usuario con el id "+str(id)}


@usuario_router.delete('/users/{id}',tags=["user"])
def delete_user(id: int)-> dict:
    db = Session()
    result: Usuario=db.query(Usuario).filter(Usuario.id== id).first()
    if not result:
        return {"message": "No se encontró"}
    userService(db).delete_user(id)
    return {"message": "Se ha eliminado al usuario"}