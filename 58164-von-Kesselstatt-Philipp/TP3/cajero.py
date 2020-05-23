class InsufficientFunds(Exception):
    def __init__(self, message):
        print(message)


class MinimumValueError(Exception):
    def __init__(self, message):
        print(message)


class PercentageError(Exception):
    def __init__(self, message):
        print(message)


class ImpossibleCombinationError(Exception):
    def __init__(self, message):
        print(message)


class ExtractionError(Exception):
    def __init__(self, message):
        print(message)


class Cajero():

    def __init__(self):
        self.dinero = {}

    def agregar_dinero(self, lista_billetes):

        for item in lista_billetes:

            moneda = item.getMoneda()

            if moneda in self.dinero.keys():
                self.dinero[moneda].append(item)

            else:
                self.dinero[moneda] = []
                self.dinero[moneda].append(item)

    def contar_dinero(self):
        contado = {}
        for keys in self.dinero.keys():
            subtotales = {}
            total = 0

            for billete in self.dinero[keys]:

                valor = billete.getDenominacion()
                total += valor

                if valor in subtotales.keys():
                    subtotales[valor] += valor
                else:
                    subtotales[valor] = valor

            contado[keys] = (subtotales, total)

        return contado

    def contado_imprimir(self):
        contado = self.contar_dinero()
        string = ""

        "{'pesos': ({1000: 10000}, 10000)}"
        "pesos:\n10 billetes de $1000, parcial $10000\nTotal: $10000"
        for tipo_moneda in contado:
            string += tipo_moneda + ":\n"
            for subtotal in contado[tipo_moneda][0]:
                string += str(int(contado[tipo_moneda][0][subtotal]/subtotal))
                string += " billetes de $" + str(subtotal)
                string += " parcial $" + str(contado[tipo_moneda][0][subtotal])
                string += "\n"

            string += "\nTotal:" + str(contado[tipo_moneda][1])

        return string

    def extraer_dinero(self, monto, porcentaje_cambio):
        self.dinero["pesos"].sort(key=lambda valor: valor.getDenominacion())

        total = self.contar_dinero()["pesos"][1]

        if self.dinero["pesos"] == []:
            raise ExtractionError("No hay billetes en el cajero")
        elif monto > total:
            raise InsufficientFunds("No hay suficiente dinero en la cuenta")
        elif monto % 100 != 0:
            raise MinimumValueError("El monto debe ser multiplo de 100")
        elif (porcentaje_cambio > 100 or
              porcentaje_cambio < 0):
            raise PercentageError(
                    "El porcentaje de cambio debe estar entre 0 y 100")
        elif monto < 1:
            raise ExtractionError("Ingrese un monto positivo")

        # monto_total = monto
        monto_cambio = monto*porcentaje_cambio/100

        monto -= monto_cambio

        extraction = []

        for billete in self.dinero["pesos"]:
            denominacion = billete.getDenominacion()

            if monto_cambio > 0:
                extraction.append(billete)
                monto_cambio -= denominacion
            else:
                break
        monto += monto_cambio

        for item in extraction:
            self.dinero["pesos"].remove(item)

        self.dinero["pesos"].sort(key=lambda valor: valor.getDenominacion(),
                                  reverse=True)

        for billete in self.dinero["pesos"]:
            denominacion = billete.getDenominacion()

            if monto/denominacion >= 1:
                extraction.append(billete)

                monto -= denominacion

        for item in extraction:
            if item in self.dinero["pesos"]:
                self.dinero["pesos"].remove(item)
        # """
        if monto > 0:
            self.dinero["pesos"] += extraction
            raise ImpossibleCombinationError("No se puede extraer ese monto con los billetes disponibles")
        # """
        """
        self.dinero["pesos"].sort(key=lambda valor: valor.getDenominacion())
        total_extraccion = sum([item.getDenominacion() for item in extraction])
        first_total = total_extraccion
        while monto_total != total_extraccion:
            self.dinero["pesos"].append(extraction.pop(0))
            extraction.append(self.dinero["pesos"].pop(0))

            total_extraccion = 0
            for item in extraction:
                total_extraccion += item.getDenominacion()
            if total_extraccion == first_total:
                pass

        """
        return extraction


"""
from billetes import Billete100
from billetes import Billete200
from billetes import Billete500
from billetes import Billete1000

aa = Cajero()

b1 = Billete100()
b2 = Billete200()
b4 = Billete1000()
b5 = Billete200()
bill = [b1, b2, b4, b5]

aa.agregar_dinero(bill)

# ------------------------------
print("Dinero en el cajero:")
for i in aa.dinero["pesos"]:
    print(i.getRepresentacion())
print("\n\n")
# ------------------------------
print(aa.contado_imprimir())
print("\n\n")
# ------------------------------
billetera = []
for i in range(10):
    billetera.append(Billete1000())

for i in range(4):
    billetera.append(Billete200())

aa.agregar_dinero(billetera)

x = aa.extraer_dinero(9000, 10)
c = 0
print("Dinero extraido:")
for i in x:
    print(i.getRepresentacion())
    c += i.getDenominacion()
print('total: ', c)
"""
