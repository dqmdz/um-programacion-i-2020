class fecha():
    def __init__(self):
        self.meses=['.','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        self.fecha=''

    
    def ingresar_fecha(self):
        self.fecha=input("ingrese la fecha separado con barras: ")
        lista=self.fecha.split("/")
        mes = self.meses[int(lista[1])]   
        print(lista[0], "de", mes, "de", lista[2])



u=fecha()
u.ingresar_fecha()