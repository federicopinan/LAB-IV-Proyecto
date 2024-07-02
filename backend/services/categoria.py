from models.categoria import Categoria as categoryModel
from schemas.categoria import Categoria as categorySchema

#! Funciones CRUD para los endpoints del router Categoria
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