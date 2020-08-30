class Billete:

    def __init__(self):
        self.denominacion = 0
        self.moneda = ''
        self.representa = ''


class Billete_100(Billete):

    def __init__(self):
        self.denominacion = 100
        self.moneda = "Pesos"
        self.representa = '$100'


class Billete_200(Billete):

    def __init__(self):
        self.denominacion = 200
        self.moneda = "Pesos"
        self.representa = '$200'


class Billete_500(Billete):

    def __init__(self):
        self.denominacion = 500
        self.moneda = "Pesos"
        self.representa = '$500'


class Billete_1000(Billete):

    def __init__(self):
        self.denominacion = 1000
        self.moneda = "Pesos"
        self.representa = '$1000'
