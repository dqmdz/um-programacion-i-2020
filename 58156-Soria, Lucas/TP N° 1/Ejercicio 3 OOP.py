class Impares:

    def __init__(self, nro):
        self.nro = nro
        self.nros = ""

    def impares(self):
        for x in range(1, self.nro, 2):
            self.nros += str(x) + ", "
        return self.nros.strip(", ")


def main():
    while True:
        nro = input("Ingrese un numero entero positivo: ")
        try:
            if nro == str(int(nro)) and int(nro) >= 0:
                nro = int(nro)
                break
        except ValueError:
            print("Ingrese un numero entero")
    imp = Impares(nro)
    print(imp.impares())


if __name__ == "__main__":
    main()
