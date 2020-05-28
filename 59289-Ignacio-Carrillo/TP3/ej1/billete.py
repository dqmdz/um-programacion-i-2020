class Billete():
    def __init__(self,denominacion,moneda):
        self.denominacion=denominacion
        self.moneda=moneda
        self.set_representacion(denominacion,moneda)
    
    def set_representacion(self,denominacion,moneda):
        if moneda=="Pesos":
            self.representacion="$ "+str(denominacion)
            
class Billete_100(Billete):
    def __init__(self,denominacion,moneda):
        Billete.__init__(self,denominacion,moneda)

class Billete_200(Billete):
    def __init__(self,denominacion,moneda):
        Billete.__init__(self,denominacion,moneda)

class Billete_500(Billete):
    def __init__(self,denominacion,moneda):
        Billete.__init__(self,denominacion,moneda)

class Billete_1000(Billete):
    def __init__(self,denominacion,moneda):
        Billete.__init__(self,denominacion,moneda)        
    