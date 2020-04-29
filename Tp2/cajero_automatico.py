from Billete import billete_100, billete_200, billete_500, billete_1000
import time



class Cajero_automatico():
    
    def __init__(self):
        self.almacen=[]
        self.total=0
        self.denominacion=[]
        self.lista2=[]
        self.money=0
        self.cambio=0
        self.porcentaje=0
        self.resta=0
        self.lista_act=[]
        self.change=[]
        self.r=0
        self.restaf=0
        self.rest=0

    def agregar_dinero(self, listabillete):
        
        for i in listabillete:
            self.almacen.append(i)
        for item in self.almacen:
            self.total += item.denominacion
            self.denominacion.append(item.denominacion)    
            
            
    def contar_dinero(self):
        
        self.denominacion.sort()
        self.denominacion.reverse()
        
        billete4=str(self.denominacion).count('1000')
        billete3=str(self.denominacion).count('500')
        billete2=str(self.denominacion).count('200')
        billete1=str(self.denominacion).count('100')
        
        muestra=''
        
        for i in self.denominacion:
            if i==1000 and billete4 != 0:
                muestra += "parcial: ${}\n".format(billete4*1000)
                muestra += "{} billetes de $1000\n".format(billete4)
                billete4=0
            if i==500 and billete3 != 0:
                muestra += "parcial: ${}\n".format(billete3*500)
                muestra += "{} billetes de $500\n".format(billete3)
                billete3=0
            if i==200 and billete2 != 0:
                muestra += "parcial: ${}\n".format(billete2*200)
                muestra += "{} billetes de $200\n".format(billete2)
                billete2=0
            if i==100 and billete1 != 0:
                muestra += "parcial: ${}\n".format(billete1*100)
                muestra += "{} billetes de $100\n".format(billete1)
                billete1=0
        muestra += "\ntotal: ${}".format(self.total)               
        return muestra 
       
    def extraer_dinero(self, money, porcentaje):
        
        self.money=money
        self.porcentaje=porcentaje
        while self.money > self.total: 
            return "Error. Quiero sacar mas dinero de lo que puedo"
        while self.money % 100 != 0: 
            return "Error. El monto es incorrecto"
            
        self.cambio = self.money * self.porcentaje/100
        round(self.cambio)
    
        self.resta=self.money-self.cambio
        self.restaf=self.resta
        
        self.denominacion.sort()
        self.denominacion.reverse()
        for i in self.denominacion:
            if self.resta / i >= 1:
                self.resta -= i
                self.lista2.append(i)
        while sum(self.lista2) < self.restaf:
            return 'Error. No hay una combinación de billetes que nos permita extraer ese monto'
        
        
        self.cambio + self.resta
       
        print("Usted desea: ${}\n".format(self.money))
        billete4=str(self.lista2).count('1000')
        billete3=str(self.lista2).count('500')
        billete2=str(self.lista2).count('200')
        billete1=str(self.lista2).count('100')
        
        muestra=''
        
        for i in self.lista2:
            if i==1000 and billete4 != 0:
                muestra += "{} billetes de $1000\n".format(billete4)
                billete4=0
            if i==500 and billete3 != 0:
                muestra += "{} billetes de $500\n".format(billete3)
                billete3=0
            if i==200 and billete2 != 0:
                muestra += "{} billetes de $200\n".format(billete2)
                billete2=0
            if i==100 and billete1 != 0:
                muestra += "{} billetes de $100\n".format(billete1)
                billete1=0
                     
        return muestra         
         
    def extraer_dinero_cambio(self):
        self.function=self.cambio + self.resta
        
        
        self.denominacion.reverse()
        
        for i in self.denominacion:
            if self.function / i >= 1:
                self.function -= i
              
                self.change.append(i)
            
        for i in self.lista2:
            self.change.append(i)
        
           
        billete4=str(self.change).count('1000')
        billete3=str(self.change).count('500')
        billete2=str(self.change).count('200')
        billete1=str(self.change).count('100')
        
        muestra=''
        
        for i in self.change:
            if i==1000 and billete4 != 0:
                muestra += "{} billetes de $1000\n".format(billete4)
                billete4=0
            if i==500 and billete3 != 0:
                muestra += "{} billetes de $500\n".format(billete3)
                billete3=0
            if i==200 and billete2 != 0:
                muestra += "{} billetes de $200\n".format(billete2)
                billete2=0
            if i==100 and billete1 != 0:
                muestra += "{} billetes de $100\n".format(billete1-billete4)
                billete1=0
                     
        return muestra         

    def final(self):

        
        for i in self.change:
            if i==100:
               self.denominacion.remove(100)
            if i==200:
               self.denominacion.remove(200)
            if i==500:
               self.denominacion.remove(500)
            if i==1000:
               self.denominacion.remove(1000)  

        
        print("\nimprimiendo, espere...\n")
        time.sleep(3)
        print(self.change)
        

        billete4=str(self.denominacion).count('1000')
        billete3=str(self.denominacion).count('500')
        billete2=str(self.denominacion).count('200')
        billete1=str(self.denominacion).count('100')


        print("\nCantidad de Billetes actualizada:\n")
        for i in self.denominacion:
            if i==1000 and billete4 != 0:
                print("{} billetes de $1000\n".format(billete4))
                billete4=0
            if i==500 and billete3 != 0:
                print("{} billetes de $500\n".format(billete3))
                billete3=0
            if i==200 and billete2 != 0:
                print("{} billetes de $200\n".format(billete2))
                billete2=0
            if i==100 and billete1 != 0:
                print("{} billetes de $100\n".format(billete1))
                billete1=0
        print("\ntotal: ${}".format(sum(self.denominacion)))               


        
       