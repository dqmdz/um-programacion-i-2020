import unittest
from billete import Billete1000, Billete500, Billete200
from cajero import CargaError, Cajero


class TestCajero(unittest.TestCase):
    def setUp(self):
        self.b1000 = Billete1000()
        self.b500 = Billete500()
        self.b200 = Billete200()
        self.cajero = Cajero()
        billetes = [0, 0, 0, 0]
        self.cajero.agregar_dinero(billetes)

    def test_extraer1(self):
        with self.assertRaises(CargaError):
            self.cajero.extraer_dinero(5000)


if __name__ == "__main__":
    unittest.main()
