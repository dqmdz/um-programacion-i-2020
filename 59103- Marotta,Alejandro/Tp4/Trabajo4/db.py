from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class DBConexion:
    def __init__(self):

       
        # Contenedor Docker con MySQL
        conexion = 'mysql+pymysql://alejandro:alejandro@mysql:3306/Trabajo4'
        self.engine = create_engine(conexion, echo=True)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.crear_estructura()

    def crear_estructura(self):
        Base.metadata.create_all(self.engine)

class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer,primary_key=True)
    nombre = Column(String(50),nullable = False)
    apellido = Column(String(50),nullable=False)
    tipo = Column(String(20),nullable=False)
    actividades = relationship("Actividad") #backref hace que sea bidireccional

    def __init__(self,nombre,apellido,tipo = "Cliente"):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo
        #self.actividades = None

    def __repr__(self):
        resultado = ''
        for act in self.actividades:
            resultado=resultado+"{}\n".format(act)
        salida = '{}: id = {}, Apellido: {},  Nombre: {}. Lista de actividades:\n {}'.format(self.tipo,self.id, self.apellido, self.nombre, resultado)
        return salida


class Actividad(Base):
    __tablename__ = "actividad"
    id = Column(Integer, primary_key=True)
    tipo_mensaje = Column(String(50))
    tipo_actividad = Column(Integer, ForeignKey('tipoActividad.id'))
    codigo_resultado = Column(String(50))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())    
    persona_id = Column(Integer, ForeignKey('persona.id'))
    descripcion = Column(String(200))

    def __init__(self,tipo_mensaje,codigo_resultado,descripcion):
        self.tipo_mensaje = tipo_mensaje
        self.codigo_resultado = codigo_resultado
        self.descripcion = descripcion

    def __repr__(self):
        salida = "Actividad: \nUsuario: {}\nID: {}\nTipo de actividad: {}\nFecha: {}\nDescripcion:{}\nResultado: {}"\
            .format(self.persona_id,self.id,self.tipo_actividad,self.fecha_creacion,self.descripcion,self.codigo_resultado)
        return salida


class TipoActividad(Base): #carga de billetes, extraccion,etc 
    __tablename__ = "tipoActividad"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(50))
    descripcion = Column(String(150))
    actividad = relationship('Actividad')

    def __init__(self, tipo,descripcion):
        self.tipo = tipo
        self.descripcion = descripcion

    def __repr__(self):
        salida = "Id: {}:\nTipo de actividad: {}\nDescripcion {}".format(
            self.id, self.tipo, self.descripcion)
        return salida

class PersonaDao:
    def __init__(self, db):
        self.db = db

    def guardar(self, persona):
        if self.buscarPorID(persona.id) == None:
            self.db.session.add(persona)
        
        self.db.session.commit()

    def borrar(self, persona):
        self.db.session.delete(persona)
        self.db.session.commit()

    def modificar(self, persona):
        actual = self.db.session.query(Persona).\
            filter_by(id=persona.id).one()
        actual.nombre = persona.nombre
        actual.apellido = persona.apellido
        self.db.session.commit()
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

    def borrar(self, actividad):
        self.db.session.delete(actividad)
        self.db.session.commit()

    def modificar(self, actividad):
        actual = self.db.session.query(Actividad)\
            .filter_by(id=actividad.id).one()
        actual.codigo_resultado = actividad.codigo_resultado
        actual.tipo_mensaje = actividad.tipo_mensaje
        actual.descripcion = actividad.descripcion
        actual.tipo_actividad = actividad.tipo_actividad
        actual.persona_id = actividad.persona_id
        self.db.session.commit()
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


class TipoActividadDao:
    def __init__(self, db):
        self.db = db

    def guardar(self, tipo_actividad):
        self.db.session.add(tipo_actividad)
        self.db.session.commit()

    def borrar(self, tipo_actividad):
        self.db.session.delete(tipo_actividad)
        self.db.session.commit()

    def modificar(self, ta):
        actual = self.db.session.query(TipoActividad)\
            .filter_by(id=ta.id).one()
        actual.tipo_actividad = ta.tipo_actividad
        actual.descripcion = ta.descripcion
        self.db.session.commit()
        return actual

    def buscarPorID(self, id):
        consulta = self.db.session.query(TipoActividad).filter_by(id=id)
        if consulta.count() > 0:
            return consulta.one()
        else:
            return None

    def buscarTodos(self):
        actual = self.db.session.query(TipoActividad).all()
        return actual
