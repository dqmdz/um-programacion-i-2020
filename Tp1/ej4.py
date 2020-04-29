class triangulo():
    def __init__(self):
       self.altura = 0

    def altura_triangulo(self):   
        self.altura = int(input("Introduce la altura del triángulo (entero positivo): "))
   
    def recorrer(self):
        for i in range(self.altura):
            for j in range(i+1):
                print("*", end=" ")
            print(" ")

alt=triangulo()

alt.altura_triangulo()
alt.recorrer()