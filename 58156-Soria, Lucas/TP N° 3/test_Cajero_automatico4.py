import unittest
from parameterized import parameterized
from Cajero_automatico import Cajero_automatico
from Cajero_automatico import PorcentajeError, ValorError, CajeroVacioError


class Cajero_automatico_Test4(unittest.TestCase):

    def setUp(self):
        self.caj = Cajero_automatico()

    @parameterized.expand([
        (500, 1000, PorcentajeError),
        (-200, 25, ValorError),
        (200, 10, CajeroVacioError)
    ])
    def test_c(self, monto, porcentaje, error):
        with self.assertRaises(error):
            self.caj.extraer_dinero_cambio(monto, porcentaje)


if __name__ == '__main__':
    unittest.main()
