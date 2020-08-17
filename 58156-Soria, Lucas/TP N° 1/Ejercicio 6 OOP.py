import time


class Primo:

    def __init__(self, nro):
        self.nro = nro
        self.x = 2

    def esPrimo(self):
        for self.x in range(2, self.nro):
            if self.nro % self.x == 0:
                return False
        return True


def main():
    while True:
        nro = input("Ingrese un numero: ")
        try:
            if nro == str(int(nro)):
                nro = int(nro)
                break
        except ValueError:
            print("Ingrese un numero entero")
    pri = Primo(nro)
    t1 = time.time()
    if pri.esPrimo():
        print("El numero {} es primo".format(nro))
    else:
        print("El numero {} no es primo, es ".format(nro) +
              "divisible por {}".format(pri.x))
    t2 = time.time()
    print("\nTardo {} segundos en calcular".format(t2 - t1))


if __name__ == "__main__":
    main()
