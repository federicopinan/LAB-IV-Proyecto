from models.prestamo import Prestamo as loanModel
from schemas.prestamo import Prestamo as  loanSchema
from datetime import datetime, date 
#! Funciones CRUD para los endpoints del router Prestamo
class PrestamoServicio():
    def __init__(self,db) -> None:
        self.db=db

    def get_loans(self):
        result=self.db.query(loanModel).all()
        return result

    def get_loan(self,id):
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
    
    #Obtener Prestamos activos de un usuario por id de usuario
    def get_prestamo_activos(self, usuario_id: int):
        now = datetime.now()
        result = self.db.query(loanModel).filter(loanModel.usuario_id == usuario_id, loanModel.fecha_devolucion >= now).all()
        return result

    def is_libro_disponible(self, libro_id: int, fecha_prestamo: date, fecha_devolucion: date):
        existing_prestamos = self.db.query(loanModel).filter(
            loanModel.libro_id == libro_id,
            loanModel.fecha_prestamo < fecha_devolucion,
            loanModel.fecha_devolucion > fecha_prestamo
        ).all()
        return len(existing_prestamos) == 0 # si existe el libro o no

    #Obtener el historial de préstamos de un usuario por id de usuario
    def get_historial_prestamos(self, usuario_id: int):
        return self.db.query(loanModel).filter(loanModel.usuario_id == usuario_id).all()
    

    def get_Total_prestamos_activos(self):
        return self.db.query(loanModel).filter(loanModel.fecha_devolucion == None,loanModel.fecha_prestamo != None).count()