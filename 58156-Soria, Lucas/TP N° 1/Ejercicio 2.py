tipo = input("Bienvenido a la pizzeria Bella Napoli\nQue tipo de " +
             "pizza prefiere? Tenemos opcion vegetariana y no" +
             " vegetariana\n").lower()
ingre = [["Peperoni", "Jamon", "Salmon"], ["Pimiento", "Tofu"]]
print("Que ingrediente elige?")
if tipo == "vegetariana":
    for i in ingre[1]:
        print(i)
else:
    for i in ingre[0]:
        print(i)
pizza = input()
print("Usted eligio la pizza {}\nLos ingredientes de su pizza son:" +
      "\nMozzarella\nTomate\n{}".format(tipo, pizza))
