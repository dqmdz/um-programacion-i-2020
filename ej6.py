class primo():
   
    def __init__(self):
        self.numero=0
    
    
    def es_primo(self,num):
        self.numero = num
        if self.numero < 2:     
            return False
        for i in range(2, num):  
            if self.numero % i == 0: 
                return "el numero no es primo"
            return "el numero es primo"


num=int(input(">>"))
n = primo()
h=n.es_primo(num)
print(h)
