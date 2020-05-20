class Billete():

    def __init__(self,denominacion,valor):
        self.denominacion = denominacion
        self.moneda_valor = valor
        self.representacion = "$"+ str(denominacion)
       

class Billete100(Billete):
    def __init__(self):
        Billete.__init__(self,100,"Pesos")
      
class Billete200(Billete):
    def __init__(self):
        Billete.__init__(self,200,"Pesos")
        
class Billete500(Billete):
    def __init__(self):
        Billete.__init__(self,500,"Pesos")

class Billete1000(Billete):
    def __init__(self):
        Billete.__init__(self,1000, "Pesos")
            