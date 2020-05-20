import unittest
from parameterized import parameterized
from Cajero_automatico import Cajero_automatico
from Cajero_automatico import BilleteError
from Billete import Billete_de_1000, Billete_de_500, Billete_de_200


class Cajero_automatico_Test3(unittest.TestCase):

    def setUp(self):
        self.caj = Cajero_automatico()
        self.mil_pesos = Billete_de_1000("pesos", "$")
        self.quinientos_pesos = Billete_de_500("pesos", "$")
        self.doscientos_pesos = Billete_de_200("pesos", "$")
        self.lista = []
        for x in range(10):
            self.lista.append(self.mil_pesos)
            self.lista.append(self.quinientos_pesos)
            self.lista.append(self.quinientos_pesos)
            self.lista.append(self.doscientos_pesos)
        for x in range(5):
            self.lista.append(self.doscientos_pesos)
        self.caj.agregar_dinero(self.lista)

    def test_a(self):
        contar = self.caj.contar_dinero()
        self.assertEqual(contar, "10 billetes de $1000, parcial $10000\n" +
                                 "20 billetes de $500, parcial $10000\n" +
                                 "15 billetes de $200, parcial $3000\n" +
                                 "Total: $23000")

    @parameterized.expand([
        (5000, "5 billetes de $1000\n"),
        (12000, "10 billetes de $1000\n4 billetes de $500\n")
    ])
    def test_b(self, monto, respuesta):
        extraer = self.caj.extraer_dinero(monto)
        self.assertEqual(extraer, respuesta)

    def test_c(self):
        with self.assertRaises(BilleteError):
            self.caj.extraer_dinero(12100)

    @parameterized.expand([
        (7000, 10, "5 billetes de $200\n6 billetes de $1000\n")
    ])
    def test_d(self, monto, porcentaje, respuesta):
        self.caj.agregar_dinero(self.lista)
        extraer = self.caj.extraer_dinero_cambio(monto, porcentaje)
        self.assertEqual(extraer, respuesta)


if __name__ == '__main__':
    unittest.main()
