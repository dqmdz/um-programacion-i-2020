import unittest
from parameterized import parameterized
from Cajero_automatico import Cajero_automatico
from Billete import Billete_de_1000, Billete_de_500
from Broker import Broker
from DB import ActividadDao


class Broker_Test(unittest.TestCase):

    def setUp(self):
        self.caj = Cajero_automatico()
        self.mil_pesos = Billete_de_1000("pesos", "$")
        self.quinientos_pesos = Billete_de_500("pesos", "$")

    @parameterized.expand([
        (500, 1000, "Error. El porcentaje es incorrecto"),
        (-200, 25, "Error. No se puede extraer cantidades de "
                   "dinero negativas"),
        (200, 10, "Error. No se puede extraer dinero si el cajero esta vacio")
    ])
    def test_errores_de_actividades_porcentaje(self, monto, porcentaje, error):
        broker = Broker([42670460, "Lucas", "Soria", False],
                        ["Voy a comprar algo con 500 pesos", 2,
                         monto, porcentaje], self.caj)
        broker.registrar_actividad()
        actDAO = ActividadDao(broker.db)
        actividades = actDAO.buscarTodos()
        actividad = actividades[0]
        actDAO.borrar(actividades[0])
        self.assertEqual(actividad.mensaje, error)

    @parameterized.expand([
        (12000, "Error. No se puede extraer mas dinero del"
         " que hay disponible en el cajero"),
        (5520, "Error. No se puede extraer dinero que"
         " no sea múltiplo de 100")
    ])
    def test_errores_de_actividades(self, monto, error):
        broker = Broker([42670460, "Lucas", "Soria", False],
                        ["Voy a comprar algo con 500 pesos", 1,
                         monto], self.caj)
        self.lista = []
        for x in range(6):
            self.lista.append(self.mil_pesos)
        self.lista.append(self.quinientos_pesos)
        self.caj.agregar_dinero(self.lista)
        broker.registrar_actividad()
        actDAO = ActividadDao(broker.db)
        actividades = actDAO.buscarTodos()
        actividad = actividades[0]
        actDAO.borrar(actividades[0])
        self.assertEqual(actividad.mensaje, error)

    @parameterized.expand([
        (5000, "5 billetes de $1000\n"),
        (12000, "10 billetes de $1000\n4 billetes de $500\n")
    ])
    def test_sin_cambio_sin_error(self, monto, respuesta):
        broker = Broker([42670460, "Lucas", "Soria", False],
                        ["Voy a comprar algo con 500 pesos", 1,
                         monto], self.caj)
        self.lista = []
        for x in range(10):
            self.lista.append(self.mil_pesos)
        for x in range(4):
            self.lista.append(self.quinientos_pesos)
        self.caj.agregar_dinero(self.lista)
        broker.registrar_actividad()
        actDAO = ActividadDao(broker.db)
        actividades = actDAO.buscarTodos()
        actividad = actividades[0]
        actDAO.borrar(actividades[0])
        self.assertEqual(actividad.mensaje, respuesta)

    @parameterized.expand([
        (7000, 10, "2 billetes de $500\n6 billetes de $1000\n")
    ])
    def test_con_cambio_sin_error(self, monto, porcentaje, respuesta):
        broker = Broker([42670460, "Lucas", "Soria", False],
                        ["Voy a comprar algo con 500 pesos", 2,
                         monto, porcentaje], self.caj)
        self.lista = []
        for x in range(17):
            self.lista.append(self.mil_pesos)
        self.lista.append(self.quinientos_pesos)
        self.lista.append(self.quinientos_pesos)
        self.caj.agregar_dinero(self.lista)
        broker.registrar_actividad()
        actDAO = ActividadDao(broker.db)
        actividades = actDAO.buscarTodos()
        actividad = actividades[0]
        actDAO.borrar(actividades[0])
        self.assertEqual(actividad.mensaje, respuesta)

    def test_contar(self):
        broker = Broker([42670460, "Lucas", "Soria", False],
                        ["Voy a comprar algo con 500 pesos", 3,
                         ], self.caj)
        broker.registrar_actividad()
        actDAO = ActividadDao(broker.db)
        actividades = actDAO.buscarTodos()
        actividad = actividades[0]
        actDAO.borrar(actividades[0])
        self.assertEqual(actividad.mensaje,
                         "Total: $0")

    def test_error_billetes(self):
        broker = Broker([42670460, "Lucas", "Soria", False],
                        ["Voy a comprar algo con 500 pesos", 1,
                         12100], self.caj)
        self.lista = []
        for x in range(17):
            self.lista.append(self.mil_pesos)
        self.caj.agregar_dinero(self.lista)
        broker.registrar_actividad()
        actDAO = ActividadDao(broker.db)
        actividades = actDAO.buscarTodos()
        actividad = actividades[0]
        actDAO.borrar(actividades[0])
        self.assertEqual(actividad.mensaje, "Error. No hay una combinación"
                                            " de billetes que nos permita"
                                            " extraer ese monto")

    def test_insertar(self):
        self.lista = []
        for x in range(17):
            self.lista.append(self.mil_pesos)
        broker = Broker([42670460, "Lucas", "Soria", False],
                        ["Voy a comprar algo con 500 pesos", 4,
                         self.lista], self.caj)
        broker.registrar_actividad()
        actDAO = ActividadDao(broker.db)
        actividades = actDAO.buscarTodos()
        actividad = actividades[0]
        actDAO.borrar(actividades[0])
        self.assertEqual(actividad.mensaje, "Se ingreso dinero correctamente")


if __name__ == '__main__':
    unittest.main()
