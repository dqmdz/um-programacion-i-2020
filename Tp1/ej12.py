from random import randint

class numeros():
    def __init__(self):
        self.lista=[]
        self.diccionario={}


    def generar_enteros(self):
        
        for i in range(5):
            
            self.lista.append(randint(1,10))
        print(self.lista)   
        self.lista.sort()  
        self.lista.reverse()  
        self.diccionario['valor aleatorio'] = self.lista    
        print(self.diccionario)

                    
            
num = numeros()

num.generar_enteros()