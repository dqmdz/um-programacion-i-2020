import random


class Cuenta:

    def __init__(self):
        self.num = []
        self.tot = 0

    def promedio(self):
        for i in range(10):
            self.num.append(random.randint(1, 10))
            self.tot += self.num[i]
        return str(self.tot/10)


def main():
    cue = Cuenta()
    prom = cue.promedio()
    for i in range(10):
        print(cue.num[i])
    print("El promedio es: " + prom)


if __name__ == "__main__":
    main()
