from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class DBConexion:
    def __init__(self):

        # Docker con MySQL
        str_conexion = 'mysql+pymysql://joaquin:joaquin@mysql:3306/sqlalchemy-TP4'
        self.engine = create_engine(str_conexion, echo=False)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.crear_estructura()

    def crear_estructura(self):
        Base.metadata.create_all(self.engine)


class Persona(Base):
    __tablename__ = "Persona"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100))
    tipo = Column(String(20), nullable=False)
    actividad = relationship('Actividad')
    
    def __init__(self, nombre, apellido, tipo="Cliente"):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo

    def __repr__(self):
        resultado = ''
        for actividad in self.actividad:
            resultado=resultado+"{}\n".format(actividad)
        salida = 'Id: {}: Apellido, Nombre: {}, {}. Lista de registros:\n {}'\
            .format(self.id, self.apellido, self.nombre, resultado)
        return salida

class Actividad(Base):
    __tablename__ = "Actividad"
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(50))
    tipo_actividad = Column(Integer, ForeignKey('TipoActividad.id'))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    persona_id = Column(Integer, ForeignKey('Persona.id'))
    descripcion = Column(String(160))
    
    

    def __init__(self, mensaje, descripcion):
        self.mensaje = mensaje
        self.descripcion = descripcion

    def __repr__(self):
        salida = "Actividad: ID: {}\n Tipo de actividad: {}-- Descripcion: {}. Realizado por: {} Fecha de Creacion {}".format(
            self.id, self.tipo_actividad,self.descripcion,self.persona_id, self.fecha_creacion)
        return salida

class Tipo_Actividad(Base):
    __tablename__ = "TipoActividad"
    id = Column(Integer, primary_key=True)
    tipo_actividad = Column(String(160))
    descripcion = Column(String(280))
    actividad = relationship('Actividad')

    def __init__(self, tipo_actividad, descripcion):
        self.tipo_actividad = tipo_actividad
        self.descripcion = descripcion

    def __repr__(self):
        salida = "Actividad {}:\nTipo de actividad: {}\nDescripcion {}\n"\
            .format(self.id, self.tipo_actividad, self.descripcion)
        return salida
    
class PersonaDao:
    def __init__(self, db):
        self.db = db
        

    def guardar(self, persona):
        self.db.session.add(persona)
        self.db.session.commit()
        #self.db.session.close()
        #return registro

    def borrar(self, persona):
        self.db.session.delete(persona)
        self.db.session.commit()
        #self.db.session.close()

    def modificar(self, persona):
        actual = self.db.session.query(Persona).filter_by(id=persona.id).one()
        actual.nombre = persona.nombre
        actual.apellido = persona.apellido
        self.db.session.commit()
        #self.db.session.close()
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

class ActividadDao:
    def __init__(self, db):
        self.db = db

    def guardar(self, actividad):
        self.db.session.add(actividad)
        self.db.session.commit()
        #self.db.session.close()
        #return registro

    def borrar(self, actividad):
        self.db.session.delete(actividad)
        self.db.session.commit()
        #self.db.session.close()

    def modificar(self, actividad):
        actual = self.db.session.query(Actividad).filter_by(id=actividad.id).one()
        actual.mensaje = actividad.mensaje
        actual.descripcion = actividad.descripcion
        actual.tipo_actividad = actividad.tipo_actividad
        actual.persona_id = actividad.persona_id
        self.db.session.commit()
        #self.db.session.close()
        return actual

    def buscarPorID(self, id):
        consulta = self.db.session.query(Actividad).filter_by(id=id)
        if consulta.count() > 0:
            return consulta.one()
        else:
            return None

    def buscarTodos(self):
        actual = self.db.session.query(Actividad).all()
        return actual

class Tipo_ActividadDao:
    def __init__(self, db):
        self.db = db

    def guardar(self, tipo_actividad):
        self.db.session.add(tipo_actividad)
        self.db.session.commit()
        #self.db.session.close()
        #return registro

    def borrar(self, tipo_actividad):
        self.db.session.delete(tipo_actividad)
        self.db.session.commit()
        #self.db.session.close()

    def modificar(self, tipo_actividad):
        actual = self.db.session.query(Tipo_Actividad).filter_by(id=tipo_actividad.id).one()
        actual.descripcion = tipo_actividad.descripcion
        actual.tipo_actividad = tipo_actividad.tipo_actividad
        self.db.session.commit()
        #self.db.session.close()
        return actual

    def buscarPorID(self, id):
        consulta = self.db.session.query(Tipo_Actividad).filter_by(id=id)
        if consulta.count() > 0:
            return consulta.one()
        else:
            return None

    def buscarTodos(self):
        actual = self.db.session.query(Tipo_Actividad).all()
        return actual
