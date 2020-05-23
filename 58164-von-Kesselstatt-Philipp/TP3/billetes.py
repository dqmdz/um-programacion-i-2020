class Billete():
    def __init__(self):

        self.denominacion = 0
        self.moneda_valor = ""
        self.representacion = ""

    def getDenominacion(self):
        return self.denominacion

    def setDenominacion(self, denominacion):
        self.denominacion = denominacion

    def getMoneda(self):
        return self.moneda_valor

    def setMoneda(self, moneda_valor):
        self.moneda_valor = moneda_valor

    def getRepresentacion(self):
        return self.representacion

    def setRepresentacion(self, representacion):
        self.representacion = representacion


class Billete100(Billete):
    def __init__(self):
        self.denominacion = 100
        self.moneda_valor = "pesos"
        self.representacion = "$100"


class Billete200(Billete):
    def __init__(self):
        self.denominacion = 200
        self.moneda_valor = "pesos"
        self.representacion = "$200"


class Billete500(Billete):
    def __init__(self):
        self.denominacion = 500
        self.moneda_valor = "pesos"
        self.representacion = "$500"


class Billete1000(Billete):
    def __init__(self):
        self.denominacion = 1000
        self.moneda_valor = "pesos"
        self.representacion = "$1000"
