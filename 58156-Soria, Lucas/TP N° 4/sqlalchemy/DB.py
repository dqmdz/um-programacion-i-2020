# docker-compose down && docker rmi tpn4_aplicacion:latest
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class DBConexion:
    def __init__(self):
        str_conexion = 'mysql+pymysql://lucas:password@mysql:3306/TP4'
        self.engine = create_engine(str_conexion, echo=True)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.crear_estructura()

    def crear_estructura(self):
        Base.metadata.create_all(self.engine)


class Persona(Base):
    __tablename__ = "Persona"
    dni = Column(Integer, primary_key=True, autoincrement=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100))
    es_empleado = Column(String(10), nullable=False, default="Cliente")
    actividades = relationship('Actividad', backref="Persona")

    def __init__(self, dni, nombre, apellido, empleado):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        if empleado:
            self.es_empleado = "Empleado"
        else:
            self.es_empleado = "Cliente"

    def __repr__(self):
        resultado = ''
        for actividad in self.actividades:
            resultado = resultado + "{}\n".format(actividad)
        salida = 'DNI de la persona: {}\nApellido, nombre: {}, {}.\nEs: {}\n'\
            .format(self.dni, self.apellido, self.nombre, self.es_empleado)
        salida += 'Lista de actividades:\n {}\n'\
            .format(resultado)
        return salida


class Actividad(Base):
    __tablename__ = "Actividad"
    id = Column(Integer, primary_key=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    resultado = Column(String(5), nullable=False)
    mensaje = Column(String(160))
    descripcion = Column(String(280))
    tipo_actividad = Column(Integer, ForeignKey('TipoActividad.id'))
    persona_id = Column(Integer, ForeignKey('Persona.dni'))

    def __init__(self, resultado, mensaje, descripcion, actividad):
        self.mensaje = mensaje
        self.tipo_actividad = actividad
        self.descripcion = descripcion
        if resultado:
            self.resultado = "Exito"
        else:
            self.resultado = "Falla"

    def __repr__(self):
        salida = "Actividad {}:\nTipo de actividad: {}\nRealizada por: {}"\
            .format(self.id, self.tipo_actividad, self.persona_id)
        salida += "Descripcion: {}\nResultado: {}\nMensaje: {}\n"\
            .format(self.descripcion, self.resultado, self.mensaje)
        salida += "Fecha de creacion: {}\n".format(self.fecha_creacion)
        return salida


class TipoActividad(Base):
    __tablename__ = "TipoActividad"
    id = Column(Integer, primary_key=True)
    tipo_actividad = Column(String(160))
    descripcion = Column(String(280))
    actividad = relationship('Actividad')

    def __init__(self, actividad, descripcion):
        self.tipo_actividad = actividad
        self.descripcion = descripcion

    def __repr__(self):
        salida = "Actividad {}:\nTipo de actividad: {}\nDescripcion {}\n"\
            .format(self.id, self.tipo_actividad, self.descripcion)
        return salida


class PersonaDao:
    def __init__(self, db):
        self.db = db

    def guardar(self, persona):
        if self.buscarPorID(persona.dni) is not None:
            actDAO = ActividadDao(self.db)
            obj = persona.actividades[0]
            obj.persona_id = persona.dni
            actDAO.guardar(obj)
            print("El usuario ya existe, guardando actividad")
        else:
            self.db.session.add(persona)
            self.db.session.commit()

    def borrar(self, persona):
        self.db.session.delete(persona)
        self.db.session.commit()

    def modificar(self, persona):
        actual = self.db.session.query(Persona).\
            filter_by(dni=persona.dni).one()
        actual.nombre = persona.nombre
        actual.apellido = persona.apellido
        self.db.session.commit()
        return actual

    def buscarPorID(self, dni):
        consulta = self.db.session.query(Persona).filter_by(dni=dni)
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
        actual.resultado = actividad.resultado
        actual.mensaje = actividad.mensaje
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

    def modificar(self, tipo_de_actividad):
        actual = self.db.session.query(TipoActividad)\
            .filter_by(id=tipo_de_actividad.id).one()
        actual.tipo_actividad = tipo_de_actividad.tipo_actividad
        actual.descripcion = tipo_de_actividad.descripcion
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
