class Materia:

    def __init__(self):
        self.nota = []
        self.asignatura = []

    def almacenar(self):
        while True:
            self.asignatura.append(input("\nIngrese el nombre de una" +
                                         " asignatura: "))
            if self.asignatura[-1] == "":
                print("\n\n")
                self.asignatura.pop()
                return None
            self.nota.append(input("Ingrese nota: "))
            print("Si quiere parar apriete enter")

    def mostrar(self):
        for i in range(len(self.asignatura)):
            print(self.asignatura[i] + ": " + self.nota[i])


def main():
    mat = Materia()
    mat.almacenar()
    mat.mostrar()


if __name__ == "__main__":
    main()
