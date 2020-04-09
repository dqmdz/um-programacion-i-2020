from io import open
class text():
   
    def reading_text(self):
        lista = []
        r=open('archivo.txt', 'r')
        txt=r.read()
        print(txt)
        for i in txt:
            lista.append(i)
        for k in lista:
            venta = k.split(',')
            print(venta)
            for esp in venta:
                if esp != '':
                    continue
                else:
                    raise Exception('Error en >> archivo.txt')
               
            print(esp)
        
            
t=text()
t.reading_text()