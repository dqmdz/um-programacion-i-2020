import unittest
from billete import Billete1000, Billete500, Billete200
from cajero import Cajero, MontoError, CombinacionError, MultiplicidadError
from cajero import CantidadError, PorcentajeError


class TestCajero(unittest.TestCase):
    def setUp(self):

        self.b1000 = Billete1000()
        self.b500 = Billete500()
        self.b200 = Billete200()
        self.cajero = Cajero()
        billetes = []
        for i in range(0, 10):
            billetes.append(self.b1000)
        for i in range(0, 20):
            billetes.append(self.b500)
        for i in range(0, 15):
            billetes.append(self.b200)
        self.cajero.agregar_dinero(billetes)

    def test_contar(self):
        a = self.cajero.contar_dinero()
        self.assertEqual(a, "10 billetes de $1000, " +
                            "parcial $10000\n" +
                            "20 billetes de $500, " +
                            "parcial $10000\n" +
                            "15 billetes de $200, " +
                            "parcial $3000\n" +
                            "Total $23000")

    def test_extraer1(self):
        b = self.cajero.extraer_dinero(5000)
        self.assertEqual(b, "5 billetes de $1000\n")

    def test_extraer2(self):
        c = self.cajero.extraer_dinero(12000)
        self.assertEqual(c, "10 billetes de $1000\n" +
                            "4 billetes de $500\n")

    def test_extraer3(self):
        # d = self.cajero.extraer_dinero(12100)
        # self.assertEqual(d, "Error. No hay una combinacion de billetes"
        #                     " que nos permita extraer ese monto.")
        with self.assertRaises(CombinacionError):
            self.cajero.extraer_dinero(12100)

    def test_extraer4(self):
        e = self.cajero.extraer_dinero_cambio(7000, 10)
        self.assertEqual(e, "5 billetes de $200\n" +
                            "6 billetes de $1000\n")

    def test_extraer5(self):
        with self.assertRaises(MontoError):
            self.cajero.extraer_dinero(-5000)

    def test_extraer6(self):
        with self.assertRaises(MultiplicidadError):
            self.cajero.extraer_dinero(6850)
    
    def test_extraer7(self):
        with self.assertRaises(CantidadError):
            self.cajero.extraer_dinero(25000)

    def test_extraer8(self):
        with self.assertRaises(PorcentajeError):
            self.cajero.extraer_dinero_cambio(7000, -110)
    
    def test_extraer9(self):
        with self.assertRaises(PorcentajeError):
            self.cajero.extraer_dinero_cambio(7000, -100)

    def test_extraer10(self):
        with self.assertRaises(MontoError):
            self.cajero.extraer_dinero_cambio(-5000, 10)

    def test_extraer11(self):
        with self.assertRaises(MultiplicidadError):
            self.cajero.extraer_dinero_cambio(6850, 10)
    
    def test_extraer12(self):
        with self.assertRaises(CantidadError):
            self.cajero.extraer_dinero_cambio(25000, 10)

if __name__ == "__main__":
    unittest.main()
