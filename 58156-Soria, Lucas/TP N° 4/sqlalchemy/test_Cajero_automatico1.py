import unittest
from parameterized import parameterized
from Cajero_automatico import Cajero_automatico
from Cajero_automatico import CantidadError
from Cajero_automatico import MultiplicidadError
from Billete import Billete_de_1000


class Cajero_automatico_Test1(unittest.TestCase):

    def setUp(self):
        self.caj = Cajero_automatico()
        self.mil_pesos = Billete_de_1000("pesos", "$")
        self.lista = []
        for x in range(10):
            self.lista.append(self.mil_pesos)
        self.caj.agregar_dinero(self.lista)

    def test_a(self):
        contar = self.caj.contar_dinero()
        self.assertEqual(contar, "10 billetes de $1000, parcial $10000\n" +
                         "Total: $10000")

    def test_b(self):
        extraer = self.caj.extraer_dinero(5000)
        self.assertEqual(extraer, "5 billetes de $1000\n")

    @parameterized.expand([
        (12000, CantidadError),
        (5520, MultiplicidadError)
    ])
    def test_c(self, monto, error):
        with self.assertRaises(error):
            self.caj.extraer_dinero(monto)


if __name__ == '__main__':
    unittest.main()
