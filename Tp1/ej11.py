class asignaturas():
    def __init__(self):
        self.diccionario={'Matemáticas': 6, 'Física': 4, 'Química': 5}
        
    def imprimir(self):
        
        for asignatura,créditos in self.diccionario.items():
            print("%s tiene %s" %(asignatura,créditos))
        
      
        suma=sum(self.diccionario.values())

        print("La cantidad total de créditos del curso es", suma)


alumno=asignaturas()

alumno.imprimir()





