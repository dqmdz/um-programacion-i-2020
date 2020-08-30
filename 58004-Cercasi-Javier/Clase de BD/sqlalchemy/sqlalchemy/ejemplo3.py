from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class DBCon:
    def __init__(self):
        #self.engine = create_engine('sqlite:///fernando.db', echo=False, connect_args={"check_same_thread": False})
        self.engine = create_engine('mysql+pymysql://fernando:fernando@192.168.10.106:3306/sqlalchemy',
                               echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.crear_estructura()

    def crear_estructura(self):
        Base.metadata.create_all(self.engine)



class Registro(Base):
    __tablename__ = "registro"
    id = Column(Integer, primary_key=True)
    actividad = Column(String(160))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, actividad):
        self.actividad = actividad

    def __repr__(self):
        salida = "Registo {}: actividad: {}. Creado el {}".format(
            self.id, self.actividad, self.fecha_creacion)
        return salida

class RegistroDao:
    def __init__(self, db):
        self.db = db

    def guardar(self, registro):
        self.db.session.add(registro)
        self.db.session.commit()
        #self.db.session.close()
        return registro

    def borrar(self, registro):
        self.db.session.delete(registro)
        self.db.session.commit()
        #self.db.session.close()

    def modificar(self, registro):
        actual = self.db.session.query(Registro).filter_by(id=registro.id).one()
        actual.actividad = registro.actividad
        self.db.session.commit()
        #self.db.session.close()
        return actual

    def buscarPorID(self, id):
        consulta = self.db.session.query(Registro).filter_by(id=id)
        if consulta.count() > 0:
            return consulta.one()
        else:
            return None


    def buscarTodos(self):
        actual = self.db.session.query(Registro).all()
        return actual


if __name__ == "__main__":
    print("Conectandose a la base de datos")
    print("Creando la estructura de las tablas")
    print("Creando la sesion de acceso a la base de datos")
    db = DBCon()
    print("Creando DAO")
    rDAO = RegistroDao(db)
    print("Agregando 2 registros")
    r1 = Registro("accion 1")
    print("Mostrando el registro r1 antes de guardar en la base de datos")
    print(r1)
    r2 = Registro("accion 2")
    r1 = rDAO.guardar(r1)
    rDAO.guardar(r2)
    print("Mostrando el registro r1 despues de guardar en la base de datos")
    print(r1)
    print("Recuperando y mostrando todo en la base de datos")
    resultado = rDAO.buscarTodos()
    for registro in resultado:
        print(registro)
    print("Agregando 2 registros mas")
    r1 = Registro("accion 3")
    r2 = Registro("accion 4")
    rDAO.guardar(r1)
    rDAO.guardar(r2)
    print("Recuperando y mostrando todo en la base de datos")
    resultado = rDAO.buscarTodos()
    for registro in resultado:
        print(registro)
    print("Borrando el segundo registro")
    registro = rDAO.buscarPorID(6)
    if registro:
        rDAO.borrar(registro)
    print("Recuperando y mostrando todo en la base de datos")
    resultado = rDAO.buscarTodos()
    for registro in resultado:
        print(registro)
    print("Borrando todos los registros")
    resultado = rDAO.buscarTodos()
    for registro in resultado:
        rDAO.borrar(registro)

    pass