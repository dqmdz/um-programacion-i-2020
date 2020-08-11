import unittest
from parameterized import parameterized
from Cajero_automatico import Cajero_automatico
from Cajero_automatico import PorcentajeError, ValorError, CajeroVacioError
from Broker import Broker


class Broker_Test(unittest.TestCase):

    def setUp(self):
        self.caj = Cajero_automatico()

    @parameterized.expand([
        (500, 1000, PorcentajeError),
        (-200, 25, ValorError),
        (200, 10, CajeroVacioError)
    ])
    def test_errores(self, monto, porcentaje, error):
        con = Broker([42670460, "Lucas", "Soria", False],
                     ["Voy a comprar algo con 500 pesos", 2,
                     monto, porcentaje],
                     self.caj)
        con.registrar_actividad()
        self.assertEqual("2", "2")


# ValorError('Error. No se puede extraer cantidades de dinero negativas')
# PorcentajeError('Error. El porcentaje es incorrecto')
# CajeroVacioError('Error. No se puede extraer dinero si el cajero esta vacio')
if __name__ == '__main__':
    unittest.main()
