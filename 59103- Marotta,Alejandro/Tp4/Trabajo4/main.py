from db import *
from cajero_completo import *
from billetes import *


if __name__ == "__main__":

    db = DBConexion()
    pDao = PersonaDao(db)
    aDao = ActividadDao(db)
    tDao = TipoActividadDao(db)

    #Crear 2 personas
    persona1 = Persona("Alejandro","Marotta") #por defecto es de tipo "Cliente"
    persona2 = Persona("Martin","Perez")

    pDao.guardar(persona1)
    pDao.guardar(persona2)
    
    #Crear los tipos de actividad --> Deposito y Extraccion
    deposito = TipoActividad("Deposito","Ingreso dinero")
    extraccion = TipoActividad("Extraccion", "Retirar dinero")
    tDao.guardar(deposito)
    tDao.guardar(extraccion)

    #Crear los 2 cajeros, uno para cada persona
    cajero1 = Cajero()
    cajero2 = Cajero()

    #Crear los objetos billetes y depositarlos

    a = Billete_100()
    b = Billete_200()
    c = Billete_500()
    d = Billete_1000()

    deposito_p1 = [a,b,c,d] #$1800
    deposito_p2= [d,d,d] #$3000

    resultado_deposito1 = cajero1.agregar_billetes(deposito_p1)
    resultado_deposito2 =cajero2.agregar_billetes(deposito_p2)

   
    #Crear las 2 actividades de deposito
    act1 = Actividad("Informacion", "Exitoso",resultado_deposito1)
    act1.tipo_actividad = deposito.id
    act1.persona_id = persona1.id

    act2 = Actividad("Informacion", "Exitoso",resultado_deposito2)
    act2.tipo_actividad = deposito.id
    act2.persona_id = persona2.id

    aDao.guardar(act1)
    aDao.guardar(act2)


    #Crear las dos extracciones correctas

    resultado_extraccion1 = cajero1.extraer_dinero(1000)
    resultado_extraccion2 = cajero2.extraer_dinero(2000)

    #Crear las dos actividades de extraccion correctas

    act3 = Actividad("Informacion","Exitoso",resultado_extraccion1)
    act3.tipo_actividad = extraccion.id
    act3.persona_id = persona1.id

    act4 = Actividad("Informacion","Exitoso",resultado_extraccion2)
    act4.tipo_actividad = extraccion.id
    act4.persona_id = persona2.id

    aDao.guardar(act3)
    aDao.guardar(act4)

    #Crear la extraccion incorrecta

    resultado_extraccion3 = cajero1.extraer_dinero(4000)

    #Crear la actividad de extraccion incorrecta

    act5 = Actividad("Informacion","Erroneo",resultado_extraccion3)
    act5.tipo_actividad = extraccion.id
    act5.persona_id = persona1.id

    aDao.guardar(act5)

    #Agrego otras personas para que no quede tan vacio

    persona3 = Persona("Pedro","Gonzales","Empleado")
    pDao.guardar(persona3)

    persona3 = Persona("Julian","Gomez","Empleado")
    pDao.guardar(persona3)

    #Consultas

    usuarios = pDao.buscarTodos()
    for usuario in usuarios:
        print(usuario)

    t_act = tDao.buscarTodos()
    for tipo in t_act:
        print(tipo)

    actividades = aDao.buscarTodos()
    for actividad in actividades:
        print(actividad)

 





    

