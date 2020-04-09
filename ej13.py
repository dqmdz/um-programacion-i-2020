from random import randint

class number():
    def __init__(self):
        self.lista=[]
   
   
    def numeros(self):
        for i in range(10):
            self.lista.append(randint(1,10))
        c=(len(self.lista))
        print("Los numeros son\n", self.lista)
        suma=sum(self.lista)
        print("Dividimos...\n", suma, "/", c)
        print("El promedio es\n", suma/(int(c)))



n=number()
n.numeros()            
        
