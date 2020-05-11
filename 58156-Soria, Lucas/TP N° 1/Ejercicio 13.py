import random

num = []
tot = 0
for i in range(10):
    num.append(random.randint(1, 10))
    tot += num[i]
    print(num[i])
print("El promedio es: " + str(tot/10))
