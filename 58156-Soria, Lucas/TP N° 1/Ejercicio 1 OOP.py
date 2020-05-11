class Group:

    def separator(self, user, sex):
        if (sex == "mujer" and user < "m") or (sex == "hombre" and user > "n"):
            return "Es parte del grupo A"
        else:
            return "Es parte del grupo B"


def main():
    user = input("Ingrese su nombre: ").lower()
    sex = input("Ingrese su genero (mujer u hombre): ").lower()
    gro = Group()
    print(gro.separator(user, sex))


if __name__ == "__main__":
    main()
