materias = {}
total = 0

while True:
    mat = input("\nIngrese el nombre de una materia: ")
    if mat == "":
        break
    materias[mat] = int(input("Ingrese los creditos de la materia: "))
    print("Si quiere parar apriete enter")
print("\n\n\n")
for i in materias:
    print(i + " tiene " + str(materias[i]) + " creditos")
    total += materias[i]
print("\nEn total hay {} creditos".format(total))
