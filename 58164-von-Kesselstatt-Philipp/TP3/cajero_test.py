import unittest
from cajero import Cajero
from billetes import Billete100
from billetes import Billete200
from billetes import Billete500
from billetes import Billete1000


class CajeroTest(unittest.TestCase):
    def setUp(self):
        self.primerSet = Cajero()
        self.segundoSet = Cajero()
        self.tercerSet = Cajero()
        self.empty = Cajero()

        billetera1 = [Billete1000() for item in range(10)]

        billetera2 = [Billete1000() for item in range(10)]
        billetera2 += [Billete500() for item in range(20)]

        billetera3 = [Billete1000() for item in range(10)]
        billetera3 += [Billete500() for item in range(20)]
        billetera3 += [Billete200() for item in range(15)]

        self.primerSet.agregar_dinero(billetera1)
        self.segundoSet.agregar_dinero(billetera2)
        self.tercerSet.agregar_dinero(billetera3)

    def test_cajero_vacio(self):

        with self.assertRaises(Exception):
            self.empty.extraer_dinero(100)

    def test_contar_a(self):
        dinero_contado = self.primerSet.contado_imprimir()
        self.assertEqual(dinero_contado,
                         "pesos:\n" +
                         "10 billetes de $1000 parcial $10000\n\n" +
                         "Total:10000")

    def test_extraer_bien_a(self):
        billetes = self.primerSet.extraer_dinero(5000, 0)
        ext = [i.getRepresentacion() for i in billetes]
        self.assertEqual(ext, ["$1000", "$1000", "$1000", "$1000", "$1000"])

    def test_extraer_mucho_a(self):
        self.assertRaises(Exception,
                          self.primerSet.extraer_dinero,
                          **{"monto": 12000, "porcentaje_cambio": 0})

    def test_extraer_mal_a(self):
        self.assertRaises(Exception,
                          self.primerSet.extraer_dinero,
                          **{"monto": 5520, "porcentaje_cambio": 0})

    def test_contar_b(self):
        dinero_contado = self.segundoSet.contado_imprimir()
        self.assertEqual(dinero_contado,
                         "pesos:\n" +
                         "10 billetes de $1000 parcial $10000\n" +
                         "20 billetes de $500 parcial $10000\n\n" +
                         "Total:20000")

    def test_extraer_bien_b(self):
        billetes = self.segundoSet.extraer_dinero(5000, 0)
        ext = [i.getRepresentacion() for i in billetes]
        self.assertEqual(ext, ["$1000", "$1000", "$1000", "$1000", "$1000"])

    def test_extraer_bien2_b(self):
        billetes = self.segundoSet.extraer_dinero(12000, 0)
        ext = [i.getRepresentacion() for i in billetes]
        self.assertEqual(ext, ["$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$500", "$500", "$500", "$500"])

    def test_extraer_mal_b(self):
        self.assertRaises(Exception,
                          self.segundoSet.extraer_dinero,
                          **{"monto": 12100, "porcentaje_cambio": 0})

    def test_extraer_cambio_b(self):
        billetes = self.segundoSet.extraer_dinero(7000, 10)
        ext = [i.getRepresentacion() for i in billetes]
        self.assertEqual(ext, ["$500", "$500", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000"])

    def test_contar_c(self):
        dinero_contado = self.tercerSet.contado_imprimir()
        self.assertEqual(dinero_contado,
                         "pesos:\n" +
                         "10 billetes de $1000 parcial $10000\n" +
                         "20 billetes de $500 parcial $10000\n" +
                         "15 billetes de $200 parcial $3000\n\n"
                         "Total:23000")

    def test_extraer_bien_c(self):
        billetes = self.tercerSet.extraer_dinero(5000, 0)
        ext = [i.getRepresentacion() for i in billetes]
        self.assertEqual(ext, ["$1000", "$1000", "$1000", "$1000", "$1000"])

    def test_extraer_bien2_c(self):
        billetes = self.tercerSet.extraer_dinero(12000, 0)
        ext = [i.getRepresentacion() for i in billetes]
        self.assertEqual(ext, ["$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$500", "$500", "$500", "$500"])

    def test_extraer_mal_c(self):
        self.assertRaises(Exception,
                          self.tercerSet.extraer_dinero,
                          **{"monto": 12100, "porcentaje_cambio": 0})

    def test_extraer_cambio_c(self):
        billetes = self.tercerSet.extraer_dinero(7000, 10)
        ext = [i.getRepresentacion() for i in billetes]
        self.assertEqual(ext, ["$200", "$200", "$200", "$200", "$1000", "$1000", "$1000", "$1000", "$1000", "$1000", "$200"])


if __name__ == '__main__':
    unittest.main()
