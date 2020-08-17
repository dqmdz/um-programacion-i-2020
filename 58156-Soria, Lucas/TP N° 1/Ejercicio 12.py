import random

veces = int(input("Ingrese la cantidad de numeros que quiere generar: "))
num = {}
for i in range(veces):
    num[i] = random.randint(1, 10)

for i in sorted(num.items(), key=lambda x: x[1], reverse=True):
    print("{} salio en posicion {}".format(i[1], i[0]))
