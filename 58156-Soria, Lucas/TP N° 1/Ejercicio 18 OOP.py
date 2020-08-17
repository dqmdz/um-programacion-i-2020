import os
import json


class ErrorValorNoValido(Exception):
    pass


class Venta:

    def __init__(self, archivo, archivo1):
        self.archivo = archivo
        self.archivo1 = archivo1

    def aDiccionario(self, linea):
        dic = {
               "nombre": linea[0],
               "monto": round(float(linea[1]), 2),
               "descripcion": linea[2],
               "formapago": linea[3]
              }
        return dic

    def convertirInfo(self):
        self.archivo1.write("[\n")
        c = 0
        for line in self.archivo.readlines():
            try:
                linea = line.replace("\n", "").split(", ")
                if "" in linea:
                    raise ErrorValorNoValido
                if c != 0:
                    self.archivo1.write(",\n")
                dic = self.aDiccionario(linea)
                json.dump(dic, self.archivo1, indent=4)
                c += 1
            except ErrorValorNoValido:
                print("\n\nOcurrió un problema con la fuente de datos\n\n")
                continue
        self.archivo1.write("\n]\n")


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    nombre = input("Ingrese el nombre del archivo: ")
    archivo = open(path + "/" + nombre + ".txt", "r")
    archivo1 = open(path + "/" + nombre + ".json", "a")
    ven = Venta(archivo, archivo1)
    ven.convertirInfo()
    archivo.close()
    archivo1.close()


if __name__ == "__main__":
    main()
