import unittest
from billete import Billete1000, Billete500, Billete200, Billete100
from cajero import Cajero, MontoError, CombinacionError, MultiplicidadError
from cajero import CantidadError, PorcentajeError, CargaError


class TestCajero(unittest.TestCase):
    def setUp(self):

        self.b1000 = Billete1000()
        self.b500 = Billete500()
        self.b200 = Billete200()
        # Set 1
        self.cajero1 = Cajero()
        billetes1 = []
        for i in range(0, 10):
            billetes1.append(self.b1000)
        self.cajero1.agregar_dinero(billetes1)
        # Set 2
        self.cajero2 = Cajero()
        billetes2 = []
        for i in range(0, 10):
            billetes2.append(self.b1000)
        for i in range(0, 20):
            billetes2.append(self.b500)
        self.cajero2.agregar_dinero(billetes2)
        # Set 3
        self.cajero3 = Cajero()
        billetes3 = []
        for i in range(0, 10):
            billetes3.append(self.b1000)
        for i in range(0, 20):
            billetes3.append(self.b500)
        for i in range(0, 15):
            billetes3.append(self.b200)
        self.cajero3.agregar_dinero(billetes3)

# Test Set 1
    def test_set1_contar(self):
        a = self.cajero1.contar_dinero()
        self.assertEqual(a, "10 billetes de $1000, " +
                            "parcial $10000\n" +
                            "Total $10000")

    def test_set1_extraer1(self):
        b = self.cajero1.extraer_dinero(5000)
        self.assertEqual(b, "5 billetes de $1000\n")

    def test_set1_extraer2(self):
        with self.assertRaises(CantidadError):
            self.cajero1.extraer_dinero(12000)

    def test_set1_extraer3(self):
        with self.assertRaises(MultiplicidadError):
            self.cajero1.extraer_dinero(5520)

    def test_set1_extraer4(self):
        with self.assertRaises(MontoError):
            self.cajero1.extraer_dinero(-5000)

    def test_set1_extraer5(self):
        with self.assertRaises(CombinacionError):
            self.cajero1.extraer_dinero(9100)

    def test_set1_extraer6(self):
        c = self.cajero1.extraer_dinero(10000)
        with self.assertRaises(CargaError):
            self.cajero1.extraer_dinero(5000)

# Test Set 2
    def test_set2_contar(self):
        a = self.cajero2.contar_dinero()
        self.assertEqual(a, "10 billetes de $1000, " +
                            "parcial $10000\n" +
                            "20 billetes de $500, " +
                            "parcial $10000\n" +
                            "Total $20000")

    def test_set2_extraer1(self):
        b = self.cajero2.extraer_dinero(5000)
        self.assertEqual(b, "5 billetes de $1000\n")

    def test_set2_extraer2(self):
        c = self.cajero2.extraer_dinero(12000)
        self.assertEqual(c, "10 billetes de $1000\n" +
                            "4 billetes de $500\n")

    def test_set2_extraer3(self):
        with self.assertRaises(CombinacionError):
            self.cajero2.extraer_dinero(12100)

    def test_set2_extraer4(self):
        e = self.cajero2.extraer_dinero_cambio(7000, 10)
        self.assertEqual(e, "2 billetes de $500\n" +
                            "6 billetes de $1000\n")

    def test_set2_extraer5(self):
        with self.assertRaises(MontoError):
            self.cajero2.extraer_dinero(-5000)

    def test_set2_extraer6(self):
        with self.assertRaises(MultiplicidadError):
            self.cajero2.extraer_dinero(6850)

    def test_set2_extraer7(self):
        with self.assertRaises(CantidadError):
            self.cajero2.extraer_dinero(25000)

    def test_set2_extraer8(self):
        with self.assertRaises(PorcentajeError):
            self.cajero2.extraer_dinero_cambio(7000, -110)
    
    def test_set2_extraer9(self):
        with self.assertRaises(PorcentajeError):
            self.cajero2.extraer_dinero_cambio(7000, 110)

    def test_set2_extraer10(self):
        with self.assertRaises(MontoError):
            self.cajero2.extraer_dinero_cambio(-5000, 10)

    def test_set2_extraer11(self):
        with self.assertRaises(MultiplicidadError):
            self.cajero2.extraer_dinero_cambio(6850, 10)
    
    def test_set2_extraer12(self):
        with self.assertRaises(CantidadError):
            self.cajero2.extraer_dinero_cambio(25000, 10)

    def test_set2_extraer13(self):
        c = self.cajero2.extraer_dinero_cambio(20000, 0)
        with self.assertRaises(CargaError):
            self.cajero2.extraer_dinero_cambio(5000, 0)

    def test_set2_extraer14(self):
        c = self.cajero2.extraer_dinero(20000)
        with self.assertRaises(CargaError):
            self.cajero2.extraer_dinero(5000)

# Test Set 3
    def test_set3_contar(self):
        a = self.cajero3.contar_dinero()
        self.assertEqual(a, "10 billetes de $1000, " +
                            "parcial $10000\n" +
                            "20 billetes de $500, " +
                            "parcial $10000\n" +
                            "15 billetes de $200, " +
                            "parcial $3000\n" +
                            "Total $23000")

    def test_set3_extraer1(self):
        b = self.cajero3.extraer_dinero(5000)
        self.assertEqual(b, "5 billetes de $1000\n")

    def test_set3_extraer2(self):
        c = self.cajero3.extraer_dinero(12000)
        self.assertEqual(c, "10 billetes de $1000\n" +
                            "4 billetes de $500\n")

    def test_set3_extraer3(self):
        with self.assertRaises(CombinacionError):
            self.cajero3.extraer_dinero(12100)

    def test_set3_extraer4(self):
        e = self.cajero3.extraer_dinero_cambio(7000, 10)
        self.assertEqual(e, "5 billetes de $200\n" +
                            "6 billetes de $1000\n")

    def test_set3_extraer5(self):
        with self.assertRaises(MontoError):
            self.cajero3.extraer_dinero(-5000)

    def test_set3_extraer6(self):
        with self.assertRaises(MultiplicidadError):
            self.cajero3.extraer_dinero(6850)
    
    def test_set3_extraer7(self):
        with self.assertRaises(CantidadError):
            self.cajero3.extraer_dinero(25000)

    def test_set3_extraer8(self):
        with self.assertRaises(PorcentajeError):
            self.cajero3.extraer_dinero_cambio(7000, -110)
    
    def test_set3_extraer9(self):
        with self.assertRaises(PorcentajeError):
            self.cajero3.extraer_dinero_cambio(7000, -100)

    def test_set3_extraer10(self):
        with self.assertRaises(MontoError):
            self.cajero3.extraer_dinero_cambio(-5000, 10)

    def test_set3_extraer11(self):
        with self.assertRaises(MultiplicidadError):
            self.cajero3.extraer_dinero_cambio(6850, 10)
    
    def test_set3_extraer12(self):
        with self.assertRaises(CantidadError):
            self.cajero3.extraer_dinero_cambio(25000, 10)

    def test_set3_extraer13(self):
        c = self.cajero3.extraer_dinero_cambio(23000, 0)
        with self.assertRaises(CargaError):
            self.cajero3.extraer_dinero_cambio(5000, 0)

    def test_set3_extraer14(self):
        c = self.cajero3.extraer_dinero(23000)
        with self.assertRaises(CargaError):
            self.cajero3.extraer_dinero(5000)


if __name__ == "__main__":
    unittest.main()