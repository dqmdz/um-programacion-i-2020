
class Cajero():
    
    def __init__(self):

        self.total = 0
       
        self.lista_100 = []
        self.lista_200 = []
        self.lista_500 = []
        self.lista_1000 = []

        self.suma_100 = 0
        self.suma_200 = 0
        self.suma_500 = 0
        self.suma_1000 = 0

    
    
    def agregar_billetes(self,lista):

        for billete in lista:
            
            if billete.valor == 100:
                self.lista_100.append(billete)
                
            if billete.valor == 200:
                self.lista_200.append(billete)
               
            if billete.valor == 500:
                self.lista_500.append(billete)
                
            if billete.valor == 1000:
                self.lista_1000.append(billete)

        #creo listas auxiliares para guardar los valores por si falla la extraccion

        self.aux100,self.aux200,self.aux500,self.aux1000 = self.lista_100.copy(),self.lista_200.copy(),self.lista_500.copy(),self.lista_1000.copy()

        valores = self.contar()

        return "Operacion Exitosa se ha ingresado ${}".format(valores[-1])
           

    def contar(self):       
 
             
        self.cant_b100 = len(self.lista_100)
        self.cant_b200 = len(self.lista_200)
        self.cant_b500 = len(self.lista_500)
        self.cant_b1000 = len(self.lista_1000)

        self.suma_100 = self.cant_b100 * 100
        self.suma_200 = self.cant_b200 *200
        self.suma_500 = self.cant_b500 *500
        self.suma_1000 = self.cant_b1000 *1000

        self.total = self.suma_100 + self.suma_200 + self.suma_500 + self.suma_1000
      

        return self.cant_b100,self.suma_100,self.cant_b200,self.suma_200,self.cant_b500,self.suma_500,self.cant_b1000,self.suma_1000, self.total


    def comprobar(self,monto): #como en ambos extraer debo comprobar lo mismo, mejor creo una funcion que lo haga

        self.contar() #largo esta funcion para que actualice los valores

        if monto % 100 == 0:

            if self.total > monto:
                return "OK"
            
            else:
                return "Error. Quiere sacar mas dinero del que puede"
        
        else:
            return "Error. El monto es incorrecto.No es multiplo de 100"

    
    def extraer_dinero(self,monto):

        lista_extraidos = []

        valor = monto

        bandera = self.comprobar(monto)

        if bandera == "OK":
            
            try: #por si la combinacion de billetes que hay no sirven para el monto pedido
                
                while len(self.aux1000) > 0 and monto >= 1000:
                    
                    monto = monto - 1000

                    billete = self.aux1000.pop()
                   
                    lista_extraidos.append(billete)
                            

                while len(self.aux500) > 0 and monto >= 500:
                   
                    monto = monto - 500

                    billete = self.aux500.pop()
                   
                    lista_extraidos.append(billete)

                while len(self.aux200) > 0 and monto >= 200:
                   
                    monto = monto - 200

                    billete = self.aux200.pop()
                   
                    lista_extraidos.append(billete)

                while len(self.aux100) > 0 and monto >= 100:
                   
                    monto = monto - 100

                    billete = self.aux100.pop()
                   
                    lista_extraidos.append(billete)

                if monto == 0:
                    #si todo sale bien se auctualizan los valores de las lostas de billetes                   
                    self.lista_100,self.lista_200,self.lista_500,self.lista_1000 = self.aux100.copy(),self.aux200.copy(),self.aux500.copy(),self.aux1000.copy()
                    
                    return "Operacion exitosa, se ha extraido ${}".format(valor)

                else:
                    raise Exception                                         
                                      
            except:
                #si falla recupera los valores iniciales
                self.aux100,self.aux200,self.aux500,self.aux1000 = self.lista_100.copy(),self.lista_200.copy(),self.lista_500.copy(),self.lista_1000.copy() 
                
                return "Error. No hay una combinación de billetes que nos permita extraer ese monto."                                
            
        else:
            return bandera


