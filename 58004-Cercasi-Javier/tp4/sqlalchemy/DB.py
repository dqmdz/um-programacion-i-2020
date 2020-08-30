from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class DBCon:
    def __init__(self):

        # Equipo local con MySQL:
        # str_conexion = 'mysql+pymysql://javi:javi@192.168.0.106:3306/tp4'

        # Contenedor Docker con MySQL
        str_conexion = 'mysql+pymysql://javi:javi@mysql:3306/tp4'

        self.engine = create_engine(str_conexion, echo=False)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.crear_estructura()

    def crear_estructura(self):
        Base.metadata.create_all(self.engine)


class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    tipo = Column(String(100), nullable=False)
    lista_actividades = relationship('Actividad')

    def __init__(self, nombre, apellido, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo

    def __repr__(self):
        resultado = ''
        for reg in self.lista_actividades:
            resultado = resultado+"{}\n".format(reg)
        salida = 'Persona {}: Nombre Completo: {}, {}. Tipo: {}. Lista de Actividades:\n{}'\
            .format(self.id, self.apellido, self.nombre, self.tipo, resultado)
        return salida


class Actividad(Base):
    __tablename__ = "actividad"
    id = Column(Integer, primary_key=True)
    mensaje = Column(String(100))
    tipo_actividad = Column(Integer, ForeignKey('tipo_Actividad.id'))
    codigo_resultado = Column(String(100))
    descripcion_actividad = Column(String(100))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    persona_id = Column(Integer, ForeignKey('persona.id'))

    def __init__(self, mensaje, codigo_resultado, descripcion_actividad):
        self.mensaje = mensaje
        self.codigo_resultado = codigo_resultado
        self.descripcion_actividad = descripcion_actividad

    def __repr__(self):
        salida = "ID: {}. Mensaje: {}. Tipo de actividad: {}. Fecha: {}. Descripcion:{}. Resultado: {}, Usuario: {}".format(
                self.id, self.mensaje, self.tipo_actividad,
                self.fecha_creacion, self.descripcion_actividad,
                self.codigo_resultado, self.persona_id)
        return salida


class TipoActividad(Base):
    __tablename__ = "tipo_Actividad"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(100))
    descripcion = Column(String(100))
    actividad = relationship('Actividad')

    def __init__(self, tipo, descripcion):
        self.tipo = tipo
        self.descripcion = descripcion

    def __repr__(self):
        salida = "ID: {}: Tipo de actividad: {}. Descripcion {}\n".format(
            self.id, self.tipo, self.descripcion)
        return salida


class PersonaDao:
    def __init__(self, db):
        self.db = db
        self.actDao = ActividadDao(self.db)

    def guardar(self, persona):
        person = self.buscarPorID(persona.apellido)
        if person:
            person.lista_actividades.append(persona.lista_actividades[0])
            self.db.session.merge(person)
        else:
            self.db.session.add(persona)
        self.db.session.commit()

    def borrar(self, persona):
        for act in persona.lista_actividades:
            self.actDao.borrar(act)
        self.db.session.delete(persona)
        self.db.session.commit()

    def modificar(self, persona):
        actual = self.db.session.query(Persona).filter_by(id=persona.id).one()
        actual.nombre = persona.nombre
        actual.apellido = persona.apellido
        self.db.session.commit()
        return actual

    def buscarPorID(self, apellido):
        consulta = self.db.session.query(Persona).filter_by(apellido=apellido)
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
        actual = self.db.session.query(Actividad).filter_by(id=actividad.id).one()
        actual.mensaje = actividad.mensaje
        actual.codigo_resultado = actividad.codigo_resultado
        actual.descripcion_actividad = actividad.descripcion_actividad
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

    def modificar(self, t_actividad):
        actual = self.db.session.query(TipoActividad).filter_by(id=t_actividad.id).one()
        actual.tipo_actividad = t_actividad.tipo_actividad
        actual.descripcion = t_actividad.descripcion
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
