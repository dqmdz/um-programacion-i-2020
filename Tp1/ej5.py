class numbers(): 
    def __init__(self):
        self.impar=1
        self.lista=[]
    
    def ingresar(self):
        print("ingrese un numero entero")
        self.impar=int(input(">>"))

    def incremento(self):

        for i in range(1, self.impar, 2):
                self.lista.append(i)
                self.lista.sort()
                self.lista.reverse()
                print(self.lista)

imp=numbers()

imp.ingresar()
imp.incremento()

        
