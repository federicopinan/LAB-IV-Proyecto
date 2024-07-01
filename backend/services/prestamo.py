from models.prestamo import Prestamo as loanModel
from schemas.prestamo import Prestamo as  loanSchema

#! Funciones CRUD para los endpoints del router Prestamo
class PrestamoServicio():
    def __init__(self,db) -> None:
        self.db=db

    def get_loans(self):
        result=self.dbquery(loanModel).all()
        return result

    def get_loans(self,id):
        result = self.db.query(loanModel).filter(loanModel.id == id).first()
        return result 

    def create_loan(self,loan:loanSchema):
        new_loan= loanModel(**loan.dict())
        self.db.add(new_loan)
        self.db.commit()
        return

    def update_loan(self, id: int, data: loanSchema):
        prestamo=self.db.query(loanModel).filter(loanModel.id==id).first()
        prestamo.libro_id=data.libro_id
        prestamo.usuario_id=data.usuario_id
        prestamo.fecha_prestamo=data.fecha_prestamo
        prestamo.fecha_devolucion=data.fecha_devolucion
        self.db.commit()
        return

    def delete_loan(self, id: int):
        self.db.query(loanModel).filter(loanModel.id == id).delete()
        self.db.commit()
        return