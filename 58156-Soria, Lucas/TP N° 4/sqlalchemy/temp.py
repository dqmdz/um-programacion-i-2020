"""
db = DBConexion()
personaDAO = PersonaDao(db)
# Definicion de algunos tipos de actividades
# def __init__(self, actividad, descripcion):
tipoDAO = TipoActividadDao(db)
t1 = TipoActividad("Extracción",
                   "Se extrae sierta cantidad de dinero del" +
                   " cajero automatico")
t2 = TipoActividad("Inserción",
                   "Se inserta sierta cantidad de dinero al" +
                   " cajero automatico")
t3 = TipoActividad("Extracción con cambio",
                   "Se extrae sierta cantidad de dinero del" +
                   " cajero automatico, empezando por los " +
                   "billetes mas pequeños")
t4 = TipoActividad("Consulta",
                   "Se consulta la cantidad de dinero disponible" +
                   " en el cajero")
tipoDAO.guardar(t1)
tipoDAO.guardar(t2)
tipoDAO.guardar(t3)
tipoDAO.guardar(t4)
# Definicion de nuevas Actividades
# def __init__(self, resultado, mensaje, descripcion, actividad):
a1 = Actividad(True, "Compra", "Compra de Samsung Galaxy Watch 3", 1)
a2 = Actividad(True, "Extraccion", "Extraccion de 200 pesos", 3)
a5 = Actividad(False, "Compra", "Compra de Samsung Galaxy Watch 3", 1)
# Definimos persona1 y las actividades que hizo
# def __init__(self, dni, nombre, apellido, empleado):
pers1 = Persona(42670460, "Lucas", "Soria", False)
pers1.actividades.append(a5)
pers1.actividades.append(a1)
pers1.actividades.append(a2)
personaDAO.guardar(pers1)
a1 = Actividad(True, "Compra", "Compra de Samsung Galaxy Watch 3", 1)
a2 = Actividad(True, "Extraccion", "Extraccion de 200 pesos", 3)
a3 = Actividad(True, "Deposito", "Deposito de 5000 pesos", 2)
a4 = Actividad(True, "Consulta de saldo", "Se quiere saber si el " +
               "cajero todavia tiene plata", 4)
a5 = Actividad(False, "Compra", "Compra de Samsung Galaxy Watch 3", 1)
# Definimos persona2 y las actividades que hizo
pers2 = Persona(50468952, "Fulano", "De Tal", True)
pers2.actividades.append(a1)
pers2.actividades.append(a2)
pers2.actividades.append(a3)
pers2.actividades.append(a4)
personaDAO.guardar(pers2)
# Modificaciones a la segunda persona (no se permite dni)
pers2 = personaDAO.buscarPorID(50468952)
pers2.nombre = "Belen"
pers2.apellido = "Soria"
personaDAO.modificar(pers2)
# Solicitud de las aplicaciones
personas = personaDAO.buscarTodos()
for persona in personas:
    print(persona)
"""
from Cajero_automatico import Cajero_automatico
from Billete import Billete_de_1000, Billete_de_500, Billete_de_200
from Controlador import Controlador


def main():
    caj = Cajero_automatico()
    mil_pesos = Billete_de_1000("pesos", "$")
    quinientos_pesos = Billete_de_500("pesos", "$")
    doscientos_pesos = Billete_de_200("pesos", "$")
    lista = []
    for x in range(10):
        lista.append(mil_pesos)
        lista.append(quinientos_pesos)
        lista.append(quinientos_pesos)
        lista.append(doscientos_pesos)
    for x in range(5):
        lista.append(doscientos_pesos)
    caj.agregar_dinero(lista)

    con = Controlador([42670460, "Lucas", "Soria", False],
                      ["Voy a comprar algo con 500 pesos", 1, 500], caj)
    con.registrar_actividad()


if __name__ == "__main__":
    main()
