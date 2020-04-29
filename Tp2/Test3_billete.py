import unittest
from Billete import billete_100, billete_200, billete_500, billete_1000
from cajero_automatico import Cajero_automatico
from parameterized import parameterized
mil = billete_1000(1000,'pesos','$1000')
quinientos = billete_500(500,'pesos','$500')
doscientos = billete_200(200,'pesos','$200')  


class Test_Cajero_1(unittest.TestCase):

    def setUp(self):
        self.lastcargo = Cajero_automatico()
        self.lista=[]
        for i in range(10):
            self.lista.append(mil)
            self.lista.append(quinientos)
            self.lista.append(quinientos)
            self.lista.append(doscientos)
        for i in range(5):
            self.lista.append(doscientos)
        self.lastcargo.agregar_dinero(self.lista)   
#Test3:
    def test_a(self):
        
        conteo = self.lastcargo.contar_dinero()
        self.assertEqual(conteo, 'parcial: $10000\n' + '10 billetes de $1000\n' + 'parcial: $10000\n' + '20 billetes de $500\n' + 'parcial: $3000\n' + '15 billetes de $200\n' + '\ntotal: $23000')    
    
    def test_b(self):
        
        num = self.lastcargo.extraer_dinero(5000,0)
        self.assertEqual(num, '5 billetes de $1000\n') 
    
    def test_c(self):    
        
        billetes = self.lastcargo.extraer_dinero(12000,0)
        self.assertEqual(billetes, '10 billetes de $1000\n' + '4 billetes de $500\n')
   
    def test_d(self):    
       
        error = self.lastcargo.extraer_dinero(12100,0)
        self.assertEqual(error, 'Error. No hay una combinación de billetes que nos permita extraer ese monto')
    
    def test_e(self):    
        
        self.lastcargo.extraer_dinero(7000,10)
        billetes2=self.lastcargo.extraer_dinero_cambio()
        self.assertEqual(billetes2, '5 billetes de $200\n' + '6 billetes de $1000\n')
   
           


if __name__ == '__main__':
    unittest.main()      