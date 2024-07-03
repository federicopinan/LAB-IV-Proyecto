from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from config.database import Session
from models.libro import Libro
from services.libro import LibroServicio
from schemas.libro import Libro as LibroSchema
from middlewares.jwt_manager import JWTBearer


libro_router = APIRouter()

@libro_router.get('/libros/', tags=["Libros📚"],response_model=List[LibroSchema])#,dependencies=[Depends(JWTBearer())])
def get_Books()-> List[LibroSchema]:
    db = Session()
    result = LibroServicio(db).get_books()
    return result

@libro_router.get('/libros/{id}', tags=["Libros📚"])
def get_Book(id: int) -> LibroSchema:
    db = Session()
    result = LibroServicio(db).get_book(id)
    return result


@libro_router.post('/libros/', tags=["Libros📚"], response_model=dict, status_code=201)
def create_book(libro: LibroSchema) -> dict:
    db = Session()
    LibroServicio(db).create_book(libro)
    return ({"Mensaje": "Se ha registrado el libro "+libro.titulo})

@libro_router.put('/libros/{id}',tags=["Libros📚"])
def update_book(id:int,libro:LibroSchema):
    db=Session()
    result=LibroServicio(db).get_book(id)
    if not result:
        return("No se encontro el libro especificado")

    LibroServicio(db).update_book(id,libro)
    return {"Mensaje":"Se ha modificado el libro con el id "+str(id)}


@libro_router.delete('/libros/{id}',tags=["Libros📚"])
def delete_book(id: int)-> dict:
    db = Session()
    result: Libro=db.query(Libro).filter(Libro.id == id).first()
    if not result:
        return {"message": "No se encontró"}
    LibroServicio(db).delete_book(id)
    return {"message": "Se ha eliminado el libro"}

#Listar todos los libros de una categoría específica.
@libro_router.get("/libros_por_categoria/{id}",tags=["Libros📚"])
def get_Book_By_CategoryID(id:int)->dict:
    db=Session()
    result = LibroServicio(db).get_libros_por_categoria(id)
    return result

@libro_router.get("/libros_por_titulo/",tags=["Libros📚"])
def GetBookByTittle(titulo:str)->List[LibroSchema]:
    db=Session()
    result=LibroServicio(db).get_libros_by_titulo(titulo)
    return result

@libro_router.get("/libros_por_autor/",tags=["Libros📚"])
def GetBookByAuthor(autor:str)->List[LibroSchema]:
    db=Session()
    result=LibroServicio(db).get_libros_by_autor(autor)
    return result

@libro_router.get("/libros_disponibles/",tags=["Libros📚"])
def GetBookByDisponibles()->List[LibroSchema]:
    db=Session()
    result=LibroServicio(db).get_libros_disponibles()
    return result
