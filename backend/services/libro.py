from models.libro import Libro as booksmodel
from schemas.libro import Libro as booksSchema
from models.prestamo import Prestamo 
import datetime
#! Funciones CRUD para los endpoints del router libro
class LibroServicio():
    def __init__(self,db)-> None:
        self.db = db

    def get_books(self):
        result=self.db.query(booksmodel).all()
        return result

    def get_book(self,id):
        result = self.db.query(booksmodel).filter(booksmodel.id == id).first()
        return result 

    def create_book(self,book:booksSchema):
        new_book = booksmodel(**book.dict())
        self.db.add(new_book)
        self.db.commit()
        return

    def update_book(self, id: int, data: booksSchema):
        book=self.db.query(booksmodel).filter(booksmodel.id==id).first()
        book.titulo=data.titulo
        book.autor=data.autor
        book.isbn=data.isbn
        book.editorial=data.editorial
        book.categoria_id=data.categoria_id
        book.disponible=data.disponible
        self.db.commit()
        return

    def delete_book(self, id: int):
        self.db.query(booksmodel).filter(booksmodel.id == id).delete()
        self.db.commit()
        return
    #Listar todos los libros de una categoría específica.
    def get_libros_por_categoria(self,categoria_id: int):
        return self.db.query(booksmodel).filter(booksmodel.categoria_id == categoria_id).all()
    
    #Listar libro por queries
    def get_libros_by_autor(self, autor:str):
        result = self.db.query(booksmodel).filter(booksmodel.autor == autor).all()
        return result
    
    def get_libros_by_titulo(self, titulo:str):
        result = self.db.query(booksmodel).filter(booksmodel.titulo == titulo).all()
        return result
    
    def get_libros_disponibles(self,):
        result = self.db.query(booksmodel).filter(booksmodel.disponible == True).all()
        return result

    #Query para buscar el total de libros
    def get_total_libros(db: Session):
        now = datetime.now()
        libros_sin_prestamo = db.query(booksmodel).outerjoin(Prestamo, booksmodel.id == Prestamo.libro_id).filter(
            or_(Prestamo.id == None, Prestamo.fecha_devolucion <= now)
        ).count()
        return libros_sin_prestamo