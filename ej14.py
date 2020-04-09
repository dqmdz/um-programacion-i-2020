import operator

class read():
    def __init__(self):
       
        self.texto=[]
    
    def texto_(self):
        t='''Python es uno de los lenguajes de programación
        dinámicos más populares que existen
        entre los que se encuentran Perl, Tcl, 
        PHP y Ruby. Aunque es considerado a menudo 
        como un lenguaje scripting es realmente 
        un lenguaje de propósito general.
        En la actualidad, Python es usado para 
        todo, desde simples "scripts", hasta grandes 
        servidores web que proveen servicio 
        ininterrumpido 24×7. 
        Es utilizado para la 
        programación de interfaces gráficas y 
        bases de datos, programación web tanto en 
        el cliente como en el servidor véase Django o Flask) 
        y testing de aplicaciones. 
        Además tiene una amplia aceptación por 
        científicos que hacen aplicaciones para las 
        supercomputadores más rápidas del mundo y por 
        los niños que recién están comenzando 
        a programar.'''
         
        listaPalabras = t.lower().split()

    
        for i in listaPalabras:
            self.texto.append(listaPalabras.count(i))
        
        print("Cadena\n" + t + "\n")
        print("Lista\n" + str(sorted(listaPalabras)) + "\n")
        print("Frecuencias\n" + str(self.texto) + "\n")
        lista=(str(list(zip(listaPalabras, self.texto))))
        print("Pares\n", lista)
    

        
        
text=read()
text.texto_()        














