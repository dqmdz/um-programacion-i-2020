import math
from plata import money
from billetes import Billete_100, Billete_1000, Billete_200, Billete_500


class FondosInsuficientes(Exception):
    pass

class NoMultiplo(Exception):
    pass

class SinBilletes(Exception):
    pass

class ExtraccionInvalida(Exception):
    pass

class Cajero_Automatico():

    def __init__(self):

        self.billetes_100 = 0
        self.billetes_200 = 0
        self.billetes_500 = 0
        self.billetes_1000 = 0
        self.total_100 = 0
        self.total_200 = 0
        self.total_500 = 0
        self.total_1000 = 0
        self.dinero_disponible = 0
        self.almacen = []
        self.cambio = 0
        self.montoo = 0


    def agregar_billetes(self, mas_billetes):

        for billete in mas_billetes:
            self.almacen.append(billete)


    def contar_billetes(self):

        #la cuenta en si
        for billete in self.almacen:

            if billete.valor == 100:
                self.billetes_100 += 1
            if billete.valor == 200:
                self.billetes_200 += 1
            if billete.valor == 500:
                self.billetes_500 += 1 
            if billete.valor == 1000:
                self.billetes_1000 += 1

        #cantidad de billetes por su valor
        self.total_billetes_100 = self.billetes_100 * 100
        self.total_billetes_200 = self.billetes_200 * 200
        self.total_billetes_500 = self.billetes_500 * 500
        self.total_billetes_1000 = self.billetes_1000 * 1000

        #total de plata en la cuenta
        self.dinero_disponible = self.total_billetes_100 + self.total_billetes_200 + self.total_billetes_500 + self.total_billetes_1000
        return self.billetes_100, self.total_billetes_100, self.billetes_200, self.total_billetes_200, self.billetes_500, self.total_billetes_500, self.billetes_1000, self.total_billetes_1000, self.dinero_disponible


    def extraer_dinero(self, monto):
        self.montoo = monto
        self.cambio = 10

        if monto % 100 != 0:
            raise NoMultiplo("El monnto debe ser multiplo de 100")

        if monto < 0:
            raise ExtraccionInvalida("Ingrese un monto valido/positivo")
        
        if self.dinero_disponible == 0:
            raise SinBilletes("El cajero no posee dinero para extraer")

        extraidos = []


        #verifico que no quiera extraer mas de lo que tiene
        if self.dinero_disponible >= monto:

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 100:
                monto = monto - 100

                #saco un billete de ese monto
                self.billetes_100 -= 1

                for billete in self.almacen:

                    if billete.valor == 100:
                        extraidos.append(billete)
                        self.almacen.remove(billete)
                        break

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 200:
                monto = monto - 200

                #saco un billete de ese monto
                self.billetes_200 -= 1

                for billete in self.almacen:

                    if billete.valor == 200:
                        extraidos.append(billete)
                        self.almacen.remove(billete)
                        break

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 500:
                monto = monto - 500

                #saco un billete de ese monto
                self.billetes_500 -= 1

                for billete in self.almacen:

                    if billete.valor == 500:
                        extraidos.append(billete)
                        self.almacen.remove(billete)
                        break

            #mientras haya billetes de mil siempre que se pida un monto acorde
            while monto >= 1000:
                monto = monto - 1000

                #saco un billete de ese monto
                self.billetes_1000 -= 1

                for billete in self.almacen:

                    if billete.valor == 1000:
                        extraidos.append(billete)
                        self.almacen.remove(billete)
                        break


            return self.montoo

        else:
            raise FondosInsuficientes("No posee dinero suficiente en la cuenta")

       

    def extraer_dinero_cambio(self):
        cambio = self.cambio
        porcentaje = self.montoo * (cambio / 100)
        copia_monto = self.montoo
        nuevo_balance = self.dinero_disponible - copia_monto
        porcentaje_redondo = math.ceil(porcentaje)
        cont_100 = 0
        cont_200 = 0
        cont_500 = 0
        cont_1000 = 0


        for billete in self.almacen:

            while porcentaje_redondo != 0:

                if porcentaje_redondo > self.total_billetes_100:
                    raise SinBilletes("No hay combinacion posible para extraer ese monto")

                if self.total_billetes_100 >= porcentaje_redondo:
                        self.almacen.remove(billete)
                        porcentaje_redondo -= 100
                        cont_100 += 1
                        break

                elif self.total_billetes_200 >= porcentaje_redondo:
                        self.almacen.remove(billete)
                        porcentaje_redondo -= 200
                        cont_200 += 1
                        break

                elif self.total_billetes_500 >= porcentaje_redondo:
                        self.almacen.remove(billete)
                        porcentaje_redondo -= 500
                        cont_500 += 1
                        break

                elif self.total_billetes_1000 >= porcentaje_redondo:
                        self.almacen.remove(billete)
                        porcentaje_redondo -= 1000
                        cont_1000 += 1
                        break
          
        print(f"""\nExtrayendo $ {copia_monto}, de los cuales  {cont_100} billetes son de 100""")
        print(f"""\n\t\t\t\t  {cont_200} billetes son de 200""")
        print(f"""\n\t\t\t\t  {cont_500} billetes son de 500""")
        print(f"""\nNuevo balance de cuenta: $ {nuevo_balance}""")
        return copia_monto


atm = Cajero_Automatico()
atm.agregar_billetes(money)
atm.contar_billetes()
atm.extraer_dinero(5000)
atm.extraer_dinero_cambio()
