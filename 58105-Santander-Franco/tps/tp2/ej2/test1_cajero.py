import unittest
from billete import Billete1000
from cajero import Cajero


class TestCajero(unittest.TestCase):
    def setUp(self):

        self.b1000 = Billete1000()
        self.cajero = Cajero()
        billetes = []
        for i in range(0, 10):
            billetes.append(self.b1000)
        self.cajero.agregar_dinero(billetes)

    def test_contar(self):
        a = self.cajero.contar_dinero()
        self.assertEqual(a, "10 billetes de $1000, " +
                            "parcial $10000\n" +
                            "Total $10000")

    def test_extraer1(self):
        b = self.cajero.extraer_dinero(5000)
        self.assertEqual(b, "5 billetes de $1000\n")

    def test_extraer2(self):
        c = self.cajero.extraer_dinero(12000)
        self.assertEqual(c, "Error. Quiere sacar mas dinero de lo que se puede"
                         )

    def test_extraer3(self):
        d = self.cajero.extraer_dinero(5520)
        self.assertEqual(d, "Error. El monto es incorrecto")


if __name__ == "__main__":
    unittest.main()
