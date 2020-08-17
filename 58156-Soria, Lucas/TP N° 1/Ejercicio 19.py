import os
import json


class ErrorValorNoValido(Exception):
    pass


class TarjetaCredito():

    def __init__(self, nombre, numero, codigo, tipo):
        self.nombre = nombre
        self.numero = numero
        self.codigo = codigo
        self.tipo = tipo

    def getNombre(self):
        return self.nombre

    def getNumero(self):
        return self.numero

    def getCodigo(self):
        return self.codigo

    def getTipo(self):
        return self.tipo


class Venta():

    def __init__(self, archivo, archivo1):
        self.archivo = archivo
        self.archivo1 = archivo1

    def getMonto(self):
        return self.monto

    def setMonto(self, monto):
        self.monto = monto

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def aDiccionario(self, linea, tarjeta):
        dic = {
            "monto": round(float(self.getMonto()), 2),
            "descripcion": self.getDescripcion(),
            "tajetaCredito": {
                "nombre": tarjeta.getNombre(),
                "numero": tarjeta.getNumero(),
                "codigo": tarjeta.getCodigo(),
                "tipo": tarjeta.getTipo()
            }
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
                tajeta = TarjetaCredito(linea[0], linea[1], linea[2], linea[3])
                self.setMonto(linea[4])
                self.setDescripcion(linea[5])
                dic = self.aDiccionario(linea, tajeta)
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
