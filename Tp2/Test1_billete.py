import unittest
from Billete import billete_100, billete_200, billete_500, billete_1000
from cajero_automatico import Cajero_automatico
from parameterized import parameterized
mil = billete_1000(1000,'pesos','$1000') 

class Test_Cajero_1(unittest.TestCase):

    def setUp(self):
        self.ingreso = Cajero_automatico()
        self.lista=[]
        for x in range(10):
            self.lista.append(mil)
        self.ingreso.agregar_dinero(self.lista)
                            

#TEST 1:
    def test_a(self):
        
        conteo = self.ingreso.contar_dinero()
        self.assertEqual(conteo, 'parcial: $10000\n' + '10 billetes de $1000\n' + '\ntotal: $10000')
    
    def test_b(self):
        
        num = self.ingreso.extraer_dinero(5000,0)
        self.assertEqual(num, '5 billetes de $1000\n')
    
    def test_c(self):    
        
        error1 = self.ingreso.extraer_dinero(12000,0)
        self.assertEqual(error1, 'Error. Quiero sacar mas dinero de lo que puedo')
    
    def test_d(self):    
       
        error2 = self.ingreso.extraer_dinero(5520,0)
        self.assertEqual(error2, 'Error. El monto es incorrecto')



if __name__ == '__main__':
    unittest.main()


                                      