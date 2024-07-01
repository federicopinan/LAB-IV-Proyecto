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

categoria_router = APIRouter()

@categoria_router.get('/category', tags=['category'],response_model=List[CategoriaSchema])#,dependencies=[Depends(JWTBearer())])
def get_Category()-> List[CategoriaSchema]:
    db = Session()
    result = CategoriaServicio(db).get_categories()
    return result

@categoria_router.get('/category/{id}', tags=['category'])
def get_Category(id: int) -> CategoriaSchema:
    db = Session()
    result = CategoriaServicio(db).get_categories(id)
    return result


@categoria_router.post('/category', tags=['category'], response_model=dict, status_code=201)
def create_category(cat: CategoriaSchema) -> dict:
    db = Session()
    CategoriaServicio(db).create_categorie(cat)
    return ({"Mensaje": "Se ha registrado la categoria "+cat.nombre})

@categoria_router.put('/category/{id}',tags=["category"])
def update_category(id:int,cat:CategoriaSchema):
    db=Session()
    result=CategoriaServicio(db).get_categories(id)
    if not result:
        return("No se encontro lacategoria especificada")

    CategoriaServicio(db).update_category(id,cat)
    return {"Mensaje":"Se ha modificado la categoria con el id "+str(id)}


@categoria_router.delete('/category/{id}',tags=["category"])
def delete_category(id: int)-> dict:
    db = Session()
    result: Categoria=db.query(Categoria).filter(Categoria.id == id).first()
    if not result:
        return {"message": "No se encontró"}
    CategoriaServicio(db).delete_categorie(id)
    return {"message": "Se ha eliminado la categoria"}