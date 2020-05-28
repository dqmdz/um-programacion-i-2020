from billete import Billetes, Billete100, Billete200, Billete500, Billete1000

class dineroIsuficiente(Exception):
    def __init__(self, retorno):
        print(retorno)

class notMultiplo(Exception):
    def __init__(self, retorno):
        print(retorno)

class rangoCambio(Exception):
    def __init__(self, retorno):
        print(retorno)

class billetesInsuficientes(Exception):
    def __init__(self, retorno):
        print(retorno)

class dineroNegativo(Exception):
    def __init__(self, retorno):
        print(retorno)

class sinBilletes(Exception):
    def __init__(self, retorno):
        print(retorno)

class Cajero():
    def __init__(self):
        self.total = 0
        self.lista1 = []
        self.lExtraidos = []

    def agregarDinero(self, listaP):
        for i in listaP:
            self.lista1.append(i)

    def contarDinero(self):
        self.total100 = 0
        self.total200 = 0
        self.total500 = 0
        self.total1000 = 0

        self.cantidad100 = 0
        self.cantidad200 = 0
        self.cantidad500 = 0
        self.cantidad1000 = 0

        for i in self.lista1:
            if i.moneda_valor == 100:
                self.total100 = self.total100+100
                self.cantidad100 += 1
            elif i.moneda_valor == 200:
                self.total200 = self.total200+200
                self.cantidad200 += 1
            elif i.moneda_valor == 500:
                self.total500 = self.total500+500
                self.cantidad500 += 1
            elif i.moneda_valor == 1000:
                self.total1000 = self.total1000+1000
                self.cantidad1000 += 1

        self.total = self.total100+self.total200+self.total500+self.total1000

        if self.total <= 0:
            raise sinBilletes("El cajero se encuentra sin billetes")
        else:
            return (self.cantidad100, self.cantidad200, self.cantidad500, self.cantidad1000, self.total100, self.total200, self.total500, self.total1000, self.total)

    def extraerDineroCambio(self, extraccion, cambio):
        lExtraidosC = []
        if extraccion < 0:
            raise dineroNegativo("Ingrese un valor valido para la extraccion")
        if self.total <= 0:
            raise sinBilletes("El cajero se encuentra sin dinero")
        if cambio > 1 or cambio < 0:
            raise rangoCambio("El rango de cambio puede solo ir de 0 a 100%")
        else:
            cambio = extraccion*cambio
        if cambio % 100 != 0:
            resto = cambio % 100
            cambio = (cambio - resto) + 100
        if cambio > 0:
            while cambio > 0 and self.cantidad100 > 0:
                extraccion = extraccion - 100
                cambio = cambio - 100
                for i in self.lista1:
                    if i.moneda_valor == 100:
                        lExtraidosC.append(i.moneda_valor)
                        self.lista1.remove(i)
                        self.cantidad100 = self.cantidad100-1
                        break

            while cambio > 0 and self.cantidad200 > 0:
                for i in self.lista1:
                    if i.moneda_valor == 200:
                        extraccion = extraccion - 200
                        cambio = cambio - 200
                        lExtraidosC.append(i.moneda_valor)
                        self.lista1.remove(i)
                        self.cantidad200 = self.cantidad200-1
                        break

            while cambio > 0 and self.cantidad500 > 0:
                extraccion = extraccion - 500
                cambio = cambio - 500
                for i in self.lista1:
                    if i.moneda_valor == 500:
                        lExtraidosC.append(i.moneda_valor)
                        self.lista1.remove(i)
                        self.cantidad200 = self.cantidad200-1
                        break

        
        extSinCambio = self.extraerDinero(extraccion)
        lExtraidosC.extend(extSinCambio)
        return lExtraidosC

    def extraerDinero(self, extraccion):
        if extraccion < 0:
            raise dineroNegativo("Ingrese un valor valido para la extraccion")
        if self.total <= 0:
            raise sinBilletes("El cajero se encuentra sin dinero")
        if extraccion % 100 == 0:
            if self.total >= extraccion:
                while extraccion >= 1000 and self.cantidad1000 > 0:
                    for i in self.lista1:
                        if i.moneda_valor == 1000:
                            extraccion = extraccion - 1000
                            self.lExtraidos.append(i.moneda_valor)
                            self.lista1.remove(i)
                            self.cantidad1000 = self.cantidad1000-1
                            break

                while extraccion >= 500 and self.cantidad500 > 0:
                    for i in self.lista1:
                        if i.moneda_valor == 500:
                            extraccion = extraccion - 500
                            self.lExtraidos.append(i.moneda_valor)
                            self.lista1.remove(i)
                            self.cantidad500 = self.cantidad500-1
                            break

                while extraccion >= 200 and self.cantidad200 > 0:
                    for i in self.lista1:
                        if i.moneda_valor == 200:
                            extraccion = extraccion - 200
                            self.lExtraidos.append(i.moneda_valor)
                            self.lista1.remove(i)
                            self.cantidad200 = self.cantidad200-1
                            break

                while extraccion >= 100 and self.cantidad100 > 0:
                    for i in self.lista1:
                        if i.moneda_valor == 100:
                            extraccion = extraccion - 100
                            self.lExtraidos.append(i.moneda_valor)
                            self.lista1.remove(i)
                            self.cantidad100 = self.cantidad100-1
                            break
                    
                if extraccion > 0:
                    raise billetesInsuficientes("Error. No hay una combinación de billetes que nos permita extraer ese monto.")
                else:
                    return self.lExtraidos

            else:
                raise dineroIsuficiente("No se puede extraer mas dinero del que hay disponible en el cajero")
        else:
            raise notMultiplo("No se puede extraer dinero que no sea múltiplo de 100")

"""
def main():
    a = Billete1000()
    aa = Billete1000()
    aaa = Billete1000()
    aaaa = Billete1000()
    aaaaa = Billete1000()
    b = Billete500()
    bb = Billete500()
    bbb = Billete500()
    c = Billete200()
    cc = Billete200()
    ccc = Billete200()
    cccc = Billete200()
    ccccc = Billete200()
    d = Billete100()
    dd = Billete100()
    ddd = Billete100()
    listaP = []
    cajero = Cajero()
    cajero.agregarDinero(listaP)
    cajero.contarDinero()
    cam = float(input("Ingrese el la cantidad de cambio que quiere obtener(0.1 para el 10%, etc): "))
    cajero.extraerDineroCambio(1000, cam)
    cajero.contarDinero()

main()
"""