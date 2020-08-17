import time

nro = int(input("Ingrese un numero: "))
c = 0
t1 = time.time()
for x in range(2, nro):
    if nro % x == 0:
        t2 = time.time()
        print("\nEl numero {} no es primo".format(nro))
        print("Porque es divisible por {}".format(x))
        c = 1
        break
if c == 0:
    t2 = time.time()
    print("\nEl numero {} es primo".format(nro))
print("\nTardo {} segundos en calcular".format(t2 - t1))
