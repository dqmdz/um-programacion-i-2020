class Billete:
    def __init__(self, denom, coin, repre):
        self.denom = 0
        self.coin = ""
        self.repre = ""


class Billete_100(Billete):
    def __init__(self, moneda, representacion):
        self.denom = 100
        self.coin = "pesos"
        self.repre = "100"


class Billete_200(Billete):
    def __init__(self, moneda, representacion):
        self.denom = 200
        self.coin = "pesos"
        self.repre = "200"


class Billete_500(Billete):
    def __init__(self, moneda, representacion):
        self.denom = 500
        self.coin = "pesos"
        self.repre = "500"


class Billete_1000(Billete):
    def __init__(self, moneda, representacion):
        self.denom = 1000
        self.coin = "pesos"
        self.repre = "$"
