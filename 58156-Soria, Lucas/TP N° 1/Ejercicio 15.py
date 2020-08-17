import os

path = os.path.dirname(os.path.abspath(__file__))
nombre = input("Ingrese el nombre del archivo: ")
archivo = open(path + "/" + nombre + ".txt", "r")
print("\nEl archivo contiene la siguiente informacion:\n\n\n")
for line in archivo.readlines():
    print(line)
archivo.close()
