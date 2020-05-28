from billete import Billete,Billete_100,Billete_200,Billete_500,Billete_1000
import copy
from errores import dineroInsuficiente,multiploError

class Cajero_automatico():

    def __init__(self):
        self.almacen_interno={'100':[],'200':[],'500':[],'1000':[]}

    def extraer_dinero(self,monto):
        if(monto%100!=0):
            raise multiploError("\n*ERROR**Debe extraer un multiplo de 100") 
        parcial,dinero_total=self.contar_dinero()
        copia_seguridad=copy.deepcopy(self.almacen_interno)
        entrega_billete=[]
        if(dinero_total>=monto):
            while(monto>0):
                if(monto>=1000 and len(self.almacen_interno['1000'])>0):
                    billete=self.almacen_interno['1000'].pop()
                    monto-=billete.denominacion
                    entrega_billete.append(billete)
                elif(monto>=500 and len(self.almacen_interno['500'])>0):
                    billete=self.almacen_interno['500'].pop()
                    monto-=billete.denominacion
                    entrega_billete.append(billete)
                elif(monto>=200 and len(self.almacen_interno['200'])>0):
                    billete=self.almacen_interno['200'].pop()
                    monto-=billete.denominacion
                    entrega_billete.append(billete)
                elif(monto>=100 and len(self.almacen_interno['100'])>0):
                    billete=self.almacen_interno['100'].pop()
                    monto-=billete.denominacion
                    entrega_billete.append(billete)
                else:
                    print("\n**ERROR** No se pudo satisfacer la extraccion por falta de billetes")
                    self.almacen_interno=copy.deepcopy(copia_seguridad)
                    return 1

        else:
            raise dineroInsuficiente("\n**ERROR**Cantidad de dinero insuficente en cajero")
        
        return entrega_billete

    def agregar_dinero(self,lista_billetes):
        for i in range(len(lista_billetes)):
            self.almacen_interno[str(lista_billetes[i].denominacion)].append(lista_billetes[i])

    def vaciar_cajero(self):
        for key,lista in self.almacen_interno.items():
            lista.clear()

    def contar_dinero(self):
        print()
        contador_dinero=[]
        for key,lista in self.almacen_interno.items():
            aux=len(lista)*int(key)
            contador_dinero.append(aux)

        dinero_total=0
        for i in range(len(contador_dinero)):
            dinero_total+=contador_dinero[i]
        
        return contador_dinero,dinero_total

