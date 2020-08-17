class Triangulo:

    def __init__(self, nro):
        self.nro = nro

    def dibujo(self):
        line = ""
        linef = ""
        for i in range(1, self.nro + 1):
            line = str(i * 2 - 1) + " " + line
            linef += line + "\n"
        return linef


def main():
    while True:
        nro = input("Ingrese un numero: ")
        try:
            if nro == str(int(nro)):
                nro = int(nro)
                break
        except ValueError:
            print("Ingrese un numero entero")
    tri = Triangulo(nro)
    print(tri.dibujo())


if __name__ == "__main__":
    main()
