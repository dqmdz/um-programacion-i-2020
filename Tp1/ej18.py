from io import open
class error():
    
   
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
            if "" in venta:
                raise Exception ("error en archivo.txt")
               
            
        
            
t=error()
t.reading_text()