

class text():
   
    def reading_text(self):
        f = open('archivo.txt','r')
        texto = f.readlines()
        print(texto)
        num=0
        f.seek(0)
        for i in texto:
            num=num+1
            print("venta numero", str(num),':')
            r=i.split(",")
            print(('Nombre:{c}, Monto:{m}, Descripcion:{d}, Forma de pago:{p}').format(
                c=r[0],
                m=r[1],
                d=r[2],
                p=r[3]))
            
t=text()
t.reading_text()

