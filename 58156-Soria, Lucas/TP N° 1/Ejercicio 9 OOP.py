class Contacto:

    def __init__(self):
        self.dic = {}

    def getNombre(self):
        return self.dic["nombre"]

    def setNombre(self, nombre):
        self.dic["nombre"] = nombre

    def getEdad(self):
        return self.dic["edad"]

    def setEdad(self, edad):
        self.dic["edad"] = edad

    def getDireccion(self):
        return self.dic["direccion"]

    def setDireccion(self, direccion):
        self.dic["direccion"] = direccion

    def getTelefono(self):
        return self.dic["telefono"]

    def setTelefono(self, telefono):
        self.dic["telefono"] = telefono


def main():
    con = Contacto()
    con.setNombre(input("Como te llamas? "))
    con.setEdad(input("Cuantos años tenes? "))
    con.setDireccion(input("Adonde vivis? "))
    con.setTelefono(input("Cual es tu telefono? "))
    print(con.getNombre() + " tiene " + con.getEdad() + " años, vive en " +
          con.getDireccion() + " y su numero de telefono es: " +
          con.getTelefono())


if __name__ == "__main__":
    main()
