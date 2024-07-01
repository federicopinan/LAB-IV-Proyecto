from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from config.database import Session
from models.usuario import Usuario
from services.usuario import UsuarioServicio
from schemas.usuario import Usuario as UsuarioSchema
from middlewares.jwt_manager import JWTBearer
from fastapi import APIRouter
from pydantic import BaseModel
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse

usuario_router = APIRouter()

@usuario_router.get('/users', tags=['user'],response_model=List[UsuarioSchema])#,dependencies=[Depends(JWTBearer())])
def get_users()-> List[UsuarioSchema]:
    db = Session()
    result = UsuarioServicio(db).get_users()
    return result

@usuario_router.get('/users/{id}', tags=['user'])
def get_user(id: int) -> UsuarioSchema:
    db = Session()
    result = UsuarioServicio(db).get_user(id)
    return result


@usuario_router.post('/users', tags=['user'], response_model=dict, status_code=201)
def create_user(user: UsuarioSchema) -> dict:
    db = Session()
    UsuarioServicio(db).create_user(user)
    return ({"Mensaje": "Se ha registrado al usuario "+user.nombre})

@usuario_router.put('/users/{id}',tags=["user"])
def update_user(id:int,user:UsuarioSchema):
    db=Session()
    result=UsuarioServicio(db).get_users(id)
    if not result:
        return("No se encontro la usuario especificado")

    UsuarioServicio(db).update_user(id,user)
    return {"Mensaje":"Se ha modificado al usuario con el id "+str(id)}


@usuario_router.delete('/users/{id}',tags=["user"])
def delete_user(id: int)-> dict:
    db = Session()
    result: Usuario=db.query(Usuario).filter(Usuario.id== id).first()
    if not result:
        return {"message": "No se encontró"}
    UsuarioServicio(db).delete_user(id)
    return {"message": "Se ha eliminado al usuario"}

# @usuario_router.post('/login', tags=['autenticacion'])
# def login(user: UsuarioSchema):
#     if user.email == "admin@gmail.com" and user.password == "admin":
#         token: str = create_token(user.dict())
#         return JSONResponse(status_code=200, content=token)