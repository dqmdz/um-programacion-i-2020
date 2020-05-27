import unittest
from Billete import (Billete_100, Billete_1000, Billete_200,
                     Billete_500)
from Cajero_Mejorado import (Cajero, CajeroMejorado, MultipoError, ExcesoError,
                             NegativoError, CombinacionError, VacioError,
                             RangoError)


class TestBanco(unittest.TestCase):

    def setUp(self):
        self.cajero = Cajero()
        self.mejora = CajeroMejorado()
        self.deposito1 = [Billete_1000(), Billete_1000(), Billete_1000(),
                          Billete_1000(), Billete_1000(), Billete_1000(),
                          Billete_1000(), Billete_1000(), Billete_1000(),
                          Billete_1000()]

        self.deposito2 = [Billete_500(), Billete_500(), Billete_500(),
                          Billete_500(), Billete_500(), Billete_500(),
                          Billete_500(), Billete_500(), Billete_500(),
                          Billete_500(), Billete_500(), Billete_500(),
                          Billete_500(), Billete_500(), Billete_500(),
                          Billete_500(), Billete_500(), Billete_500(),
                          Billete_500(), Billete_500()]

        self.deposito3 = [Billete_200(), Billete_200(), Billete_200(),
                          Billete_200(), Billete_200(), Billete_200(),
                          Billete_200(), Billete_200(), Billete_200(),
                          Billete_200(), Billete_200(), Billete_200(),
                          Billete_200(), Billete_200(), Billete_200()]

    def test_deposito_10000(self):
        self.cajero.carga(self.deposito1)
        self.assertEqual(self.cajero.conteo(), (10000, 0, 0, 0, 10000))
        self.cajero.vaciado()

    def test_extraccion_5000_correcta(self):
        self.cajero.carga(self.deposito1)
        self.assertEqual(self.cajero.conteo(), (10000, 0, 0, 0, 10000))
        self.assertEqual(self.cajero.extraer(5000), (5, 0, 0, 0))
        self.cajero.vaciado()

    def test_extraccion_12000_incorrecta(self):
        with self.assertRaises(ExcesoError):
            self.cajero.carga(self.deposito1)
            self.assertEqual(self.cajero.conteo(), (10000, 0, 0, 0, 10000))
            self.cajero.extraer(12000)
            self.cajero.vaciado()

    def test_extraccion_5520_incorrecta(self):
        with self.assertRaises(MultipoError):
            self.cajero.carga(self.deposito1)
            self.assertEqual(self.cajero.conteo(), (10000, 0, 0, 0, 10000))
            self.cajero.extraer(5520)
            self.cajero.vaciado()

    def test_deposito_20000(self):
        self.cajero.carga(self.deposito1 + self.deposito2)
        self.assertEqual(self.cajero.conteo(), (10000, 10000, 0, 0, 20000))
        self.cajero.vaciado()

    def test_extraer_5000_de_20000(self):
        self.cajero.carga(self.deposito1 + self.deposito2)
        self.assertEqual(self.cajero.conteo(), (10000, 10000, 0, 0, 20000))
        self.assertEqual(self.cajero.extraer(5000), (5, 0, 0, 0))
        self.cajero.vaciado()

    def test_extraccion_12000_de_20000(self):
        self.cajero.carga(self.deposito1 + self.deposito2)
        self.assertEqual(self.cajero.conteo(), (10000, 10000, 0, 0, 20000))
        self.assertEqual(self.cajero.extraer(12000), (10, 4, 0, 0))
        self.cajero.vaciado()

    def test_extraccion_12100_de_20000(self):
        self.cajero.carga(self.deposito1 + self.deposito2)
        self.assertEqual(self.cajero.conteo(), (10000, 10000, 0, 0, 20000))
        with self.assertRaises(CombinacionError):
            self.cajero.extraer(12100)
        self.cajero.vaciado()

    def test_extraccion_7000_de_20000(self):
        self.mejora.carga(self.deposito1 + self.deposito2)
        self.assertEqual(self.mejora.conteo(), (10000, 10000, 0, 0, 20000))
        self.assertEqual(self.mejora.extraer_dinero_cambio(7000, 10.0),
                                                          (6, 2, 0, 0))
        self.cajero.vaciado()

    def test_extraccion_7000_cambio_exceso(self):
        self.mejora.carga(self.deposito1 + self.deposito2)
        self.assertEqual(self.mejora.conteo(), (10000, 10000, 0, 0, 20000))
        with self.assertRaises(RangoError):
            self.mejora.extraer_dinero_cambio(7000, 500.0)
        self.cajero.vaciado()

    def test_extraccion_7000_cambio_negativo(self):
        self.mejora.carga(self.deposito1 + self.deposito2)
        self.assertEqual(self.mejora.conteo(), (10000, 10000, 0, 0, 20000))
        with self.assertRaises(RangoError):
            self.mejora.extraer_dinero_cambio(7000, -3)
        self.cajero.vaciado()

    def test_deposito_23000(self):
        self.cajero.carga(self.deposito1 + self.deposito2 + self.deposito3)
        self.assertEqual(self.cajero.conteo(), (10000, 10000, 3000, 0, 23000))
        self.cajero.vaciado()

    def test_extraer_5000_de_23000(self):
        self.cajero.carga(self.deposito1 + self.deposito2 + self.deposito3)
        self.assertEqual(self.cajero.conteo(), (10000, 10000, 3000, 0, 23000))
        self.assertEqual(self.cajero.extraer(5000), (5, 0, 0, 0))
        self.cajero.vaciado()

    def test_extraer_5000_sin_fondos(self):
        with self.assertRaises(VacioError):
            self.cajero.extraer(5000)

    def test_extraccion_7000_cambio_sin_fondos(self):
        with self.assertRaises(VacioError):
            self.mejora.extraer_dinero_cambio(7000, 10.0)

    def test_extraccion_12000_de_23000(self):
        self.cajero.carga(self.deposito1 + self.deposito2 + self.deposito3)
        self.assertEqual(self.cajero.conteo(), (10000, 10000, 3000, 0, 23000))
        self.assertEqual(self.cajero.extraer(12000), (10, 4, 0, 0))
        self.cajero.vaciado()

    def test_extraccion_12100_de_23000(self):
        with self.assertRaises(CombinacionError):
            self.cajero.carga(self.deposito1 + self.deposito2 + self.deposito3)
            self.assertEqual(self.cajero.conteo(), (10000, 10000, 3000, 0,
                                                    23000))
            self.cajero.extraer(12100)
            self.cajero.vaciado()

    def test_extraccion_7000_de_23000(self):
        self.mejora.carga(self.deposito1 + self.deposito2 + self.deposito3)
        self.assertEqual(self.mejora.conteo(), (10000, 10000, 3000, 0, 23000))
        self.assertEqual(self.mejora.extraer_dinero_cambio(7000, 10.0),
                                                          (6, 0, 5, 0))
        self.mejora.vaciado()

    def test_negativo_cambio_7000_de_23000(self):
        with self.assertRaises(NegativoError):
            self.mejora.carga(self.deposito1 + self.deposito2 + self.deposito3)
            self.assertEqual(self.mejora.conteo(), (10000, 10000, 3000, 0,
                                                    23000))
            self.mejora.extraer_dinero_cambio(-7000, 10.0)
            self.mejora.vaciado()

    def test_negativo_7000_de_23000(self):
        with self.assertRaises(NegativoError):
            self.mejora.carga(self.deposito1 + self.deposito2 + self.deposito3)
            self.assertEqual(self.mejora.conteo(), (10000, 10000, 3000, 0,
                                                    23000))
            self.mejora.extraer(-7000)
            self.mejora.vaciado()

    def test_extraccion_8000_de_23000(self):
        self.mejora.carga(self.deposito1 + self.deposito2 + self.deposito3)
        self.assertEqual(self.mejora.conteo(), (10000, 10000, 3000, 0, 23000))
        self.assertEqual(self.mejora.extraer_dinero_cambio(8000, 10.0),
                                                          (7, 0, 5, 0))
        self.cajero.vaciado()


if __name__ == '__main__':
    unittest.main()
