class persona():
    def __init__(self):
        self.nombre=''
        self.edad=''
        self.direccion=''
        self.telefono=''
    
    def ingresar(self):
        self.nombre=input("ingrese su nombre\n")
        self.edad=input("ingrese su edad\n")
        self.direccion=input("ingrese su direccion\n")
        self.telefono=(input("ingrese su telefono\n"))

    def diccionario(self):
        diccionario={"nombre" : self.nombre, "edad" : self.edad, "direccion" : self.direccion, "telefono" : self.telefono}  
        print(diccionario)
        print("")
        print(self.nombre, "tiene", self.edad, "años , vive en", self.direccion, "y su numero de telefono es", self.telefono)

pers=persona()

pers.ingresar()
pers.diccionario()        









#<nombre> tiene
#<edad> años, vive en <dirección> y su número de teléfono es#

#<teléfono>