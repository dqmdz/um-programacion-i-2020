class CombinacionError(Exception):
    pass


class MultiplicidadError(Exception):
    pass


class CantidadError(Exception):
    pass


class PorcentajeError(Exception):
    pass


class MontoError(Exception):
    pass


class Cajero():
    def __init__(self):
        self.cant100 = []
        self.cant200 = []
        self.cant500 = []
        self.cant1000 = []
        self.montos_p = []
        self.monto_total = 0
        self.b_extr = [0, 0, 0, 0]
        self.cantidades = []
        self.sacado = []
        self.total = 0
        self.cambio2 = 0

    def agregar_dinero(self, billetes):
        for i in billetes:
            if i.denominacion == 1000:
                self.cant1000.append(i.denominacion)
            elif i.denominacion == 500:
                self.cant500.append(i.denominacion)
            elif i.denominacion == 200:
                self.cant200.append(i.denominacion)
            else:
                self.cant100.append(i.denominacion)

    def contar_dinero(self):
        text1 = ""
        self.cantidades = [len(self.cant1000), len(self.cant500),
                           len(self.cant200), len(self.cant100)]
        self.montos_p = [self.cantidades[0] * 1000, self.cantidades[1] * 500,
                         self.cantidades[2] * 200, self.cantidades[3] * 100]
        self.monto_total = int(self.montos_p[0] + self.montos_p[1] +
                               self.montos_p[2] + self.montos_p[3])
        for i in range(len(self.cantidades)):
            if i == 0:
                if len(self.cant1000) != 0:
                    text1 += str(self.cantidades[i]) + " billetes de $1000,"
                    text1 += " parcial $" + str(self.montos_p[i]) + "\n"
            elif i == 1:
                if len(self.cant500) != 0:
                    text1 += str(self.cantidades[i]) + " billetes de $500,"
                    text1 += " parcial $" + str(self.montos_p[i]) + "\n"
            elif i == 2:
                if len(self.cant200) != 0:
                    text1 += str(self.cantidades[i]) + " billetes de $200,"
                    text1 += " parcial $" + str(self.montos_p[i]) + "\n"
            else:
                if len(self.cant100) != 0:
                    text1 += str(self.cantidades[i]) + " billetes de $100"
                    text1 += " parcial $" + str(self.montos_p[i]) + "\n"
        text1 += "Total $" + str(self.monto_total)
        return text1

    def extraer_dinero(self, monto):
        # tx = ""
        tx2 = ""
        self.caja = [len(self.cant1000), len(self.cant500),
                     len(self.cant200), len(self.cant100)]
        self.total += (len(self.cant1000) * 1000) + (len(self.cant500) * 500)
        self.total += (len(self.cant200) * 200) + (len(self.cant100) * 100)
        # try:
        if monto < 0:
            raise MontoError("Error.Ingrese un monto mayor a cero")
        # except MontoError:
        #    return "Error. Ingrese un monto mayor a cero"
        # try:
        if monto % 100 != 0:
            raise MultiplicidadError("Error. El monto es incorrecto")
        # except MultiplicidadError:
        #    return "Error. El monto es incorrecto"
        # try:
        if monto >= self.total:
            raise CantidadError("Error. Quiere sacar mas dinero de lo que se"
                                " puede")
        # except CantidadError:
            # return "Error. Quiere sacar mas dinero de lo que se puede"
        val = [1000, 500, 200, 100]
        for i in range(len(val)):
            while self.caja[i] > 0 and monto >= val[i]:
                monto -= val[i]
                self.caja[i] -= 1
                self.b_extr[i] += 1
        # try:
        if monto != 0:
            raise CombinacionError("Error. No hay una combinacion de billetes"
                                   " que nos permita extraer ese monto.")
        # except CombinacionError:
        #    tx += "Error. No hay una combinacion de billetes que nos permita "
        #    tx += "extraer ese monto."
        #    return tx
        for i in range(len(self.b_extr)):
            if i == 0:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $1000\n"
            elif i == 1:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $500\n"
            elif i == 2:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $200\n"
            else:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $100\n"
        return tx2

    def extraer_dinero_cambio(self, monto, porcentaje):
        # tx = ""
        tx2 = ""
        self.caja = [len(self.cant1000), len(self.cant500),
                     len(self.cant200), len(self.cant100)]
        self.total += (len(self.cant1000) * 1000) + (len(self.cant500) * 500)
        self.total += (len(self.cant200) * 200) + (len(self.cant100) * 100)
        # Notifico en caso de que ingresen un monto no aceptado
        if monto < 0:
            raise MontoError("Error.Ingrese un monto mayor a cero")
        # try:
        if monto % 100 != 0:
            raise MultiplicidadError("Error. El monto es incorrecto")
        # except MultiplicidadError:
        #     return "Error. El monto es incorrecto"
        # Notifico en caso de que el dinero en el cajero
        # sea menor que el monto ingresado
        # try:
        if monto >= self.total:
            raise CantidadError("Error. Quiere sacar mas dinero de lo que se"
                                " puede")
        # except CantidadError:
        #     return "Error. Quiere sacar mas dinero de lo que se puede"
        # Notifico en caso de que ingresen un porcentaje no apto
        # try:
        if porcentaje < 1 or porcentaje >= 100:
            raise PorcentajeError("Error. Ingrese un porcentaje entre 1 y 100")
        # except PorcentajeError:
        #     return "Error. Ingrese un porcentaje entre 0 y 100"
        # Paso al entero ingresado como porcentaje a decimales
        porcentaje = porcentaje * 0.01
        # Calculo el cambio a dar
        cambio = round(monto * porcentaje)
        # Aproximo el cambio al proximo multiplo de 100
        # En caso de que no lo sea
        if cambio % 100 != 0:
            cambio += (100 - (cambio % 100))
        # Creo una otra variable que almacene el valor del cambio
        # Luego se usara para restarsela al monto ingresado
        # Y asi poder seguir con el progreso de sacado de dinero
        # De forma normal
        self.cambio2 = cambio
        # Creo una variable que contenga los billetes de menor a mayor
        val = [100, 200, 500, 1000]
        # Realizo la extraccion de billetes en cambio
        self.caja = self.caja[::-1]
        for i in range(len(val)):
            while self.caja[i] > 0 and cambio >= val[i]:
                cambio -= val[i]
                self.caja[i] -= 1
                self.b_extr[i] += 1
        # En caso de que el cambio sea distinto de cero, porque no
        # Se ejecutaron los while al no tener cierto billete para dar
        # El cambio, le sumo 100 a cambio y sel.cambio2 y vuelvo a hacer
        # La extraccion de billetes hasta que el cambio sea cero
        while cambio != 0:
            cambio += 100
            self.cambio2 += 100
            for i in range(len(val)):
                while self.caja[i] > 0 and cambio >= val[i]:
                    cambio -= val[i]
                    self.caja[i] -= 1
                    self.b_extr[i] += 1
        # Le resto el monto final del cambio al monto ingresado para poder
        # Hacer la extraccion del monto en forma normal
        monto -= self.cambio2
        # Invierto los valores de la caja y la lista para que se extraiga los
        # Billetes de forma normal
        self.caja = self.caja[::-1]
        val = val[::-1]
        self.b_extr = self.b_extr[::-1]
        for i in range(len(val)):
            while self.caja[i] > 0 and monto >= val[i]:
                monto -= val[i]
                self.caja[i] -= 1
                self.b_extr[i] += 1
        # Notifico en caso de que el monto no sea cero, por ende no hay direno
        # disponible, con lo que hay en el cajero,
        # para devolver al cliente
        # try:
        if monto != 0:
            raise CombinacionError("Error. No hay una combinacion de billetes"
                                   " que nos permita extraer ese monto.")
        # except CombinacionError:
        #     tx += "Error. No hay una combinacion de billetes que nos permita"
        #     tx += "extraer ese monto."
        #     return tx
        self.b_extr = self.b_extr[::-1]
        # Imprimo el resultado
        for i in range(len(self.b_extr)):
            if i == 0:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $100\n"
            elif i == 1:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $200\n"
            elif i == 2:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $500\n"
            else:
                if self.b_extr[i] != 0:
                    tx2 += str(self.b_extr[i]) + " billetes de $1000\n"
        return tx2


if __name__ == "__main__":
    main = Cajero()
