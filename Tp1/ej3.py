class entero():
    
    def __init__(self):
       self.entero_positivo = 0 

    def ingresar(self):
        print("ingrese un numero entero positivo")
        self.entero_positivo=int(input(">>"))
    
    def recorrer(self):
        for i in range(1, self.entero_positivo, 2):
            if self.entero_positivo > 0:
                print(i)

lista=entero()

lista.ingresar()
lista.recorrer()
