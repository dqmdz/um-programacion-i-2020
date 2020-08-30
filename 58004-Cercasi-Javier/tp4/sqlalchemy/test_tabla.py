import unittest
from Billete import (Billete_100, Billete_1000, Billete_200,
                     Billete_500)
from Cajero_Mejorado import (Cajero, CajeroMejorado)

from Tablas import Tablas
from DB import (TipoActividad, Persona, PersonaDao, Actividad, ActividadDao,
                DBCon, TipoActividadDao)


class TestTablas(unittest.TestCase):

    def setUp(self):
        self.db = DBCon()
        self.persona_dao = PersonaDao(self.db)
        self.actDao = ActividadDao(self.db)
        self.tipodao = TipoActividadDao(self.db)
        self.cajero = Cajero()
        self.mejora = CajeroMejorado()

    def test_deposito_2000(self):

        tablas = Tablas("Juan", "Gomez", "Empleado", "Informacion",
                        "Exitoso", "t1",
                        [Billete_1000(), Billete_1000()])

        tabla_p = self.persona_dao.buscarPorID(0)
        self.assertEqual(tabla_p.nombre, "Juan")
        self.assertEqual(tabla_p.apellido, "Gomez")
        self.assertEqual(tabla_p.tipo, "Empleado")

        tabla_a = self.actDao.buscarTodos()[0]

        self.assertEqual(tabla_a.mensaje, "Informacion")
        self.assertEqual(tabla_a.codigo_resultado, "Exitoso")
        self.assertEqual(tabla_a.descripcion_actividad, "Se ha depositado $2000")

        tabla_t = self.tipodao.buscarTodos()[1-1]       # Por t1 (fila i=0)
        self.assertEqual(tabla_t.descripcion, "Ingreso de dinero al banco")
        self.persona_dao.borrar(tabla_p)
        self.cajero.vaciado()

    def test_deposito_3500(self):

        tablas = Tablas("Juan", "Cruz", "Gerente", "Informacion",
                        "Exitoso", "t1",
                        [Billete_1000(), Billete_1000(), Billete_200(),
                         Billete_200(), Billete_1000(), Billete_100()])

        tabla_p = self.persona_dao.buscarPorID(0)
        self.assertEqual(tabla_p.nombre, "Juan")
        self.assertEqual(tabla_p.apellido, "Cruz")
        self.assertEqual(tabla_p.tipo, "Gerente")

        tabla_a = self.actDao.buscarTodos()[0]

        self.assertEqual(tabla_a.mensaje, "Informacion")
        self.assertEqual(tabla_a.codigo_resultado, "Exitoso")
        self.assertEqual(tabla_a.descripcion_actividad, "Se ha depositado $3500")

        tabla_t = self.tipodao.buscarTodos()[1-1]       # Por t1 (fila i=0)
        self.assertEqual(tabla_t.descripcion, "Ingreso de dinero al banco")
        self.persona_dao.borrar(tabla_p)
        self.cajero.vaciado()

    def test_extraccion_500(self):

        tablas = Tablas("Raul", "Fuentes", "Cliente", "Informacion",
                        "Exitoso", "t2",
                        [500, 0])

        tabla_p = self.persona_dao.buscarPorID(0)
        self.assertEqual(tabla_p.nombre, "Raul")
        self.assertEqual(tabla_p.apellido, "Fuentes")
        self.assertEqual(tabla_p.tipo, "Cliente")

        tabla_a = self.actDao.buscarTodos()[0]

        self.assertEqual(tabla_a.mensaje, "Informacion")
        self.assertEqual(tabla_a.codigo_resultado, "Exitoso")
        self.assertEqual(tabla_a.descripcion_actividad,
                         "Se extrajo sin cambio $500")

        tabla_t = self.tipodao.buscarTodos()[2-1]       # Por t2 (fila i=1)
        self.assertEqual(tabla_t.descripcion,
                         "Se extrae dinero del banco")
        self.persona_dao.borrar(tabla_p)
        self.mejora.vaciado()

    def test_extraccion_3300(self):

        tablas = Tablas("Javi", "Cercasi", "Cliente", "Informacion",
                        "Exitoso", "t2",
                        [3300, 0])

        tabla_p = self.persona_dao.buscarPorID(0)
        self.assertEqual(tabla_p.nombre, "Javi")
        self.assertEqual(tabla_p.apellido, "Cercasi")
        self.assertEqual(tabla_p.tipo, "Cliente")

        tabla_a = self.actDao.buscarTodos()[0]

        self.assertEqual(tabla_a.mensaje, "Informacion")
        self.assertEqual(tabla_a.codigo_resultado, "Exitoso")
        self.assertEqual(tabla_a.descripcion_actividad,
                         "Se extrajo sin cambio $3300")

        tabla_t = self.tipodao.buscarTodos()[2-1]       # Por t2 (fila i=1)
        self.assertEqual(tabla_t.descripcion,
                         "Se extrae dinero del banco")
        self.persona_dao.borrar(tabla_p)
        self.mejora.vaciado()

    def test_extraccion_con_cambio(self):

        tablas = Tablas("Rodrigo", "Bueno", "Cantante", "Informacion",
                        "Exitoso", "t3",
                        [3800, 10])

        tabla_p = self.persona_dao.buscarPorID(0)
        self.assertEqual(tabla_p.nombre, "Rodrigo")
        self.assertEqual(tabla_p.apellido, "Bueno")
        self.assertEqual(tabla_p.tipo, "Cantante")

        tabla_a = self.actDao.buscarTodos()[0]

        self.assertEqual(tabla_a.mensaje, "Informacion")
        self.assertEqual(tabla_a.codigo_resultado, "Exitoso")
        self.assertEqual(tabla_a.descripcion_actividad,
                         "Se extrajo con cambio $3800")

        tabla_t = self.tipodao.buscarTodos()[3-1]       # Por t3 (fila i=2)
        self.assertEqual(tabla_t.descripcion,
                         "Se extrae dinero con cambio del banco")
        self.persona_dao.borrar(tabla_p)
        self.mejora.vaciado()


if __name__ == '__main__':
    unittest.main()
