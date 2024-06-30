from models.libro import Libro as booksmodel
from schemas.libro import Libro as booksSchema

class LibroServicio():
    def __init__(self,db)-> None:
        self.db = db

    def get_books(self):
        result=self.dbquery(booksmodel).all()
        return result

    def get_books(self,id):
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
        self.db.commit()
        return

    def delete_book(self, id: int):
        self.db.query(booksmodel).filter(booksmodel.id == id).delete()
        self.db.commit()
        return


