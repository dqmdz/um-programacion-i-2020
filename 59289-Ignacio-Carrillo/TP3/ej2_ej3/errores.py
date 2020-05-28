
class multiploError(Exception):  #extraer multiplo de 100
    pass                         #tested

class dineroInsuficiente(Exception): #cantidad a extrar > dinero en cajero
    pass                             #tested

class imposibleExtraer(Exception): #No tenemos disponibilidad de combinacion de billetes para satisfacer solicitud
    pass                           #tested

class porcentajeCambio(Exception):  #tested
    pass                            #Porcentaje de cambio entre 0 y 100

class extraccionNegativa(Exception): #tested
    pass                            #Monto a extraer superior a cero

class cajeroVacio(Exception):       #tested
    pass                            #El cajero no tiene billetes
