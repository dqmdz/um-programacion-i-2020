user = input("Ingrese su nombre: ").lower()
sex = input("Ingrese su genero (mujer u hombre): ").lower()

if (sex == "mujer" and user < "m") or (sex == "hombre" and user > "n"):
    print("Es parte del grupo A")
else:
    print("Es parte del grupo B")
