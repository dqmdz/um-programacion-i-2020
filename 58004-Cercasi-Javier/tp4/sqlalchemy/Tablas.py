from DB import (TipoActividad, Persona, PersonaDao, Actividad, ActividadDao,
                DBCon, TipoActividadDao)
from Cajero_Mejorado import (Cajero, CajeroMejorado)
from Billete import (Billete_100, Billete_1000, Billete_200,
                     Billete_500)


class Tablas():

    def __init__(self, nombre, apellido, tipo, mensaje, codigo, tipo_act,
                 dinero):

        self.db = DBCon()
        # Persona:
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo

        # Actividad:
        self.mensaje = mensaje
        self.codigo = codigo
        # Tipo_actividad:
        self.tipo_actividad = tipo_act
        # Dinero:
        self.dinero = dinero
        # Tipos:
        self.persona = ''
        self.generar_tipos()

    def generar_tipos(self):

        tipo = TipoActividadDao(self.db)

        if len(tipo.buscarTodos()) == 0:

            self.t1 = TipoActividad("Deposito", "Ingreso de dinero al banco")
            self.t2 = TipoActividad("Extracción", "Se extrae dinero del banco")
            self.t3 = TipoActividad("Extracción con cambio",
                                    "Se extrae dinero con cambio del banco")

            tipo.guardar(self.t1)
            tipo.guardar(self.t2)
            tipo.guardar(self.t3)
        self.generar_personas()

    def generar_personas(self):
        self.persona_dao = PersonaDao(self.db)
        self.persona = Persona(self.nombre, self.apellido, self.tipo)
        self.banco()

    def banco(self):

        self.deposito1 = [Billete_1000(), Billete_1000(), Billete_1000(),
                          Billete_500(), Billete_500(), Billete_500(),
                          Billete_200(), Billete_200(), Billete_200(),
                          Billete_100(), Billete_100()]
        self.cajero = Cajero()
        self.mejora = CajeroMejorado()

        if self.tipo_actividad == "t1":
            self.cajero.carga(self.dinero)
            self.resultado = "Se ha depositado $"+str(self.cajero.conteo()[-1])

        elif self.tipo_actividad == "t2":
            self.cajero.carga(self.deposito1)
            self.cajero.conteo()
            self.resultado = self.cajero.extraer(self.dinero[0])[-1]

        elif self.tipo_actividad == "t3":
            self.mejora.carga(self.deposito1)
            self.mejora.conteo()
            self.resultado = self.mejora.extraer_dinero_cambio(self.dinero[0],
                                                               self.dinero[1])[-1]

        self.generar_actividades()

    def generar_actividades(self):
        actividadDao = ActividadDao(self.db)
        tipodao = TipoActividadDao(self.db)
        if self.tipo_actividad == "t1":

            actividades = Actividad(self.mensaje, self.codigo, self.resultado)
            tipo1 = tipodao.buscarPorID(1)

        if self.tipo_actividad == "t2":
            actividades = Actividad(self.mensaje, self.codigo, self.resultado)
            tipo1 = tipodao.buscarPorID(2)

        if self.tipo_actividad == "t3":
            actividades = Actividad(self.mensaje, self.codigo, self.resultado)
            tipo1 = tipodao.buscarPorID(3)

        actividades.tipo_actividad = tipo1.id
        actividadDao.guardar(actividades)

        (self.persona).lista_actividades.append(actividades)
        self.persona_dao.guardar(self.persona)
