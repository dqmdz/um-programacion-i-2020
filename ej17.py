import json 
class text():
   
    def reading_text(self):
        j = open('archivo.json', 'w')
        f = open('archivo.txt','r')
        texto = f.readlines()
        print(texto)
        num=0
        f.seek(0)
        for i in texto:
            num=num+1
            print("venta numero", str(num),':')
            r=i.split(",")
            diccionario={'Nombre': r[0], 'Monto':r[1],'Descripcion':r[2], 'Forma de pago':r[3]}
            print(diccionario)
            json.dump(diccionario, j, indent=1)

        
         

t=text()
t.reading_text()