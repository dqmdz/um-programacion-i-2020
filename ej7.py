class frase_letra():
    def __init__(self):
        self.lista=''
        self.letra=''
    
    def encontrar(self):
        self.lista=input("ingrese una frase\n")
        self.letra=input("ingrese una letra\n")
        n=0
        for i in self.lista:
            if i == self.letra:
                n=n+1
        print("la cantidad de veces que se repite esa letra es", str(n))
                

let=frase_letra()

let.encontrar()







