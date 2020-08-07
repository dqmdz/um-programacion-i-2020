from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class DBCon:
    def __init__(self):
        str_conexion = 'mysql+pymysql://lucas:password@'
        str_conexion += 'mysql:3306/TP4'
        self.engine = create_engine(str_conexion, echo=True)

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
    es_empleado = Column(String(10), nullable=False, default="Cliente")
    actividades = relationship('Actividad', backref="Persona")

    def __init__(self, nombre, apellido, empleado):
        self.nombre = nombre
        self.apellido = apellido
        if empleado:
            self.es_empleado = "Empleado"
        else:
            self.es_empleado = "Cliente"
        self.actividades = None

    def __repr__(self):
        resultado = ''
        for actividad in self.actividades:
            resultado = resultado + "{}\n".format(actividad)
        salida = 'Persona {}: \nApellido, nombre: {}, {}.\nEs: {}\n'\
            .format(self.id, self.apellido, self.nombre, self.es_empleado)
        salida += 'Lista de actividades:\n {}'\
            .format(resultado)
        return salida


class Actividad(Base):
    __tablename__ = "Actividad"
    id = Column(Integer, primary_key=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    resultado = Column(String(5), nullable=False, default=True)
    tipo_actividad = Column(Integer, ForeignKey('TipoActividad.id'))
    persona_id = Column(Integer, ForeignKey('Persona.id'))

    def __init__(self, resultado):
        if resultado:
            self.resultado = "Exito"
        else:
            self.resultado = "Falla"
        self.actividades = None

    def __repr__(self):
        salida = "Actividad {}: actividad: {}. Creado el {}".format(
            self.id, self.actividad, self.fecha_creacion)
        return salida


class TipoActividad(Base):
    __tablename__ = "tipo_actividad"
    id = Column(Integer, primary_key=True)
    tipo_actividad = Column(String(160))
    descripcion = Column(String(280))
    actividad = relationship('Actividad')

    def __init__(self, actividad):
        self.tipo_de_actividad = actividad

    def __repr__(self):
        salida = "Actividad {}:\nTipo de actividad: {}\nDescripcion {}".format(
            self.id, self.tipo_actividad, self.descripcion)
        return salida
