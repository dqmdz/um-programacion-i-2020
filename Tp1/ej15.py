from io import open

class text():
   
    def reading_text(self):
        f = open('archivo.txt','r')
        texto = f.read()
        f.close()
        print(texto)


t=text()
t.reading_text()
