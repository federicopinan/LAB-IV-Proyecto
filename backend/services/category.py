from models.category import categoryModel
from schemas.category import categorySchema

class categoryService():
    def __init__(self,db) -> None:
        self.db=db

    def get_categories(self):
        result=self.dbquery(categoryModel).all()
        return result

    def get_categories(self,id):
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