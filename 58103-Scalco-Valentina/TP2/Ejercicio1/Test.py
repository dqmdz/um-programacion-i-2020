import unittest
from Cajero import Atm
from Billetes import Billete_1000, Billete_500, Billete_200, Billete_100


class TestAtm(unittest.TestCase):
    def setUp(self):
        self.cien = Billete_100("pesos", "$")
        self.docientos = Billete_200("pesos", "$")
        self.quinientos = Billete_500("pesos", "$")
        self.onek = Billete_1000("pesos", "$")
        self.atm1 = Atm()
        self.atm2 = Atm()
        self.atm3 = Atm()

        lista_billetes = []
        lista_billetes = [self.onek for valor in range(0, 10)]
        self.atm1.agregar_dinero(lista_billetes)
        self.atm2.agregar_dinero(lista_billetes)
        self.atm3.agregar_dinero(lista_billetes)

        lista_billetes = [self.quinientos for valor in range(0, 20)]
        self.atm2.agregar_dinero(lista_billetes)

        for i in range(0, 15):
            lista_billetes.append(self.docientos)
        self.atm3.agregar_dinero(lista_billetes)

    def test_set_1_a(self):
        resultado = ["0 billetes de $100, Parcial $0",
            "0 billetes de $200, Parcial $0", "0 billetes de $500, Parcial $0",
            "10 billetes de $1000, Parcial $10000", "Total: $10000"]
        self.assertEqual(self.atm1.contar_dinero(), resultado)

    def test_set_1_b(self):
        self.assertEqual(self.atm1.extraer_dinero(5000), ["5 billetes de $1000"])

    def test_set_1_c(self):
        error = "Error. Monto no válido, ingrese un monto menor"
        self.assertEqual(self.atm1.extraer_dinero(12000), error)

    def test_set_1_d(self):
        error = "Error. Monto no válido, ingrese un monto multiplo de 100"
        self.assertEqual(self.atm1.extraer_dinero(5520), error)

    def test_set_2_a(self):
        resultado = ["0 billetes de $100, Parcial $0",
                    "0 billetes de $200, Parcial $0", "20 billetes de $500, Parcial $10000",
                    "10 billetes de $1000, Parcial $10000", "Total: $20000"]
        self.assertEqual(self.atm2.contar_dinero(), resultado)

    def test_set_2_b(self):
        self.assertEqual(self.atm2.extraer_dinero(5000), ["5 billetes de $1000", "0 billetes de $500"])

    def test_set_2_c(self):
        self.assertEqual(self.atm2.extraer_dinero(12000), ["10 billetes de $1000",
            "4 billetes de $500"])

    def test_set_2_d(self):
        error = "Error. No hay una combinación de billetes que nos permita extraer ese monto"
        self.assertEqual(self.atm2.extraer_dinero(12100), error)

    def test_set_3_a(self):
        resultado = ["0 billetes de $100, Parcial $0",
            "15 billetes de $200, Parcial $3000", "20 billetes de $500, Parcial $10000",
            "10 billetes de $1000, Parcial $10000", "Total: $23000"]
        self.assertEqual(self.atm3.contar_dinero(), resultado)

    def test_set_3_b(self):
        self.assertEqual(self.atm3.extraer_dinero(5000), ["5 billetes de $1000", "0 billetes de $500", "0 billetes de $200"])

    def test_set_3_c(self):
        self.assertEqual(self.atm3.extraer_dinero(12000), ["10 billetes de $1000", "4 billetes de $500", "0 billetes de $200"])

    def test_set_3_d(self):
        error = "Error. No hay una combinación de billetes que nos permita extraer ese monto"
        self.assertEqual(self.atm3.extraer_dinero(12100), error)


if __name__ == '__main__':
    unittest.main()
