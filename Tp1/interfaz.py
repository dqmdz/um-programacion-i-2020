from Billete import billete_100, billete_200, billete_500, billete_1000
from cajero_automatico import Cajero_automatico




def main():
    cien = billete_100(100,'pesos','$100')
    doscientos = billete_200(200,'pesos','$200')
    quinientos = billete_500(500,'pesos','$500')
    mil = billete_1000(1000,'pesos','$1000') 



    c=Cajero_automatico() 
    c.agregar_dinero([cien, doscientos, doscientos, doscientos, quinientos, mil, mil, mil,  cien, cien, cien, cien, cien, cien, cien, cien, mil, quinientos, quinientos, quinientos, doscientos, cien, cien, cien, quinientos, cien])  
    print(c.contar_dinero())         
    c.extraer_dinero(5000, 20) 
    c.sacar_dinero_cambio()
    c.result()

    
    
        

if __name__ == "__main__":
    main()
   
