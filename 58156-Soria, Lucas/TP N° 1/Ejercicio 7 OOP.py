class Frase:

    def __init__(self, frase):
        self.frase = frase

    def veces(self, letra):
        return self.frase.count(letra)


def main():
    frase = input("Ingrese una frase: ").replace("", ",").strip(",").split(",")
    letra = input("Ingrese una letra: ")
    fra = Frase(frase)
    vec = fra.veces(letra)
    print("La cantidad de letras '{}' en la frase es: {}".format(letra, vec))


if __name__ == "__main__":
    main()
