class curso():
    def __init__(self):
        self.asignaturas=['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
        self.notas=[]
    def asignatura(self):
        print("ingrese la nota que saco en las siguientes asignaturas") 
        for i in self.asignaturas:
            print(i)
            if i == 'Matematica':
                m=input("")
                self.notas.append(m)
            if i == 'Fisica':
                f=input("") 
                self.notas.append(f)   
            if i == 'Quimica':
                q=input("")
                self.notas.append(q)
            if i == 'Historia':
                h=input("")    
                self.notas.append(h)
            if i == 'Lengua':
                l=input("")  
                self.notas.append(l) 
        print("Sus resultafos son")   
        print(self.asignaturas[0],":", self.notas[0],"\n", self.asignaturas[1],":", self.notas[1],"\n", 
        self.asignaturas[2],":", self.notas[2],"\n", self.asignaturas[3],":", self.notas[3],"\n", 
        self.asignaturas[4],":", self.notas[4],"\n") 
        print("A seguir trabajando")

           

        

n=curso()   

n.asignatura() 


