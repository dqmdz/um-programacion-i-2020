import os
import json


class ErrorValorNoValido(Exception):
    pass


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
    try:
        linea = line.replace("\n", "").split(", ")
        if "" in linea:
            raise ErrorValorNoValido
        if c != 0:
            archivo1.write(",\n")
        dic = aDiccionario(linea)
        json.dump(dic, archivo1, indent=4)
        c += 1
    except ErrorValorNoValido:
        print("\n\nOcurrió un problema con la fuente de datos\n\n")
        continue
archivo1.write("\n]\n")
archivo.close()
archivo1.close()
