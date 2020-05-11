import os

path = os.path.dirname(os.path.abspath(__file__))
nombre = input("Ingrese el nombre del archivo: ")
archivo = open(path + "/" + nombre + ".txt", "r")
print("\nEl archivo contiene la siguiente informacion:\n\n")
for line in archivo.readlines():
    linea = line.split(",")
    print("Nombre: {}, monto: {},".format(linea[0], linea[1]) +
          "descripcion: {}, forma de pago: {}".format(linea[2], linea[3]))
archivo.close()
