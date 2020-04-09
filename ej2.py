class pizeria():
    def __init__(self):
        self.pizza = " " 
        self.ingrediente = ""

    
    
    def tipo_de_pizza(self):
        print("ingrese si desea una pizza vegetariana o si desea una pizza no vegetariana")
        self.pizza=(input(">>"))

        if self.pizza == "vegetariana":
       
          
            if self.pizza == "vegetariana":
                print("escriba el ingrediente que desea \n -1: Pimiento\n -2: Tofu ")
                self.ingrediente=input(">>")
                print("su pizza es", self.pizza, "y sus ingredientes son tomate, muzzarella y", self.ingrediente)   
            else:
                print("escriba el ingrediente que desea\n -1:Peperoni\n -2:Salmon\n -3:Jamón ")
                self.ingrediente1=input(">>")
                print("su pizza es", self.pizza, "y sus ingredientes son tomate,muzzarella y", self.ingrediente1)   
                
local=pizeria()   
local.tipo_de_pizza()  
 
