from cajero_automatico import Cajero_automatico 
from billete import Billete,Billete100,Billete200,Billete500,Billete1000 
from excepciones import Monto_mayor, Monto_multiplo, Combinacion_billetes, Porcentaje, Cajero_vacio, Monto_negativo

import unittest


class TestCajero(unittest.TestCase):
    
    def setUp(self):
        self.b100=Billete100()
        self.b200=Billete200()
        self.b500=Billete500()
        self.b1000=Billete1000()
        
        
       
        self.cajero_1 = Cajero_automatico()
        self.cajero_2 = Cajero_automatico()
        self.cajero_3 = Cajero_automatico()
        self.cajero_4 = Cajero_automatico()

        self.lista_billetes_1 = ([self.b1000,self.b1000,self.b1000,
                                    self.b1000,self.b1000,self.b1000,self.b1000,
                                    self.b1000,self.b1000,self.b1000])
        
        self.lista_billetes_2 = ([self.b1000,self.b1000,self.b1000,self.b1000,self.b1000,self.b1000,self.b1000,
                                self.b1000,self.b1000,self.b1000,self.b500,self.b500,self.b500,self.b500,self.b500,
                                self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,
                                self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,]) 

        self.lista_billetes_3 = ([self.b1000,self.b1000,self.b1000,self.b1000,self.b1000,self.b1000,self.b1000,
                                self.b1000,self.b1000,self.b1000,self.b500,self.b500,self.b500,self.b500,self.b500,
                                self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,
                                self.b500,self.b500,self.b500,self.b500,self.b500,self.b500,self.b200,self.b200,self.b200,self.b200,
                                self.b200,self.b200,self.b200,self.b200,self.b200,self.b200,self.b200,self.b200,self.b200,self.b200,self.b200]) 
        
        self.lista_billetes_4 = ([])

        self.cajero_1.agregar_billetes(self.lista_billetes_1)
        self.cajero_2.agregar_billetes(self.lista_billetes_2)
        self.cajero_3.agregar_billetes(self.lista_billetes_3)
        self.cajero_4.agregar_billetes(self.lista_billetes_4)

    #Tests con la lista 1
    def test_contar_dinero_lista_1(self):
        billetes = self.cajero_1.contar_dinero()
        self.assertEqual(billetes, ([0 ,0, 0, 10000], 10000))

    def test_extraer_dinero_lista_1(self):
        billetes = self.cajero_1.extraer_dinero(5000)
        resultado = [i.denominacion for i in billetes]
        self.assertEqual(resultado, [1000,1000,1000,1000,1000])

    def test_error_monto_multiplo_1(self):
        with self.assertRaises(Monto_multiplo):
            self.cajero_1.extraer_dinero(5520)

    def test_error_monto_mayor_lista_1(self):
        with self.assertRaises(Monto_mayor):
            self.cajero_1.extraer_dinero(12000)    

    def test_error_monto_negativo_lista_1(self):
        with self.assertRaises(Monto_negativo):
            self.cajero_1.extraer_dinero(-4000)

    #Tests con la lista 2
    def test_contar_dinero_lista_2(self):
        billetes = self.cajero_2.contar_dinero()
        self.assertEqual(billetes, ([0 ,0, 10000, 10000], 20000))
    
    def test_extraer_dinero_a_lista_2(self):
        billetes = self.cajero_2.extraer_dinero(5000)
        resultado = [i.denominacion for i in billetes]
        self.assertEqual(resultado, [1000,1000,1000,1000,1000])
    
    def test_extraer_dinero_b_lista_2(self):
        billetes = self.cajero_2.extraer_dinero(12000)
        resultado = [i.denominacion for i in billetes]
        self.assertEqual(resultado, [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,500,500,500,500])
    
    def test_error_extraer_combinacion_lista_2(self):
        with self.assertRaises(Combinacion_billetes):
            self.cajero_2.extraer_dinero(12100)
    
    def test_error_monto_multiplo_lista_2(self):
        with self.assertRaises(Monto_multiplo):
            self.cajero_2.extraer_dinero(10560)

    def test_error_monto_negativo_lista_2(self):
        with self.assertRaises(Monto_negativo):
            self.cajero_2.extraer_dinero(-500)

    def test_extraer_dinero_cambio_lista_2(self):
        billetes = self.cajero_2.extraer_dinero_cambio(7000,10)
        resultado = [i.denominacion for i in billetes]
        self.assertEqual(resultado, [500,500,1000,1000,1000,1000,1000,1000])
    
    def test_error_porcentaje_lista_2(self):
        with self.assertRaises(Porcentaje):
            self.cajero_2.extraer_dinero_cambio(7000,250)
    

    #Tests con la lista 3
    def test_contar_dinero_lista_3(self):
        billetes = self.cajero_3.contar_dinero()
        self.assertEqual(billetes, ([0 ,3000, 10000, 10000], 23000))
    
    def test_extraer_dinero_lista_3(self):
        billetes = self.cajero_3.extraer_dinero(5000)
        resultado = [i.denominacion for i in billetes]
        self.assertEqual(resultado, [1000,1000,1000,1000,1000])

    def test_monto_negativo_lista_3(self):
        with self.assertRaises(Monto_negativo):
            self.cajero_3.extraer_dinero(-4000)

    #Tests con la lista 4 (VACIA)
    def test_cajero_vacio_lista_4(self):
        with self.assertRaises(Cajero_vacio):
            self.cajero_4.extraer_dinero(12100)
   


if __name__ == "__main__":
    unittest.main()