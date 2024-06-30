from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.responses import JSONResponse
from app.database import Session
from models.book import Libro
from services.book import bookService
from schemas.book import LibroBase
#from middleware.jwtbearer import JWTBearer

book_router = APIRouter()

@book_router.get('/book', tags=['book'],response_model=List[LibroBase])#,dependencies=[Depends(JWTBearer())])
def get_Books()-> List[LibroBase]:
    db = Session()
    result = bookService(db).get_books()
    return result

@book_router.get('/books/{id}', tags=['book'])
def get_Book(id: int) -> LibroBase:
    db = Session()
    result = bookService(db).get_books(id)
    return result


@book_router.post('/books', tags=['book'], response_model=dict, status_code=201)
def create_book(libro: LibroBase) -> dict:
    db = Session()
    bookService(db).create_book(libro)
    return ({"Mensaje": "Se ha registrado el libro "+libro.titulo})

@book_router.put('/books/{id}',tags=["book"])
def update_book(id:int,libro:LibroBase):
    db=Session()
    result=bookService(db).get_books(id)
    if not result:
        return("No se encontro el libro especificado")

    bookService(db).update_book(id,libro)
    return {"Mensaje":"Se ha modificado el libro con el id "+str(id)}


@book_router.delete('/books/{id}',tags=["book"])
def delete_book(id: int)-> dict:
    db = Session()
    result: Libro=db.query(Libro).filter(Libro.id == id).first()
    if not result:
        return {"message": "No se encontró"}
    bookService(db).delete_book(id)
    return {"message": "Se ha eliminado el libro"}