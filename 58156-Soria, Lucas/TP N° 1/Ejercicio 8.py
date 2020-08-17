nota = []
asignatura = []
while True:
    asignatura.append(input("\nIngrese el nombre de una asignatura: "))
    if asignatura[-1] == "":
        print("\n\n")
        asignatura.pop()
        break
    nota.append(input("Ingrese nota: "))
    print("Si quiere parar apriete enter")
for i in range(len(asignatura)):
    print(asignatura[i] + ": " + nota[i])
