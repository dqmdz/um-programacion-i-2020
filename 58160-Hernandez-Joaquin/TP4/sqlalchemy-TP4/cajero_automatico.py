from billete import Billete,Billete100,Billete200,Billete500,Billete1000


class Cajero_automatico():
    
    def __init__(self):
        self.almacen_billetes= {'100':[], '200':[], '500':[], '1000':[]}
        

    def agregar_billetes(self,lista_billetes): #Agrega cada billete a su respectiva lista por su key 
        for i in range(len(lista_billetes)):
            self.almacen_billetes[str(lista_billetes[i].denominacion)].append(lista_billetes[i])
        
        valores = self.contar_dinero()
        return "Operacion exitosa !!! se han depositado ${}".format(valores[1])
    
    def contar_dinero(self):# dinero de cada billete en su lista
        self.dinero_parcial=[]
        for key,lista in self.almacen_billetes.items():
            x=len(lista)*int(key) # x variable en se guarda el resultado
            self.dinero_parcial.append(x) #contar cada billete de la lista del dinero entregado por la dominacion 

        self.dinero_total=0
        for i in range(len(self.dinero_parcial)):
            self.dinero_total += self.dinero_parcial[i] # de cada dinero parcial se suma al total
        return self.dinero_parcial,self.dinero_total
        
    def extraer_dinero(self,monto):
        self.dinero_parcial,self.dinero_total= self.contar_dinero()
        
        if monto % 100 != 0:
            return "Error !!! Monto incorrecto, ingrese un valor multiplo de 100"
        if monto > self.dinero_total:
            return "Error !!! monto excede el total del cajero"
        
        self.dinero_entregado = [] #lista para guardar dinero de extraccion SIN CAMBIO

        if (self.dinero_total>=monto):
            while(monto > 0):
                if(monto >= 1000 and len(self.almacen_billetes['1000']) > 0):
                    billete= self.almacen_billetes['1000'].pop()
                    monto-=billete.denominacion
                    self.dinero_total-=billete.denominacion
                    self.dinero_entregado.append(billete)

                elif(monto >= 500 and len(self.almacen_billetes['500']) > 0):
                    billete= self.almacen_billetes['500'].pop()
                    monto-=billete.denominacion
                    self.dinero_total-=billete.denominacion
                    self.dinero_entregado.append(billete) 
                
                elif(monto >= 200 and len(self.almacen_billetes['200']) > 0):
                    billete= self.almacen_billetes['200'].pop()
                    monto-=billete.denominacion
                    self.dinero_total-=billete.denominacion
                    self.dinero_entregado.append(billete) 
                
                elif(monto >= 100 and len(self.almacen_billetes['100']) > 0):
                    billete= self.almacen_billetes['100'].pop()
                    monto-=billete.denominacion
                    self.dinero_total-=billete.denominacion
                    self.dinero_entregado.append(billete)
                
                else:
                    return "Error !!! NO HAY COMBINACION DE BILLETES"
        else:
            return "Error !!! No hay dinero suficiente en el cajero"
        
        # return self.dinero_entregado # LISTA CON LOS OBJETO DE CADA BILLETE

        self.dinero_extraido_total = 0
        for i in range(len(self.dinero_entregado)):  
            self.dinero_extraido_total += self.dinero_entregado[i].denominacion
        d_total = self.dinero_extraido_total 
        return "Operacion Exitosa, Monto extraido ${}".format(d_total)    #Numero entero con dinero extraido (SIN_CAMBIO)


   

# if __name__ == "__main__":
#     #Pruebas 
#     cajero=Cajero_automatico()

#     a=Billete100()
#     b=Billete200()
#     c=Billete500()
#     d=Billete1000()
#     e=Billete200()
#     f=Billete1000()
#     g=Billete1000()
#     h=Billete100()
#     i=Billete200()
#     j=Billete500()
#     k=Billete500()
#     l=Billete100()
#     m=Billete100()
#     n=Billete200()
#     o=Billete500()
#     p=Billete1000()
#     q=Billete100()
#     r=Billete200()
#     s=Billete500()
#     t=Billete1000()
#     u=Billete100()
#     v=Billete100()
#     x=Billete100()
#     w=Billete200()
#     y=Billete200()
#     z=Billete200()

#     lista=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,w,y,z] #Lista con los objetos billete
    
#     valor = cajero.agregar_billetes(lista)
#     print(valor)

#     dinero_ext_total=cajero.extraer_dinero(1000)
#     print(dinero_ext_total)


    #1ra Extraccion SIN CAMBIO
    #cajero.extraer_dinero(2500)
    #print(cajero.dinero_entregado) 
    # print(cajero.dinero_parcial)
    # print(cajero.dinero_total)  
    # print(cajero.dinero_extraido_total) #sin cambio
    #print(cajero.contar_dinero()) 
    # print()

    #2da Extraccion
    # cajero.extraer_dinero(1000) 
    # print(cajero.extraer_dinero)  
    # print(cajero.contar_dinero()) 
    # print()
    # print(cajero.dinero_extraido_total)
    
    # 3ra Extraccion
    # cajero.extraer_dinero(1000)   
    # print(cajero.dinero_extraido_total)
    # #print(cajero.dinero_entregado)#LISTA CON OBJETO BILLETE 1000
    # print(cajero.contar_dinero()) 