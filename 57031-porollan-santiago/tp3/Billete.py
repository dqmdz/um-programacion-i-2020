

class Billete():
    def __init__(self, denominacion, moneda, representacion):
        self.denominacion = denominacion
        self.moneda = moneda
        self.representacion = representacion + denominacion


class Billete_de_100(Billete):
    def __init__(self):
        super().__init__("100", "pesos", "$")


class Billete_de_200(Billete):
    def __init__(self):
        super().__init__("200", "pesos", "$")


class Billete_de_500(Billete):
    def __init__(self):
        super().__init__("500", "pesos", "$")


class Billete_de_1000(Billete):
    def __init__(self):
        super().__init__("1000", "pesos", "$")
