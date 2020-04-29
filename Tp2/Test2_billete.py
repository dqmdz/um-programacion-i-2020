import unittest
from Billete import billete_100, billete_200, billete_500, billete_1000
from cajero_automatico import Cajero_automatico
from parameterized import parameterized
mil = billete_1000(1000,'pesos','$1000')
quinientos = billete_500(500,'pesos','$500') 

class Test_Cajero_1(unittest.TestCase):

    def setUp(self):
        self.cargo = Cajero_automatico()
        self.lista=[]
        for i in range(10):
            self.lista.append(mil)
            self.lista.append(quinientos)
            self.lista.append(quinientos)
        self.cargo.agregar_dinero(self.lista)   
        
        
                            

#TEST 2:
    def test_a(self):
        
        conteo = self.cargo.contar_dinero()
        self.assertEqual(conteo, 'parcial: $10000\n' + '10 billetes de $1000\n' + 'parcial: $10000\n' + '20 billetes de $500\n' + '\ntotal: $20000')
    
    def test_b(self):
        
        num = self.cargo.extraer_dinero(5000,0)
        self.assertEqual(num, '5 billetes de $1000\n')
    
    def test_c(self):    
        
        billetes = self.cargo.extraer_dinero(12000,0)
        self.assertEqual(billetes, '10 billetes de $1000\n' + '4 billetes de $500\n')
    
    def test_d(self):    
       
        error = self.cargo.extraer_dinero(12100,0)
        self.assertEqual(error, 'Error. No hay una combinación de billetes que nos permita extraer ese monto')
    
    def test_e(self):    
        
        self.cargo.extraer_dinero(7000,10)
        billetes2=self.cargo.extraer_dinero_cambio()
        self.assertEqual(billetes2, '2 billetes de $500\n' + '6 billetes de $1000\n')


if __name__ == '__main__':
    unittest.main()