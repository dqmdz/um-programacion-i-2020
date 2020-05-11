import os
import json


def aDiccionario(linea):
    dic = {
           "nombre": linea[0],
           "monto": round(float(linea[1]), 2),
           "descripcion": linea[2],
           "formapago": linea[3]
          }
    return dic


path = os.path.dirname(os.path.abspath(__file__))
nombre = input("Ingrese el nombre del archivo: ")
archivo = open(path + "/" + nombre + ".txt", "r")
archivo1 = open(path + "/" + nombre + ".json", "a")
archivo1.write("[\n")
c = 0
for line in archivo.readlines():
    if c != 0:
        archivo1.write(",\n")
    linea = line.replace("\n", "").split(", ")
    dic = aDiccionario(linea)
    json.dump(dic, archivo1, indent=4)
    c += 1
archivo1.write("\n]\n")
archivo.close()
archivo1.close()
