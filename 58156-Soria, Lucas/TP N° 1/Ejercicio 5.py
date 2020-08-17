nro = int(input("Ingrese un numero: "))
line = ""
for i in range(1, nro + 1):
    line = str(i * 2 - 1) + " " + line
    print(line)
