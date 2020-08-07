from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()


class Registro(Base):
    __tablename__ = "registro"
    id = Column(Integer, primary_key=True)
    actividad = Column(String(length=50))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, actividad):
        self.actividad = actividad

    def __repr__(self):
        salida = "Registo {}: actividad: {}. Creado el {}".format(
            self.id, self.actividad, self.fecha_creacion)
        return salida

if __name__ == "__main__":
    print("Conectandose a la base de datos")
    #engine = create_engine('sqlite:///fernando.db',
    #                       echo=False,
    #                       connect_args={"check_same_thread": False})
    engine = create_engine('mysql+pymysql://fernando:fernando@192.168.10.106:3306/sqlalchemy',
                           echo=True)

    print("Creando la estructura de las tablas")
    Base.metadata.create_all(engine)
    print("Creando la sesion de acceso a la base de datos")
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Agregando 2 registros")
    r1 = Registro("accion 1")
    print("Mostrando el registro r1 antes de guardar en la base de datos")
    print(r1)
    r2 = Registro("accion 2")
    session.add(r1)
    session.add(r2)
    session.commit()
    print("Mostrando el registro r1 despues de guardar en la base de datos")
    print(r1)
    print("Recuperando y mostrando todo en la base de datos")
    #session.close()
    #session = Session()
    resultado = session.query(Registro).all()
    for registro in resultado:
        print(registro)
    print("Agregando 2 registros mas")
    r1 = Registro("accion 3")
    r2 = Registro("accion 4")
    session.add(r1)
    session.add(r2)
    session.commit()
    print("Recuperando y mostrando todo en la base de datos")
    #session.close()
    session = Session()
    resultado = session.query(Registro).all()
    for registro in resultado:
        print(registro)
    print("Borrando el segundo registro")
    #session.close()
    session = Session()
    resultado = session.query(Registro).filter_by(id=2)
    if resultado.count() > 0:
        registro = resultado.one()
        #session.delete(registro)
        #session.commit()

    resultado = session.query(Registro).filter_by(id=2)
    if resultado.count() > 0:
        registro = resultado.one()

        if registro.actividad == "fsdfsdf":
            pass

        identificador = registro.id

        print("ID: {}".format(identificador))




    print("Recuperando y mostrando todo en la base de datos")
    #session.close()
    session = Session()
    resultado = session.query(Registro).all()
    for registro in resultado:
        print(registro)
    print("Borrando todos los registros")
    #session.close()
    session = Session()
    resultado = session.query(Registro).all()
    for registro in resultado:
        session.delete(registro)
    session.commit()
    session.close()
