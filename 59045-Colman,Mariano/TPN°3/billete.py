class Billetes():

    def __init__(self, moneda_valor, representacion):
        self.denominacion = "Pesos"
        self.moneda_valor = moneda_valor
        self.representacion = representacion


class Billete100(Billetes):
    def __init__(self):
        Billetes.__init__(self, 100, "$100")


class Billete200(Billetes):
    def __init__(self):
        Billetes.__init__(self, 200, "$200")


class Billete500(Billetes):
    def __init__(self):
        Billetes.__init__(self, 500, "$500")


class Billete1000(Billetes):
    def __init__(self):
        Billetes.__init__(self, 1000, "$1000")