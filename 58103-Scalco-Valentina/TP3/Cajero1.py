
class CantidadError(Exception):
    pass


class ValueError(Exception):
    pass


class MultiplicidadError(Exception):
    pass


class BilleteError(Exception):
    pass


class DisponibilidadError(Exception):
    pass


class Atm:

    def __init__(self):
        self.billetes100 = []
        self.billetes200 = []
        self.billetes500 = []
        self.billetes1k = []
        self.total = 0

    def agregar_dinero(self, lista_de_billetes):
        for i in lista_de_billetes:
            if i.denom == 100:
                self.billetes100.append(i)
            elif i.denom == 200:
                self.billetes200.append(i)
            elif i.denom == 500:
                self.billetes500.append(i)
            else:
                self.billetes1k.append(i)

    def contar_dinero(self):
        billete =[len(self.billetes100), len(self.billetes200),
                len(self.billetes500), len(self.billetes1k)]
        count_bills = []
        for x in range(len(billete)):
            if x == 0:
                valor = 100
            if x == 1:
                valor = 200
            if x == 2:
                valor = 500
            if x == 3:
                valor = 1000
            string = (str(billete[x]) + " billetes de $" + str(valor) + ", Parcial $" + str(billete[x] * valor))
            count_bills.append(string)
        self.total = (billete[0]*100 + billete[1]*200 + billete[2]*500 + billete[3]*1000)
        count_bills.append("Total: $" + str(self.total))
        return(count_bills)

    def extraer_dinero(self, monto):
        disponible = [len(self.billetes1k), len(self.billetes500),
                    len(self.billetes200), len(self.billetes100)]
        self.total = (disponible[0]*1000 + disponible[1]*500 + disponible[2]*200 + disponible[3]*100)
        retiro = []
        cant = 0
        count_bills = []
        if monto < 0:
            raise ValueError("Error. Monto negativo no válido, ingrese un monto positivo")
        if self.total == 0:
            raise DisponibilidadError("Error. Cajero vacío")
        if monto > self.total:
            raise CantidadError("Error. Monto no válido, ingrese un monto menor")
        if monto % 100 != 0:
            raise MultiplicidadError("Error. Monto no válido, ingrese un monto multiplo de 100")
        cant = monto//1000
        if disponible[0] != 0 or cant != 0:
            if cant <= disponible[0]:
                for i in range(cant):
                    disponible[0] -= 1
                retiro.append(cant)
                monto -= cant * 1000
            else:
                monto -= disponible[0] * 1000
                retiro.append(disponible[0])
                disponible[0] = 0
            valor = 1000
            for i in range(len(retiro)):
                string = (str(retiro[i]) + " billetes de $" + str(valor))
            count_bills.append(string)

        cant = monto//500
        if disponible[1] != 0 or cant != 0:
            if cant <= disponible[1]:
                for i in range(cant):
                    disponible[1] -= 1
                retiro.append(cant)
                monto -= cant * 500
            else:
                monto -= disponible[1] * 500
                retiro.append(disponible[1])
                disponible[1] = 0
            valor = 500
            for i in range(len(retiro)):
                string = (str(retiro[i]) + " billetes de $" + str(valor))
            count_bills.append(string)

        cant = monto//200
        if disponible[2] != 0 or cant != 0:
            if cant <= disponible[2]:
                for i in range(cant):
                    disponible[2] -= 1
                retiro.append(cant)
                monto -= cant * 200
            else:
                monto -= disponible[2] * 200
                retiro.append(disponible[2])
                disponible[2] = 0
            valor = 200
            for i in range(len(retiro)):
                string = (str(retiro[i]) + " billetes de $" + str(valor))
            count_bills.append(string)

        cant = monto//100
        if disponible[3] != 0 or cant != 0:
            if cant <= disponible[3]:
                for i in range(cant):
                    disponible[3] -= 1
                retiro.append(cant)
            else:
                monto -= disponible[3] * 100
                retiro.append(disponible[3])
                disponible[3] = 0
            valor = 100
            for i in range(len(retiro)):
                string = (str(retiro[i]) + " billetes de $" + str(valor))
            count_bills.append(string)
        if monto == 0:
            return count_bills
        else:
            raise BilleteError("Error. No hay una combinación de billetes que nos permita extraer ese monto")
