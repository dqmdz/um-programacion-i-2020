class ExcesoError(Exception):
    pass


class MultipoError(Exception):
    pass


class NegativoError(Exception):
    pass


class CombinacionError(Exception):
    pass


class VacioError(Exception):
    pass


class Cajero():

    def __init__(self):
        self.cien = []
        self.doscien = []
        self.quini = []
        self.mil = []
        self.entrega = []
        self.suma = 0
        self.transaccion = False

    def carga(self, deposito):
        for fajo in deposito:

            if fajo.denominacion == 100:
                self.cien.append(100)

            if fajo.denominacion == 200:
                self.doscien.append(200)

            if fajo.denominacion == 500:
                self.quini.append(500)

            if fajo.denominacion == 1000:
                self.mil.append(1000)

    def conteo(self):

        depo_100 = len(self.cien) * 100
        depo_200 = len(self.doscien) * 200
        depo_500 = len(self.quini) * 500
        depo_1000 = len(self.mil) * 1000
        self.suma = depo_100 + depo_1000 + depo_200 + depo_500
        return(depo_1000, depo_500, depo_200, depo_100, self.suma)

    def vaciado(self):
        self.cien = []
        self.doscien = []
        self.quini = []
        self.mil = []

    def extraer(self, pedido, redondeo=0):

        self.pedido = pedido
        self.transaccion = True
        self.entrega = []
        n = 0

        if self.suma == 0:
            self.transaccion = False
            raise VacioError

        if pedido < 0:
            self.transaccion = False
            raise NegativoError

        if self.suma < pedido:
            self.transaccion = False
            raise ExcesoError

        if pedido % 100 != 0:
            self.transaccion = False
            raise MultipoError

        while (self.pedido != 0) and (self.transaccion is True):

            if (len(str(self.pedido)) >= 4) and (len(self.mil) != 0):

                self.mil.pop()      # Sacar el ultimo elemento de la lista
                self.pedido -= 1000
                self.entrega.append(1000)

            if (len(str(self.pedido)) == 3) or (len(self.mil) == 0):

                n += 1

                if n > 5:
                    if (self.pedido != 0) and (redondeo != 0):
                        return(self.pedido)
                    else:
                        raise(CombinacionError)

                if (len(self.quini) != 0) and (self.pedido >= 500):

                    self.quini.pop()
                    self.pedido -= 500
                    self.entrega.append(500)

                elif (self.pedido >= 200) and ((len(self.doscien) != 0) or
                                               ((len(self.quini) == 0) and
                                               (len(self.doscien) != 0))):
                    self.doscien.pop()
                    self.pedido -= 200
                    self.entrega.append(200)

                elif (self.pedido >= 100) and ((len(self.cien) != 0) or
                                               ((len(self.doscien) == 0) and
                                               (len(self.cien) != 0))):

                    self.cien.pop()
                    self.pedido -= 100
                    self.entrega.append(100)
        total = (self.entrega.count(1000)*1000 + self.entrega.count(500)*500 +
                 self.entrega.count(200)*200 + self.entrega.count(100)*100)
        return(self.entrega.count(1000), self.entrega.count(500),
               self.entrega.count(200), self.entrega.count(100),
               "Se extrajo sin cambio ${}".format(str(total)))
