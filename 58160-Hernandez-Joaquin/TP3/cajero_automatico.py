from billete import Billete,Billete100,Billete200,Billete500,Billete1000
from excepciones import Monto_mayor, Monto_multiplo, Combinacion_billetes, Porcentaje, Cajero_vacio, Monto_negativo
class Cajero_automatico():
    
    def __init__(self):
        self.almacen_billetes= {'100':[], '200':[], '500':[], '1000':[]}
        

    def agregar_billetes(self,lista_billetes): #Agrega cada billete a su respectiva lista por su key 
        for i in range(len(lista_billetes)):
            self.almacen_billetes[str(lista_billetes[i].denominacion)].append(lista_billetes[i])
    
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
        
        if self.dinero_total == 0:
            raise Cajero_vacio("Error !!! NO HAY DINERO EN EL CAJERO")        
        if monto % 100 != 0:
            raise Monto_multiplo("Error !!! Monto incorrecto, ingrese un valor multiplo de 100")
        if monto > self.dinero_total:
            raise Monto_mayor("Error !!! Monto excede el total del cajero")
        if monto < 0:
            raise Monto_negativo("Error !!! Monto Negativo")
        
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
                    raise Combinacion_billetes("Error !!! NO HAY COMBINACION DE BILLETES")
        else:
            raise Monto_mayor("Error !!! No hay dinero suficiente en el cajero")
        
        return self.dinero_entregado # LISTA CON LOS OBJETO DE CADA BILLETE

        # self.dinero_extraido_total = 0
        # for i in range(len(self.dinero_entregado)):  
        #     self.dinero_extraido_total += self.dinero_entregado[i].denominacion
        # return self.dinero_extraido_total    #Numero entero con dinero extraido (SIN_CAMBIO)


    def extraer_dinero_cambio(self,monto,porcentaje):
        self.dinero_parcial,dinero_total = self.contar_dinero()

        if self.dinero_total == 0:
            raise Cajero_vacio("Error !!! NO HAY DINERO EN EL CAJERO")               
        if porcentaje < 0 or porcentaje > 100:
            raise Porcentaje("Error!!! Porcentaje incorrecto")
        if monto % 100 != 0:
            raise Monto_multiplo("Error !!! Monto incorrecto, ingrese un valor multiplo de 100")
        if monto > dinero_total:
            raise Monto_mayor("Error !!! monto excede el total del cajero")
        if monto < 0:
            raise Monto_negativo("Error !!! Monto Negativo")
        

        porcentaje = int(monto * porcentaje / 100) #Porcentaje 2100*10/100 210 pero aproxima a 300 (mayor)
        self.dinero_porcentaje = porcentaje
        
        self.dinero_entregado_cc = []

        if (dinero_total>=self.dinero_porcentaje): 
            while(self.dinero_porcentaje > 0): #LISTA AL REVES DE MENOR A MAYOR                
                if(len(self.almacen_billetes['100']) > 0):
                    billete= self.almacen_billetes['100'].pop()
                    self.dinero_porcentaje-=billete.denominacion
                    dinero_total-=billete.denominacion
                    self.dinero_entregado_cc.append(billete)

                elif(len(self.almacen_billetes['200']) > 0):
                    billete= self.almacen_billetes['200'].pop()
                    self.dinero_porcentaje-=billete.denominacion
                    dinero_total-=billete.denominacion
                    self.dinero_entregado_cc.append(billete) 
                
                elif(len(self.almacen_billetes['500']) > 0):
                    billete= self.almacen_billetes['500'].pop()
                    self.dinero_porcentaje-=billete.denominacion
                    dinero_total-=billete.denominacion
                    self.dinero_entregado_cc.append(billete) 
                
                elif(len(self.almacen_billetes['1000']) > 0):
                    billete= self.almacen_billetes['1000'].pop()
                    self.dinero_porcentaje-=billete.denominacion
                    dinero_total-=billete.denominacion
                    self.dinero_entregado_cc.append(billete)
                    
        else:
            raise Monto_mayor("\nError !!! No hay dinero suficiente en el cajero")
        # print(self.dinero_entregado_cc) #LISTA CON LOS OBJETO DE CADA BILLETE
        self.dinero_extraido_total_cc = 0
        for i in range(len(self.dinero_entregado_cc)):
            self.dinero_extraido_total_cc += self.dinero_entregado_cc[i].denominacion

        self.sin_cambio = monto - self.dinero_extraido_total_cc 
        # print(self.sin_cambio)
        # print(self.dinero_extraido_total_cc) #Numero entero del dinero extraido
        # print(self.dinero_porcentaje)
        
        self.extraer_dinero(self.sin_cambio)  #funcion de extraer dinero pero con el monto(SIN_CAMBIO)
        # print(self.dinero_entregado)
        self.dinero_entregado_cc.extend(self.dinero_entregado) #Lista con los obj de cada billete (de la extraer_dinero)
        return self.dinero_entregado_cc

        # self.total= self.dinero_extraido_total_cc + self.sin_cambio
        # print(self.total) #Dinero de Extraccion (SIN CAMBIO)
        

if __name__ == "__main__":
    #Pruebas 
    cajero=Cajero_automatico()

    a=Billete100()
    b=Billete200()
    c=Billete500()
    d=Billete1000()
    e=Billete200()
    f=Billete1000()
    g=Billete1000()
    h=Billete100()
    i=Billete200()
    j=Billete500()
    k=Billete500()
    l=Billete100()
    m=Billete100()
    n=Billete200()
    o=Billete500()
    p=Billete1000()
    q=Billete100()
    r=Billete200()
    s=Billete500()
    t=Billete1000()
    u=Billete100()
    v=Billete100()
    x=Billete100()
    w=Billete200()
    y=Billete200()
    z=Billete200()

    lista=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,w,y,z] #Lista con los objetos billete
    
    cajero.agregar_billetes(lista)
    print(cajero.almacen_billetes)
    print(cajero.contar_dinero())

    #1ra Extraccion SIN CAMBIO
    #cajero.extraer_dinero(2500)
    #print(cajero.dinero_entregado) 
    # print(cajero.dinero_parcial)
    # print(cajero.dinero_total)  
    # print(cajero.dinero_extraido_total) #sin cambio
    #print(cajero.contar_dinero()) 
    # print()

    #1er Extraccion CON CAMBIO
    #cajero.extraer_dinero_cambio(7000,10)   
    #print(cajero.contar_dinero())  
    # print(cajero.dinero_extraido_total_cc) # con cambio 
    # print()

    #2da Extraccion
    # cajero.extraer_dinero(1000) 
    # print(cajero.dinero_extraido_total)  
    # print(cajero.contar_dinero()) 
    # print()
    
    # 3ra Extraccion
    # cajero.extraer_dinero(1000)   
    # print(cajero.dinero_extraido_total)
    # #print(cajero.dinero_entregado)#LISTA CON OBJETO BILLETE 1000
    # print(cajero.contar_dinero()) 