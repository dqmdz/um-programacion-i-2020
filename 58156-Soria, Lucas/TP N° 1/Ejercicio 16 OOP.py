import os


class Venta:

    def __init__(self, archivo):
        self.archivo = archivo

    def mostrarInfo(self):
        for line in self.archivo.readlines():
            linea = line.split(",")
            print("Nombre: {}, monto: {},".format(linea[0], linea[1],) +
                  "descripcion: {},".format(linea[2]) +
                  " forma de pago: {}".format(linea[3]))


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    nombre = input("Ingrese el nombre del archivo: ")
    print("\nEl archivo contiene la siguiente informacion:\n\n\n")
    archivo = open(path + "/" + nombre + ".txt", "r")
    ven = Venta(archivo)
    ven.mostrarInfo()
    archivo.close()


if __name__ == "__main__":
    main()
