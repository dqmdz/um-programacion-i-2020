class Materias:

    def __init__(self):
        self.materias = {}
        self.total = 0

    def setMateria(self, materia, creditos):
        self.materias[materia] = creditos

    def mostrar(self):
        print("\n\n\n")
        for i in self.materias:
            print(i + " tiene " + str(self.materias[i]) + " creditos")
            self.total += self.materias[i]
        print("\nEn total hay {} creditos".format(self.total))


def main():
    materias = Materias()
    while True:
        mat = input("\nIngrese el nombre de una materia: ")
        if mat == "":
            break
        materias.setMateria(mat, int(input("Ingrese los creditos de la " +
                                           "materia: ")))
        print("Si quiere parar apriete enter")
    materias.mostrar()


if __name__ == "__main__":
    main()
