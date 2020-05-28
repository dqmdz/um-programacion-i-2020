from cajero_automatico import Cajero_automatico
from billete import Billete_100,Billete_1000,Billete_200,Billete_500,Billete_1000
import unittest
import os
from errores import multiploError, dineroInsuficiente, imposibleExtraer, porcentajeCambio, extraccionNegativa, cajeroVacio

class TestCajero(unittest.TestCase):
    os.system("reset")

    def setUp(self):
        self.billete100=Billete_100(100,"Pesos")
        self.billete200=Billete_200(200,"Pesos")
        self.billete500=Billete_500(500,"Pesos")
        self.billete1000=Billete_1000(1000,"Pesos")
        
        self.cajero=Cajero_automatico()

        self.lista1=[]
        for i in range(10):
            self.lista1.append(self.billete1000)
        
        self.lista2=[]
        for i in range(10):
            self.lista2.append(self.billete1000)
        for i in range(20):
            self.lista2.append(self.billete500)
        
        self.lista3=[]
        for i in range(10):
            self.lista3.append(self.billete1000)
        for i in range(20):
            self.lista3.append(self.billete500)
        for i in range(15):
            self.lista3.append(self.billete200)

    #Set de pruebas 1
    def test1_contardinero(self):
        self.cajero.agregar_dinero(self.lista1)
        self.assertEqual(self.cajero.contar_dinero(),([0,0,0,10000],10000))
        self.cajero.vaciar_cajero()

    def test1_extraerdinero(self):
        self.cajero.agregar_dinero(self.lista1)
        b1000=self.billete1000
        lista_entrega=[]
        for i in range(5):
            lista_entrega.append(b1000)
        self.assertEqual(self.cajero.extraer_dinero(5000),lista_entrega)
        self.cajero.vaciar_cajero()
    
    def test1_extraerdinero2(self):
        self.cajero.agregar_dinero(self.lista1)
        with self.assertRaises(dineroInsuficiente):
            self.cajero.extraer_dinero(12000)
        self.cajero.vaciar_cajero()
    
    def test1_extraerdinero3(self):
        self.cajero.agregar_dinero(self.lista1)
        with self.assertRaises(multiploError):
            self.cajero.extraer_dinero(5520)
        self.cajero.vaciar_cajero()

    #Set de pruebas 2
    def test2_contardinero(self):
        self.cajero.agregar_dinero(self.lista2)
        self.assertEqual(self.cajero.contar_dinero(),([0,0,10000,10000],20000))
        self.cajero.vaciar_cajero()
    
    def test2_extraerdinero(self):
        self.cajero.agregar_dinero(self.lista2)
        lista_entrega=[]
        for i in range(5):
            lista_entrega.append(self.billete1000)
        self.assertEqual(self.cajero.extraer_dinero(5000),lista_entrega)
        self.cajero.vaciar_cajero()

    def test2_extraerdinero2(self):
        self.cajero.agregar_dinero(self.lista2)
        lista_entrega=[]
        for i in range(10):
            lista_entrega.append(self.billete1000)
        for i in range(4):
            lista_entrega.append(self.billete500)
        self.assertEqual(self.cajero.extraer_dinero(12000),lista_entrega)
        self.cajero.vaciar_cajero()

    def test2_extraerdinero3(self):
        self.cajero.agregar_dinero(self.lista2)
        with self.assertRaises(imposibleExtraer):
            self.cajero.extraer_dinero(12100)
        self.cajero.vaciar_cajero()

    def test2_extraerdinero_cambio(self):
        self.cajero.agregar_dinero(self.lista2)
        lista_entrega=[]
        lista_entrega_cambio=[]
        for i in range(2):
            lista_entrega_cambio.append(self.billete500)
        for i in range(6):
            lista_entrega.append(self.billete1000)
        self.assertEqual(self.cajero.extraer_dinero_cambio(7000,10),(lista_entrega,lista_entrega_cambio))
        self.cajero.vaciar_cajero()

    #Set de prueba 3
    def test3_contardinero(self):
        self.cajero.agregar_dinero(self.lista3)
        self.assertEqual(self.cajero.contar_dinero(),([0,3000,10000,10000],23000))
        self.cajero.vaciar_cajero()
    
    def test3_extraerdinero(self):
        self.cajero.agregar_dinero(self.lista3)
        lista_entrega=[]
        for i in range(5):
            lista_entrega.append(self.billete1000)
        self.assertEqual(self.cajero.extraer_dinero(5000),lista_entrega)
        self.cajero.vaciar_cajero()
    
    def test3_extraerdinero2(self):
        self.cajero.agregar_dinero(self.lista3)
        lista_entrega=[]
        for i in range(10):
            lista_entrega.append(self.billete1000)
        for i in range(4):
            lista_entrega.append(self.billete500)
        self.assertEqual(self.cajero.extraer_dinero(12000),lista_entrega)
        self.cajero.vaciar_cajero()
    
    def test3_extraerdinero3(self):
        self.cajero.agregar_dinero(self.lista3)
        with self.assertRaises(imposibleExtraer):
            self.cajero.extraer_dinero(12100)
        self.cajero.vaciar_cajero()
    
    def test3_extraerdinero_cambio(self):
        self.cajero.agregar_dinero(self.lista3)
        lista_entrega=[]
        lista_entrega_cambio=[]
        for i in range(4):
            lista_entrega_cambio.append(self.billete200)
        for i in range(6):
            lista_entrega.append(self.billete1000)
        lista_entrega.append(self.billete200)
        self.assertEqual(self.cajero.extraer_dinero_cambio(7000,10),(lista_entrega,lista_entrega_cambio))
        self.cajero.vaciar_cajero()

    #set de prueba 4 -> para probar nuevas excepciones incorporadas
    def test4_extraerdinero(self):
        with self.assertRaises(cajeroVacio):
            self.cajero.extraer_dinero(100)
    
    def test4_extraerdinero1(self):
        with self.assertRaises(extraccionNegativa):
            self.cajero.extraer_dinero(-500)
    
    def test4_extraerdinero_cambio(self):
        self.cajero.agregar_dinero(self.lista1)
        with self.assertRaises(porcentajeCambio):
            self.cajero.extraer_dinero_cambio(1000,120)
        self.cajero.vaciar_cajero()
    
    def test4_extraerdinero_cambio2(self):
        self.cajero.agregar_dinero(self.lista1)
        with self.assertRaises(porcentajeCambio):
            self.cajero.extraer_dinero_cambio(1000,-20)
        self.cajero.vaciar_cajero()


if __name__ == "__main__":
    unittest.main()
