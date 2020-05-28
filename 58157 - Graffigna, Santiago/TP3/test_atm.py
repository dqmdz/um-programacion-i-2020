from billetes import Billete_100, Billete_200, Billete_500, Billete_1000
from atm import Cajero_Automatico, FondosInsuficientes, NoMultiplo, SinBilletes, ExtraccionInvalida
import unittest

class TestCajero_Automatico(unittest.TestCase):

    def setUp(self):

        self.doscientos = Billete_200()
        self.quinientos = Billete_500()
        self.mil = Billete_1000()

        self.atm_cero = Cajero_Automatico()
        self.atm_a = Cajero_Automatico()
        self.atm_b = Cajero_Automatico()
        self.atm_c = Cajero_Automatico()

        self.cero = []
        self.diezK = [self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil]
        self.veinteK = [self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos]
        self.veintitresK = [self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.mil, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.quinientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos, self.doscientos]

        self.atm_cero.agregar_billetes(self.cero)
        self.atm_a.agregar_billetes(self.diezK)
        self.atm_b.agregar_billetes(self.veinteK)
        self.atm_c.agregar_billetes(self.veintitresK)


    #Primer set de pruebas-----------------------------------------------------------------
    def test_contar_billetes_diezK(self):
        contar = self.atm_a.contar_billetes()
        self.assertEqual(contar, (0, 0, 0, 0, 0, 0, 10, 10000, 10000))


    def test_extraer_5K(self):
        self.atm_a.contar_billetes()
        extraer_cinco = self.atm_a.extraer_dinero(5000)
        self.assertEqual(5000, extraer_cinco)

    def test_extraer_mas_de_lo_que_hay_A(self):
        self.atm_a.contar_billetes()
        with self.assertRaises(FondosInsuficientes):
            self.atm_a.extraer_dinero(100000)

    def test_extraer_monto_no_multiplo_A(self):
        self.atm_a.contar_billetes()
        with self.assertRaises(NoMultiplo):
            self.atm_a.extraer_dinero(2001)

    def test_sin_dinero_ABC(self):
        self.atm_cero.contar_billetes()
        with self.assertRaises(SinBilletes):
            self.atm_cero.extraer_dinero(1000)

    def test_sin_dinero_combinacion_A(self):
        self.atm_a.contar_billetes()
        with self.assertRaises(SinBilletes):
            self.atm_a.extraer_dinero(100)
            self.atm_a.extraer_dinero_cambio()

    def test_monto_negativo_A(self):
        self.atm_a.contar_billetes()
        with self.assertRaises(ExtraccionInvalida):
            self.atm_a.extraer_dinero(-1000)


    #Segundo set de pruebas----------------------------------------------------------------------------------------------------------------------------
    def test_contar_billetes_diezK_B(self):
        contar = self.atm_b.contar_billetes()
        self.assertEqual(contar, (0, 0, 0, 0, 20, 10000, 10, 10000, 20000))

    def test_extraer_5K_B(self):
        self.atm_b.contar_billetes()
        extraer_cinco = self.atm_b.extraer_dinero(5000)
        self.assertEqual(5000, extraer_cinco)

    def test_extraer_12K_B(self):
        self.atm_b.contar_billetes()
        extraer_doce = self.atm_b.extraer_dinero(12000)
        self.assertEqual(extraer_doce, 12000)


    def test_extraer_mas_de_lo_que_hay_B(self):
        self.atm_b.contar_billetes()
        with self.assertRaises(FondosInsuficientes):
            self.atm_b.extraer_dinero(100000)

    def test_extraer_monto_no_multiplo_B(self):
        self.atm_b.contar_billetes()
        with self.assertRaises(NoMultiplo):
            self.atm_b.extraer_dinero(2001)

    def test_monto_negativo_B(self):
        self.atm_b.contar_billetes()
        with self.assertRaises(ExtraccionInvalida):
            self.atm_b.extraer_dinero(-1000)

    def test_sin_dinero_combinacion_B(self):
        self.atm_b.contar_billetes()
        with self.assertRaises(SinBilletes):
            self.atm_b.extraer_dinero(100)
            self.atm_b.extraer_dinero_cambio()


    #Tercer set de pruebas----------------------------------------------------------------------------------------------------------------------------
    def test_contar_billetes_C(self):
        money = self.atm_c.contar_billetes()
        self.assertEqual(money, (0, 0, 15, 3000, 20, 10000, 10, 10000, 23000))
        (0, 0, 15, 3000, 20, 10000, 10, 10000, 23000)

    def test_extraer_C(self):
        self.atm_c.contar_billetes()
        extraer_cinco = self.atm_c.extraer_dinero(5000)
        self.assertEqual(5000, extraer_cinco)

    def test_extraer_monto_no_multiplo_C(self):
        self.atm_c.contar_billetes()
        with self.assertRaises(NoMultiplo):
            self.atm_c.extraer_dinero(2001)

    def test_extraer_mas_de_lo_que_hay_C(self):
        self.atm_c.contar_billetes()
        with self.assertRaises(FondosInsuficientes):
            self.atm_c.extraer_dinero(100000)

    def test_monto_negativo_C(self):
        self.atm_c.contar_billetes()
        with self.assertRaises(ExtraccionInvalida):
            self.atm_c.extraer_dinero(-1000)

    def test_sin_dinero_combinacion_C(self):
        self.atm_c.contar_billetes()
        with self.assertRaises(SinBilletes):
            self.atm_c.extraer_dinero(100)
            self.atm_c.extraer_dinero_cambio()


if __name__ == "__main__":
    unittest.main() 
    