import unittest
from cajeroAutomarico import Cajero, dineroIsuficiente, notMultiplo, billetesInsuficientes, dineroNegativo, rangoCambio, sinBilletes
from billete import Billetes, Billete100, Billete200, Billete500, Billete1000

class Test_Cajero(unittest.TestCase):

    def setUp(self):
        self.cien = Billete100()
        self.docientos = Billete200()
        self.quinientos = Billete500()
        self.mil = Billete1000()

        listaP = []
        self.cajero1 = Cajero()
        for i in range(0, 10):
            listaP.append(self.mil)
        self.cajero1.agregarDinero(listaP)

        listaP2 = []
        self.cajero2 = Cajero()
        for i in range(0, 10):
            listaP2.append(self.mil)
        for i in range(0, 20):
            listaP2.append(self.quinientos)
        self.cajero2.agregarDinero(listaP2)

        listaP3 = []
        self.cajero3 = Cajero()
        for i in range(0, 10):
            listaP3.append(self.mil)
        for i in range(0, 20):
            listaP3.append(self.quinientos)
        for i in range(0, 15):
            listaP3.append(self.docientos)
        self.cajero3.agregarDinero(listaP3)

        listaP4 = []
        self.cajero4 = Cajero()
        self.cajero4.agregarDinero(listaP4)
    
    def test1_contar(self):

        self.assertEqual(self.cajero1.contarDinero(), (0, 0, 0, 10, 0, 0, 0, 10000, 10000))

    def test1_extraer(self):

        self.cajero1.contarDinero()
        self.assertEqual(self.cajero1.extraerDinero(5000), [1000, 1000, 1000, 1000, 1000])

    def test1_extraccionErronea(self):

        self.cajero1.contarDinero()
        with self.assertRaises(dineroIsuficiente):
            self.cajero1.extraerDinero(11000)

    def test1_extraccionErronea2(self):
        
        self.cajero1.contarDinero()
        with self.assertRaises(notMultiplo):
            self.cajero1.extraerDinero(5520)

    def test2_contar(self):
        
        self.assertEqual(self.cajero2.contarDinero(), (0, 0, 20, 10, 0, 0, 10000, 10000, 20000))

    def test2_extraer(self):

        self.cajero2.contarDinero()
        self.assertEqual(self.cajero2.extraerDinero(5000), [1000, 1000, 1000, 1000, 1000])

    def test2_extraer2(self):

        self.cajero2.contarDinero()
        self.assertEqual(self.cajero2.extraerDinero(12000), [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 500, 500, 500, 500])

    def test2_error(self):

        self.cajero2.contarDinero()
        with self.assertRaises(billetesInsuficientes):
            self.cajero2.extraerDinero(12100)
      
    def test2_extraerConcambio(self):

        self.cajero2.contarDinero()
        resultado = self.cajero2.extraerDineroCambio(7000, 0.1)
        self.assertEqual(resultado, [500, 500, 1000, 1000, 1000, 1000, 1000, 1000])

    def test3_contar(self):
        
        self.assertEqual(self.cajero3.contarDinero(), (0, 15, 20, 10, 0, 3000, 10000, 10000, 23000))

    def test3_extraer(self):

        self.cajero3.contarDinero()
        self.assertEqual(self.cajero3.extraerDinero(5000), [1000, 1000, 1000, 1000, 1000])
    
    def test3_extraer2(self):

        self.cajero3.contarDinero()
        self.assertEqual(self.cajero3.extraerDinero(12000), [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 500, 500, 500, 500])

    def test3_error(self):

        self.cajero3.contarDinero()
        with self.assertRaises(billetesInsuficientes):
            self.cajero3.extraerDinero(12100)

    def test3_cambio(self):

        self.cajero3.contarDinero()
        resultado = self.cajero3.extraerDineroCambio(7000, 0.1)
        self.assertEqual(resultado, [200, 200, 200, 200, 1000, 1000, 1000, 1000, 1000, 1000, 200])

    def test_negativo(self):
        
        self.cajero3.contarDinero()
        with self.assertRaises(dineroNegativo):
            self.cajero3.extraerDinero(-1000)

    def test_errorCambio(self):
        
        self.cajero3.contarDinero()
        with self.assertRaises(rangoCambio):
            self.cajero3.extraerDineroCambio(7000, 1.1)

    def test_sinBilletes(self):
        
        with self.assertRaises(sinBilletes):
            self.cajero4.contarDinero()



if __name__ == "__main__":
        unittest.main()
