class pizeria():
    def __init__(self):
        self.


print("ingrese 1 si desea una pizza vegetariana y 2 si desea una pizza no vegetariana")
pizza=int(input(">>"))

if pizza == 1:
    print("escriba el ingrediente que desea \n -1: Pimiento\n -2: Tofu ")
    ingrediente=input(">>")

    if ingrediente.upper() == "PIMIENTO" or ingrediente.upper() == "TOFU":
        print("Su pizza es vegetariana")
        print("sus ingredeintes son muzzarella,tomate y", ingrediente)
    else:
        print("ingrese nuevamente 1 o 2")    
else:
    print("escriba el ingrediente que desea\n -1:Peperoni\n -2:Salmon\n -3:Jamón ")
    ingrediente1=input(">>")
    if ingrediente1.upper() == "PEPERONI" or ingrediente1.upper() == "SALMON" or ingrediente1.upper() == "JAMON":
        print("su pizza es no vegetariana y sus ingredientes son\n")
        print("muzzarella, tomate y", ingrediente1)  
    else:
        print("pruebe de nuevo")          
    