import os
from cajero_automatico import Cajero_automatico
from billete import Billete,Billete_100,Billete_200,Billete_500,Billete_1000

class Api():

    def __init__(self):
        self.cajero=Cajero_automatico() #objeto cajero
        self.lista_billetes=[]

    def ejecutar(self):
        os.system("clear clc")
        print("CAJERO AUTOMATICO")
        flag=True 
        while flag==True:
            menu=self.menu()
            if(menu==1):
                os.system("clear clc")
                self.reconocer_billetes()

            elif(menu==2):
                os.system("clear clc")
                print("\nVaciando cajero...")
                self.cajero.vaciar_cajero()

            elif(menu==3):
                os.system("clear clc")
                monto=int(input("\nIngrese el monto a extraer: "))
                entrega=self.cajero.extraer_dinero(monto)
                total=0
                if(type(entrega) is list):
                    print("\nBilletes entregados: ")
                    for i in range(len(entrega)):
                        print(entrega[i].denominacion)
                        total+=entrega[i].denominacion
                    print("\nTotal entregado: ${}".format(total))

            elif(menu==4):
                os.system("clear clc")
                parcial,total=self.cajero.contar_dinero()
                print("Montos Parciales:")
                for i in range(len(parcial)):
                    print("${}".format(parcial[i]))
                print("Monto Total: ${}".format(total))
            else:
                os.system("clear clc")
                print("\nCerrando Sesion...")
                flag=False
            print()
         
    def cargar_cajero(self):
        if(len(self.lista_billetes)>0):
            self.cajero.agregar_dinero(self.lista_billetes)
        else:
            print("\n**Error al cargar cajero** No se ha ingresado dinero")
        self.lista_billetes.clear()

    def reconocer_billetes(self):
        tipo="Pesos"
        eleccion=int(input("""
        Ingrese la cantidad de billetes de 100: """))
        for i in range(eleccion):
            billete=Billete_100(100,tipo)
            self.lista_billetes.append(billete)
        eleccion=int(input("""
        Ingrese la cantidad de billetes de 200: """))
        for i in range(eleccion):
            billete=Billete_200(200,tipo)
            self.lista_billetes.append(billete)
        eleccion=int(input("""
        Ingrese la cantidad de billetes de 500: """))
        for i in range(eleccion):
            billete=Billete_500(500,tipo)
            self.lista_billetes.append(billete)
        eleccion=int(input("""
        Ingrese la cantidad de billetes de 1000: """))
        for i in range(eleccion):
            billete=Billete_1000(1000,tipo)
            self.lista_billetes.append(billete)
        
        self.cargar_cajero()

    def menu(self):
        while True:
            try:
                eleccion=int(input("""
                Ingrese que desea hacer:
                1- Cargar cajero
                2- Vaciar cajero
                3- Extraer dinero
                4- Contar dinero cajero
                0- Salir
                                    
                Eleccion: """))
                if(eleccion!=1 and eleccion!=2 and eleccion!=3 and eleccion!=4 and eleccion!=0):
                    raise ValueError
                else:
                    break
            except ValueError:
                os.system("clear clc")
                print("\n***ERROR*** Introduzca una opcion válida")

        return eleccion

if __name__ == "__main__":
    api = Api()  
    api.ejecutar()