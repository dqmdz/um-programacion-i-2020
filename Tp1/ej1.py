class grupo():

    def __init__(self):

        self.nombre = input("ingrese su nombre \n >> ")
        self.sexo = input("ingrese su sexo \n >> ")
    
    def imprimir(self):
        print("el nombre del alumno es", self.nombre)  
        print("el sexo de alumno es", self.sexo)
       
    def comprobar(self):
        
        if self.sexo[0].upper() == "F":
    
            if self.nombre[0].upper() == "A" or self.nombre[0].upper() == "B" or self.nombre[0].upper() == "C" or self.nombre[0].upper() == "D" or self.nombre[0].upper() == "E" or self.nombre[0].upper() == "F" or self.nombre[0].upper() == "G" or self.nombre[0].upper() == "H" or self.nombre[0].upper() == "I" or self.nombre[0].upper() == "j" or self.nombre[0].upper() == "k" or self.nombre[0].upper() == "L" or self.nombre[0].upper() == "M":
                print("Usted pertenece al grupo A")
            
        else:
             print("Usted pertenece al grupo B")        
    
  

alumno=grupo()

alumno.imprimir() 
alumno.comprobar()
