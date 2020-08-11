from DB import DBConexion, Persona, Actividad, TipoActividad
from DB import PersonaDao, TipoActividadDao
# from DB import PersonaDao, ActividadDao, TipoActividadDao


class Controlador:

    def __init__(self, datos_persona, datos_actividad, caj):
        # Instancias del cajero y base de datos
        self.db = DBConexion()
        self.cajero = caj
        # Generar los tipos de actividad si no existen
        self.generar_tipos()
        # Toma de datos
        self.datos_actividad = datos_actividad
        self.datos_persona = datos_persona
        # Hacer la actividad que se desea

    # TipoActividad: tipo_actividad, descripcion
    def generar_tipos(self):
        tipoDAO = TipoActividadDao(self.db)
        tipos = tipoDAO.buscarTodos()
        if len(tipos) == 0:
            # Definicion de los Tipos de Actividades
            t1 = TipoActividad("Extracción",
                               "Se extrae sierta cantidad de dinero del" +
                               " cajero automatico")
            t2 = TipoActividad("Extracción con cambio",
                               "Se extrae sierta cantidad de dinero del" +
                               " cajero automatico, empezando por los " +
                               "billetes mas pequeños")
            t3 = TipoActividad("Consulta",
                               "Se consulta la cantidad de dinero disponible" +
                               " en el cajero")
            t4 = TipoActividad("Inserción",
                               "Se inserta sierta cantidad de dinero al" +
                               " cajero automatico")

            # Guardar tipos en la Base de Datos
            tipoDAO.guardar(t1)
            tipoDAO.guardar(t2)
            tipoDAO.guardar(t3)
            tipoDAO.guardar(t4)

    def usar_cajero(self):
        if self.datos_actividad[1] == 1:
            msn = self.cajero.extraer_dinero(self.datos_actividad[2])
        elif self.datos_actividad[1] == 2:
            msn = self.cajero.extraer_dinero_cambio(self.datos_actividad[2],
                                                    self.datos_actividad[3])
        elif self.datos_actividad[1] == 3:
            msn = self.cajero.contar_dinero()
        elif self.datos_actividad[1] == 4:
            self.cajero.agregar_dinero(self.datos_actividad[2])
            msn = "Se ingreso dinero correctamente"
        else:
            return "El inidice del tipo de actividad no es correcto"
        return msn

    # Registro de la actividad en la base de datos
    def registrar_actividad(self):
        resultado = True
        try:
            mensaje = self.usar_cajero()
        except Exception as e:
            resultado = False
            mensaje = e
        personaDAO = PersonaDao(self.db)
        # def __init__(self, resultado, mensaje, descripcion, actividad):
        # Definicion de los datos de la actividad
        act_descripcion = self.datos_actividad[0]
        act_actividad = self.datos_actividad[1]
        # Crea actividad
        a = Actividad(resultado, mensaje, act_descripcion, act_actividad)
        # def __init__(self, dni, nombre, apellido, empleado):
        # Definicion de los datos de la persona
        per_dni = self.datos_persona[0]
        per_nombre = self.datos_persona[1]
        per_apellido = self.datos_persona[2]
        per_empleado = self.datos_persona[3]
        # Crea persona
        per = Persona(per_dni, per_nombre, per_apellido, per_empleado)
        per.actividades.append(a)
        # Guarda las actividades de la persona
        personaDAO.guardar(per)
