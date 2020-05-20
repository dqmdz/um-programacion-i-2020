class Billete():
    def __init__(self):
        self.denominacion = 0
        self.moneda = "pesos"
        self.representacion = "$" + str(self.denominacion)


class Billete100(Billete):
    def __init__(self):
        self.denominacion = 100
        self.moneda = "pesos"
        self.representacion = "$" + str(self.denominacion)


class Billete200(Billete):
    def __init__(self):
        self.denominacion = 200
        self.moneda = "pesos"
        self.representacion = "$" + str(self.denominacion)


class Billete500(Billete):
    def __init__(self):
        self.denominacion = 500
        self.moneda = "pesos"
        self.representacion = "$" + str(self.denominacion)


class Billete1000(Billete):
    def __init__(self):
        self.denominacion = 1000
        self.moneda = "pesos"
        self.representacion = "$" + str(self.denominacion)
