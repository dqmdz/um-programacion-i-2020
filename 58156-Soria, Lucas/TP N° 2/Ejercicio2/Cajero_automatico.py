#!/usr/bin/python
import math


class CantidadError(Exception):
    pass


class MultiplicidadError(Exception):
    pass


class PorcentajeError(Exception):
    pass


class BilleteError(Exception):
    pass


class Cajero_automatico:

    def __init__(self):
        self.billetes_mil = []
        self.billetes_quinientos = []
        self.billetes_doscientos = []
        self.billetes_cien = []

    def agregar_dinero(self, lista_billetes):
        for x in lista_billetes:
            if x.denominacion == 100:
                self.billetes_cien.append(x)
            elif x.denominacion == 200:
                self.billetes_doscientos.append(x)
            elif x.denominacion == 500:
                self.billetes_quinientos.append(x)
            else:
                self.billetes_mil.append(x)

    def contar_dinero(self):
        texto = ""
        lista = [1000, 500, 200, 100]
        parcial = []
        billetes = [len(self.billetes_mil), len(self.billetes_quinientos),
                    len(self.billetes_doscientos), len(self.billetes_cien)]
        parcial = [lista[x] * billetes[x] for x in range(len(billetes))]
        for x in range(len(billetes)):
            if billetes[x] != 0:
                texto += "{} billetes de ".format(billetes[x])
                texto += "${}, parcial ${}\n".format(lista[x], parcial[x])
        texto += "Total: ${}".format(sum(i for i in parcial))
        return texto

    def extraer_dinero(self, monto):
        dar = [0, 0, 0, 0]
        billetes = []
        lista = [1000, 500, 200, 100]
        dispo = [len(self.billetes_mil),
                 len(self.billetes_quinientos),
                 len(self.billetes_doscientos),
                 len(self.billetes_cien)]
        total = sum(i for i in [lista[x]*dispo[x] for x in range(len(lista))])
        try:
            if monto > total:
                raise CantidadError
        except CantidadError:
            return "Error. Quiero sacar mas dinero de lo que puedo"
        try:
            if monto % 100 != 0:
                raise MultiplicidadError
        except MultiplicidadError:
            return "Error. El monto es incorrecto"
        for x in range(len(lista)):
            billetes.append(math.trunc(monto/lista[x]))
            monto = monto % lista[x]
        for x in range(len(lista)):
            while billetes[x] > 0:
                if dispo[x] > 0:
                    if x == 0:
                        self.billetes_mil.pop()
                    elif x == 1:
                        self.billetes_quinientos.pop()
                    elif x == 2:
                        self.billetes_doscientos.pop()
                    else:
                        self.billetes_cien.pop()
                    dar[x] += 1
                    dispo[x] -= 1
                    billetes[x] -= 1
                else:
                    try:
                        if x != 3:
                            billetes[x+1] += 2 * billetes[x]
                            if x == 1:
                                billetes[x+2] += billetes[x]
                        else:
                            raise BilleteError
                        billetes[x] = 0
                    except BilleteError:
                        return ("Error. No hay una combinación de" +
                                " billetes que nos permita extraer " +
                                "ese monto")
        texto = ""
        for x in range(4):
            if dar[x] != 0:
                texto += "{} billetes de ${}\n".format(dar[x], lista[x])
        return texto

    def extraer_dinero_cambio(self, monto, porc):
        dar = [0, 0, 0, 0]
        suma = 0
        lista = [100, 200, 500, 1000]
        try:
            if porc > 100 or porc < 0:
                raise PorcentajeError
        except PorcentajeError:
            return "Error. El porcentaje es incorrecto"
        porc = math.trunc(monto * porc / 100)
        sacar = porc
        sacar = str(sacar)[::-1]
        if len(sacar) <= 2:
            sacar = 100
        else:
            sacar = sacar[::-1][:2]
            sacar = (int(sacar[::-1]) + 1) * 100
        if sacar - porc >= 100 or sacar - porc <= 0:
            sacar = porc
        billetes = [math.trunc(sacar / 100), 0, 0, 0]
        dispo = [len(self.billetes_cien),
                 len(self.billetes_doscientos),
                 len(self.billetes_quinientos),
                 len(self.billetes_mil)]
        total = sum(i for i in [lista[x]*dispo[x] for x in range(len(lista))])
        try:
            if monto > total:
                raise CantidadError
        except CantidadError:
            return "Error. Quiero sacar mas dinero de lo que puedo"
        try:
            if monto % 100 != 0:
                raise MultiplicidadError
        except MultiplicidadError:
            return "Error. El monto es incorrecto"
        for x in range(len(lista)):
            while billetes[x] > 0 and suma <= sacar:
                if dispo[x] > 0:
                    if x == 3:
                        self.billetes_mil.pop()
                    elif x == 2:
                        self.billetes_quinientos.pop()
                    elif x == 1:
                        self.billetes_doscientos.pop()
                    else:
                        self.billetes_cien.pop()
                    dar[x] += 1
                    dispo[x] -= 1
                    billetes[x] -= 1
                else:
                    try:
                        if x < 3:
                            billetes[x+1] += billetes[x]
                        else:
                            raise BilleteError
                        billetes[x] = 0
                    except BilleteError:
                        return ("Error. No hay una combinación de" +
                                " billetes que nos permita extraer " +
                                "ese monto")
                suma = sum(i for i in[dar[x]*lista[x] for x in range(4)])
        texto = self.extraer_dinero(monto - suma)
        for x in texto.strip("\n").split("\n"):
            renglon = x.split(" ")
            if renglon[-1] == "$1000":
                dar[3] += int(renglon[0])
            elif renglon[-1] == "$500":
                dar[2] += int(renglon[0])
            elif renglon[-1] == "$200":
                dar[1] += int(renglon[0])
            elif renglon[-1] == "$100":
                dar[0] += int(renglon[0])
            else:
                return texto
        texto = ""
        for x in range(4):
            if dar[x] != 0:
                texto += "{} billetes de ${}\n".format(dar[x], lista[x])
        return texto
