import random


class Aleatorio:

    def __init__(self):
        self.num = {}

    def getNumero(self, i):
        print("{} salio en posicion {}".format(i[1], i[0]))

    def setNumero(self, i):
        self.num[i] = random.randint(1, 10)

    def randomNumbers(self, veces):
        for i in range(veces):
            self.setNumero(i)
        for i in sorted(self.num.items(), key=lambda x: x[1], reverse=True):
            self.getNumero(i)


def main():
    veces = int(input("Ingrese la cantidad de numeros que quiere generar: "))
    alea = Aleatorio()
    alea.randomNumbers(veces)


if __name__ == "__main__":
    main()
