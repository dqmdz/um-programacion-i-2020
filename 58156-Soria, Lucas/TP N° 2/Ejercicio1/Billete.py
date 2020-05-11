#!/usr/bin/python
class Billete:

    def __init__(self):
        self.denominacion = 0
        self.moneda = ""
        self.representacion = ""


class Billete_de_100(Billete):

    def __init__(self, moneda, representacion):
        self.denominacion = 100
        self.moneda = moneda
        self.representacion = representacion + "100"


class Billete_de_200(Billete):

    def __init__(self, moneda, representacion):
        self.denominacion = 200
        self.moneda = moneda
        self.representacion = representacion + "200"


class Billete_de_500(Billete):

    def __init__(self, moneda, representacion):
        self.denominacion = 500
        self.moneda = moneda
        self.representacion = representacion + "500"


class Billete_de_1000(Billete):

    def __init__(self, moneda, representacion):
        self.denominacion = 1000
        self.moneda = moneda
        self.representacion = representacion + "1000"
