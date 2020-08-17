class Texto:

    def __init__(self):
        self.texto = '''
La soja es la principal producción del agro argentino. Su producción se
 realiza en Argentina desde hace varias décadas, siendo introducida en la
 década del 70. Es entonces cuando comienza el proceso de “sojización”
 del agro argentino, aumentando sostenida y significativamente la superficie
 utilizada para este cultivo. Paralelamente, la introducción de semillas
 transgénicas entre otras tecnologías innovadoras y el incremento de la
 capacidad de procesamiento de granos, han colaborado al crecimiento de
 la industria.
Argentina cuenta con ciertas ventajas cuando se enfrenta al mercado
 internacional como los favorables precios relativos y la preexistencia de una
 base tecnológica, productiva y empresaria que fue trasladada de otras
 actividades a la producción y procesamiento de la soja. Por otro lado, la
 capacidad de procesamiento del grano, tanto a través de inversiones para
 aumentar la capacidad de molienda, como en la mejora de los puertos para
 exportación, ha mejorado año a año.
Aunque la producción de soja ha aumentado en las últimas décadas,
 naturalmente el crecimiento muestra altibajos, producto de que todavía la
 incidencia climática es demasiado alta, las sequías, lluvias extremas,
 piedras, entre otras causales, pueden generar una mala cosecha más allá de
 los avances tecnológicos con los que se cuente. Debido a estas fluctuaciones
 naturales de la producción de soja, también las exportaciones de soja
 presentan fluctuaciones. Sin embargo, las ventas al exterior también dependen
 del comportamiento especulativo de los productores; como la exportación está
 concentrada en pocas grandes empresas, éstas especulan con el precio de la
 soja. Así retienen las cosechas hasta situaciones de tipo de cambio
 favorables y devaluaciones del peso.
La importancia del cultivo de soja en Argentina radica en que la mayor parte
 de la producción no es consumida en el interior del país, sino que es
 exportada. Es la última década las exportaciones de soja han llegado a
 representar entre el 26 y el 31 de las exportaciones totales. Esto
 significa entonces que la soja no sólo tiene una gran importancia fiscal en
 el país en forma de impuestos cobrados, sino que es también la causa de la
 entrada de una gran cantidad de divisas.
En el contexto internacional Argentina compite históricamente por el puesto
 de mayor exportador de soja con Estados Unidos y Brasil, siendo estos los
 principales competidores de las exportaciones nacionales. Por otro lado,
 nuestros principales compradores de soja son China y la Zona Euro.
'''
        self.palabras = {}
        self.pal = {}

    def top20(self):
        for i in self.texto.lower().replace("," or "." or "-" or "\n",
                                            "").split(" "):
            if i not in self.palabras.keys():
                self.palabras[i] = 1
            else:
                self.palabras[i] += 1
        c = 0
        for i in sorted(self.palabras.items(), key=lambda x: x[1],
                        reverse=True):
            if c == 20:
                break
            self.pal[i[0]] = i[1]
            c += 1
        return self.pal


def main():
    tex = Texto()
    pal = tex.top20()
    for i in sorted(pal.items()):
        print("'{}' se repitio {} veces".format(i[0], i[1]))


if __name__ == "__main__":
    main()
