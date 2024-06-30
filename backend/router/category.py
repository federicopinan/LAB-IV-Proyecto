from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from app.database import Session
from models.category import Categoria
from services.category import categoryService
from schemas.category import Categoria
#from middleware.jwtbearer import JWTBearer

category_router = APIRouter()

@category_router.get('/category', tags=['category'],response_model=List[Categoria])#,dependencies=[Depends(JWTBearer())])
def get_Category()-> List[Categoria]:
    db = Session()
    result = categoryService(db).get_categories()
    return result

@category_router.get('/category/{id}', tags=['category'])
def get_Category(id: int) -> Categoria:
    db = Session()
    result = categoryService(db).get_categories(id)
    return result


@category_router.post('/category', tags=['category'], response_model=dict, status_code=201)
def create_category(cat: Categoria) -> dict:
    db = Session()
    categoryService(db).create_categorie(cat)
    return ({"Mensaje": "Se ha registrado la categoria "+cat.nombre})

@category_router.put('/category/{id}',tags=["category"])
def update_category(id:int,cat:Categoria):
    db=Session()
    result=categoryService(db).get_categories(id)
    if not result:
        return("No se encontro lacategoria especificada")

    categoryService(db).update_category(id,cat)
    return {"Mensaje":"Se ha modificado la categoria con el id "+str(id)}


@category_router.delete('/category/{id}',tags=["category"])
def delete_category(id: int)-> dict:
    db = Session()
    result: Categoria=db.query(Categoria).filter(Categoria.id == id).first()
    if not result:
        return {"message": "No se encontró"}
    categoryService(db).delete_categorie(id)
    return {"message": "Se ha eliminado la categoria"}