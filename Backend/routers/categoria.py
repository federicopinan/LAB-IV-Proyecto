from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from config.database import Session
from models.categoria import Categoria
from services.categoria import CategoriaServicio
from schemas.categoria import Categoria as CategoriaSchema
from middlewares.jwt_manager import JWTBearer
from passlib.context import CryptContext


categoria_router = APIRouter()

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def authenticate_user(users:dict, email: str, password: str)->Usuario:
#     user = get_user(users, email)
#     if not user:
#         return False
#     if not verify_password(password, user.password):
#         return False
#     user = Usuario.model_validate(user)
#     return user

# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)

# def get_user(users:list, email: str):
#     for item in users:
#         if item.email == email:
#             return item

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)    

@categoria_router.get('/categoria', tags=["Categorias🏷️"],response_model=List[CategoriaSchema])#,dependencies=[Depends(JWTBearer())])
def get_Category()-> List[CategoriaSchema]:
    db = Session()
    result = CategoriaServicio(db).get_categoria()
    return result

@categoria_router.get('/categoria/{id}', tags=["Categorias🏷️"])
def get_Category(id: int) -> CategoriaSchema:
    db = Session()
    result = CategoriaServicio(db).get_categorie(id)
    return result


@categoria_router.post('/categoria', tags=["Categorias🏷️"], response_model=dict, status_code=201)
def create_category(cat: CategoriaSchema) -> dict:
    db = Session()
    CategoriaServicio(db).create_categorie(cat)
    return ({"Mensaje": "Se ha registrado la categoria "+cat.nombre})

@categoria_router.put('/categoria/{id}',tags=["Categorias🏷️"])
def update_category(id:int,cat:CategoriaSchema):
    db=Session()
    result=CategoriaServicio(db).get_categorie(id)
    if not result:
        return("No se encontro la categoria especificada")

    CategoriaServicio(db).update_category(id,cat)
    return {"Mensaje":"Se ha modificado la categoria con el id "+str(id)}


@categoria_router.delete('/categoria/{id}',tags=["Categorias🏷️"])
def delete_category(id: int)-> dict:
    db = Session()
    result: Categoria=db.query(Categoria).filter(Categoria.id == id).first()
    if not result:
        return {"message": "No se encontró"}
    CategoriaServicio(db).delete_categorie(id)
    return {"message": "Se ha eliminado la categoria"}