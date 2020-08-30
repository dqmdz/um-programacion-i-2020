from Cajero import (Cajero, ExcesoError, MultipoError, NegativoError,
                    CombinacionError, VacioError)


class RangoError(Exception):
    pass


class CajeroMejorado(Cajero):

    def extraer_dinero_cambio(self, pedido, porcentaje):

        self.transaccion = True
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

        if (porcentaje < 0) or (porcentaje > 100):
            self.transaccion = False
            raise RangoError

        redondeo = a = int((porcentaje/100) * pedido)

        if (a % 100) != 0:

            b = int(str(a)[-2] + str(a)[-1])
            c = (100 - b) + b
            redondeo = a - b + c

        # Chequearemos si hay resto o no, luego de entregar los
        # billetes grandes, y se sumaran a la entrega de cambio:
        try:
            resto = self.extraer(pedido - redondeo, redondeo)
            resto += redondeo
        except TypeError:
            resto = redondeo

        while (resto != 0) and (self.transaccion is True):

            if (len(self.cien) != 0) and (resto >= 100):

                self.cien.pop()      # Sacar el ultimo elemento de la lista
                resto -= 100
                self.entrega.append(100)

            if (len(self.cien) == 0):
                n += 1

                if n > 5:
                    raise(CombinacionError)
                    exit()

                if (len(self.doscien) != 0) and (resto >= 200):

                    self.doscien.pop()
                    resto -= 200
                    self.entrega.append(200)

                elif (resto >= 500) and ((len(self.quini) != 0) or
                                         ((len(self.doscien) == 0) and
                                         (len(self.quini) != 0))):
                    self.quini.pop()
                    resto -= 500
                    self.entrega.append(500)

                elif (resto >= 1000) and ((len(self.mil) != 0) or
                                          ((len(self.quini) == 0) and
                                          (len(self.mil) != 0))):

                    self.mil.pop()
                    resto -= 1000
                    self.entrega.append(1000)
        total = (self.entrega.count(1000)*1000 + self.entrega.count(500)*500 +
                 self.entrega.count(200)*200 + self.entrega.count(100)*100)

        return(self.entrega.count(1000), self.entrega.count(500),
               self.entrega.count(200), self.entrega.count(100),
               "Se extrajo con cambio ${}".format(str(total)))
