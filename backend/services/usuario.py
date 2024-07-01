from models.usuario import Usuario as usuariosModel
from schemas.usuario import  Usuario as  userSchema

#! Funciones CRUD para los endpoints del router Usuario
class UsuarioServicio():
    def __init__(self,db) -> None:
        self.db=db

    def get_users(self):
        result=self.dbquery(usuariosModel).all()
        return result

    def get_users(self,id):
        result = self.db.query(usuariosModel).filter(usuariosModel.id == id).first()
        return result 

    def create_user(self,user:userSchema):
        new_user= usuariosModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return

    def update_user(self, id: int, data: userSchema):
        usuario=self.db.query(usuariosModel).filter(usuariosModel.id==id).first()
        usuario.nombre=data.nombre
        usuario.email=data.email
        usuario.contrasena=data.contrasena
        self.db.commit()
        return

    def delete_user(self, id: int):
        self.db.query(usuariosModel).filter(usuariosModel.id == id).delete()
        self.db.commit()
        return