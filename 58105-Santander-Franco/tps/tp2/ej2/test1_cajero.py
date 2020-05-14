import unittest
from billete import Billete1000
from cajero import Cajero, CantidadError, MultiplicidadError, MontoError
from cajero import CombinacionError

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
        with self.assertRaises(CantidadError):
            self.cajero.extraer_dinero(12000)
        # c = self.cajero.extraer_dinero(12000)
        # self.assertEqual(c, "Error. Quiere sacar mas dinero de lo que se
        #                     "puede)

    def test_extraer3(self):
        with self.assertRaises(MultiplicidadError):
            self.cajero.extraer_dinero(5520)
        # d = self.cajero.extraer_dinero(5520)
        # self.assertEqual(d, "Error. El monto es incorrecto")

    def test_extraer4(self):
        # e = self.cajero.extraer_dinero(-5000)
        # self.assertEqual(e, "Error. Ingrese un monto mayor a cero")
        with self.assertRaises(MontoError):
            self.cajero.extraer_dinero(-5000)

    def test_extraer5(self):
        with self.assertRaises(CombinacionError):
            self.cajero.extraer_dinero(9100)


if __name__ == "__main__":
    unittest.main()
