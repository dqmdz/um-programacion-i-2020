from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class DBCon:
    def __init__(self):

        # Contenedor Docker con MySQL
        str_conexion = 'mysql+pymysql://lucas:lucas@'
        str_conexion += 'mysql:3306/TP4'
        self.engine = create_engine(str_conexion, echo=True)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.crear_estructura()

    def crear_estructura(self):
        Base.metadata.create_all(self.engine)


# Relacion One To Many
# One
class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100))
    registros = relationship('Registro', backref="persona")

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.registro = None

    def __repr__(self):
        resultado = ''
        for reg in self.registros:
            resultado = resultado + "{}\n".format(reg)
        salida = 'Persona {}: apellido, nombre: {}, {}. '\
            .format(self.id, self.apellido, self.nombre)
        salida += 'Lista de registros:\n {}'\
            .format(resultado)
        return salida


# Many
class Registro(Base):
    __tablename__ = "registro"
    id = Column(Integer, primary_key=True)
    actividad = Column(String(160))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    persona_id = Column(Integer, ForeignKey('persona.id'))

    def __init__(self, actividad):
        self.actividad = actividad

    def __repr__(self):
        salida = "Registo {}: actividad: {}. Creado el {}".format(
            self.id, self.actividad, self.fecha_creacion)
        return salida


class PersonaDao:
    def __init__(self, db):
        self.db = db

    def guardar(self, persona):
        self.db.session.add(persona)
        self.db.session.commit()
        # self.db.session.close()
        # return registro

    def borrar(self, persona):
        self.db.session.delete(persona)
        self.db.session.commit()
        # self.db.session.close()

    def modificar(self, persona):
        actual = self.db.session.query(Persona).filter_by(id=persona.id).one()
        actual.nombre = persona.nombre
        actual.apellido = persona.apellido
        self.db.session.commit()
        # self.db.session.close()
        return actual

    def buscarPorID(self, id):
        consulta = self.db.session.query(Persona).filter_by(id=id)
        if consulta.count() > 0:
            return consulta.one()
        else:
            return None

    def buscarTodos(self):
        actual = self.db.session.query(Persona).all()
        return actual


def main():
    print("Conectandose a la base de datos")
    print("Creando la estructura de las tablas")
    print("Creando la sesion de acceso a la base de datos")
    db = DBCon()
    print("Creando DAO")
    personaDAO = PersonaDao(db)

    r1 = Registro("accion 1")
    r2 = Registro("accion 2")
    pers1 = Persona("Fernando", "Villarreal")
    pers1.registros.append(r1)
    pers1.registros.append(r2)

    personaDAO.guardar(pers1)

    r1 = Registro("accion 1")
    r2 = Registro("accion 2")
    r3 = Registro("accion 3")
    r4 = Registro("accion 4")
    pers1 = Persona("Otra", "Persona")
    pers1.registros.append(r1)
    pers1.registros.append(r2)
    pers1.registros.append(r3)
    pers1.registros.append(r4)

    personaDAO.guardar(pers1)

    pers2 = personaDAO.buscarPorID(1)
    pers2.nombre = "Cambiando"
    pers2.apellido = "Nombre"
    personaDAO.modificar(pers2)
    personas = personaDAO.buscarTodos()
    for persona in personas:
        print(persona)


if __name__ == "__main__":
    main()
