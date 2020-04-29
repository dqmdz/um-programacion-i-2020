import time
class billete():
   
    def __init__(self, denominacion, moneda_valor, representacion):
        
        self.denominacion = denominacion
        self.moneda_valor = moneda_valor
        self.representacion = representacion
        
class billete_100(billete):

    def __init__(self, denominacion, moneda_valor, representacion):
        super().__init__(denominacion, moneda_valor, representacion)

class billete_200(billete):
  
    def __init__(self, denominacion, moneda_valor, representacion):
        super().__init__(denominacion, moneda_valor, representacion)


class billete_500(billete):
  
    def __init__(self, denominacion, moneda_valor, representacion):
        super().__init__(denominacion, moneda_valor, representacion)

class billete_1000(billete):
  
    def __init__(self, denominacion, moneda_valor, representacion):
        super().__init__(denominacion, moneda_valor, representacion)

  



        

        
