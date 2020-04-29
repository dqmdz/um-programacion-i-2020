print("ingrese un numero entero")
n=int(input(">>"))
lista=[]

for i in range(1, n, 2):
        lista.append(i)
        lista.sort()
        lista.reverse()
        print(lista)

        
