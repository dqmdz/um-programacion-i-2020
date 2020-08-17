nro = int(input("Ingrese un numero entero positivo: "))
nros = ""
for x in range(1, nro, 2):
    nros += str(x) + ", "
print(nros.strip(", "))
