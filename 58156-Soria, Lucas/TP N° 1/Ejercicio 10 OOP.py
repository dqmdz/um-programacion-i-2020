class Fecha:

    def __init__(self):
        self.mes = {"01": "Enero", "02": "Febrero", "03": "Marzo",
                    "04": "Abril", "05": "Mayo", "06": "Junio",
                    "07": "Julio", "08": "Agosto", "09": "Septiembre",
                    "10": "Octubre", "11": "Noviembre", "12": "Diciembre"}
        self.fecha = []

    def convertir(self, fecha):
        self.fecha = fecha.split("/")
        return self.fecha


def main():
    fec = Fecha()
    fecha = fec.convertir(input("Ingrese la fecha en formato dd/mm/aaaa: "))
    print(fecha[0] + " de " + fec.mes[fecha[1]] + " de " + fecha[2])


if __name__ == "__main__":
    main()
