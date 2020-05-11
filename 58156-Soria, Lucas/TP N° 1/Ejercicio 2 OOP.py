class Pizza:

    def __init__(self, tipo):
        self.tipo = tipo
        self.ingre = [["Peperoni", "Jamon", "Salmon"], ["Pimiento", "Tofu"]]

    def ingredientes(self):
        print("Que ingrediente elige?")
        if self.tipo == "v":
            for i in self.ingre[1]:
                print(i)
            i = 1
        else:
            for i in self.ingre[0]:
                print(i)
            i = 0
        while True:
            elige = input().capitalize()
            if elige in self.ingre[i]:
                break
            else:
                print("Perdon, no tenemos ese ingrediente")
        return elige


def main():
    print("Bienvenido a la pizzeria Bella Napoli\nQue tipo de " +
          "pizza prefiere?")
    while True:
        tipo = input("Tenemos opcion vegetariana (V) y no" +
                     " vegetariana (NV)\n").lower()
        if tipo == "v" or tipo == "nv":
            break
        else:
            print("Debe escribir v o nv, segun prefiera")
    pizza = Pizza(tipo)
    elige = pizza.ingredientes()
    print("\n\nLos ingredientes de su pizza son:" +
          "\nMozzarella\nTomate\n{}".format(elige))


if __name__ == "__main__":
    main()
