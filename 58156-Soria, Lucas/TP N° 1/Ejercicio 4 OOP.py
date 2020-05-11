class Triangulo:

    def __init__(self, nro):
        self.nro = nro

    def dibujo(self):
        patron = ""
        for x in range(1, self.nro + 1):
            patron += "*" * x + "\n"
        return patron


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
