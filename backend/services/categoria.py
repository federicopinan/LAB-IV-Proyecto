from models.categoria import categoryModel as categoryModel
from schemas.categoria import categoryModel as categorySchema
from models.prestamo import Prestamo 
from models.libro import Libro as booksmodel

#! Funciones CRUD para los endpoints del router categoryModel
class CategoriaServicio():
    def __init__(self,db) -> None:
        self.db=db

    def get_categoria(self):
        result=self.db.query(categoryModel).all()
        return result

    def get_categorie(self,id):
        result = self.db.query(categoryModel).filter(categoryModel.id == id).first()
        return result 

    def create_categorie(self,category:categorySchema):
        new_category = categoryModel(**category.dict())
        self.db.add(new_category)
        # self.db.add(new_category)
        self.db.commit()
        return

    def update_category(self, id: int, data: categorySchema):
        categoria=self.db.query(categoryModel).filter(categoryModel.id==id).first()
        categoria.nombre=data.nombre
        categoria.descripcion=data.descripcion
        self.db.commit()
        return

    def delete_categorie(self, id: int):
        self.db.query(categoryModel).filter(categoryModel.id == id).delete()
        self.db.commit()
        return
    
    #Query para mostrar la categoria más popular
    def get_categoria_mas_popular(db: Session):
        return db.query(
            categoria.nombre,
            func.count(Prestamo.id).label("total")
        ).join(booksmodel, categoryModel.id == booksmodel.categoria_id
        ).join(Prestamo, booksmodel.id == Prestamo.libro_id
        ).group_by(categoryModel.id
        ).order_by(func.count(Prestamo.id).desc()
        ).first()