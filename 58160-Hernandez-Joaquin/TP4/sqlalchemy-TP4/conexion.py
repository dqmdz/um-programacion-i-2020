from DB import DBConexion,Persona,Actividad,Tipo_Actividad,PersonaDao,ActividadDao,Tipo_ActividadDao
from billete import Billete100,Billete200,Billete500,Billete1000
from cajero_automatico import Cajero_automatico

if __name__ == "__main__":

    print("Conectandose a la base de datos")
    print("Creando la estructura de las tablas")
    print("Creando la sesion de acceso a la base de datos")
    db = DBConexion()

    print("Creando DAO")
    persona_DAO = PersonaDao(db)
    actividad_DAO = ActividadDao(db)
    tipo_DAO = Tipo_ActividadDao(db)
       
    
    pers1 = Persona("Joaquin", "Hernandez", "Cliente")
    pers2 = Persona("Armando","Esteban Quito", "Cliente")
    
    persona_DAO.guardar(pers1)
    persona_DAO.guardar(pers2)
    
    cargar_dinero = Tipo_Actividad("Deposito", "Ingresar dinero")
    extraer_dinero =  Tipo_Actividad("Extraccion", "Extraer dinero")
    tipo_DAO.guardar(cargar_dinero)
    tipo_DAO.guardar(extraer_dinero)
    
    cajero1 = Cajero_automatico()
    cajero2 = Cajero_automatico()
    
    #Creo Billetes
    a=Billete100()
    b=Billete200()
    c=Billete500()
    d=Billete1000()
    e=Billete200()
    f=Billete1000()

    dep1=[a,b,c,d,e,f] #3000 #Deposito1
    dep2=[a,a,b,b,c,c,d,d] #3600 #Deposito2
    
    agr_bill_1 = cajero1.agregar_billetes(dep1)
    agr_bill_2 = cajero2.agregar_billetes(dep2)
    
    #Acitvidad de deposito
    #ACTIVIDAD 1
    a1 = Actividad("Informacion",agr_bill_1)
    a1.tipo_actividad = cargar_dinero.id
    a1.persona_id = pers1.id
    pers1.actividad.append(a1) #Guardo actividad 1
    persona_DAO.guardar(pers1) #Forma distinta a la actividad 2

    #ACITIVIDAD 2
    a2 = Actividad("Informacion",agr_bill_2)
    a2.tipo_actividad = cargar_dinero.id
    a2.persona_id= pers2.id
    actividad_DAO.guardar(a2) #Guardo actividad 2

    
    extraccion_1 = cajero1.extraer_dinero(1500)
    extraccion_2 = cajero2.extraer_dinero(2000)

    pers3 = Persona("Robin", "Hood", "Cliente")
    persona_DAO.guardar(pers3)
    
    pers4 = Persona("Ignacio", "Cabrera", "Cliente")
    persona_DAO.guardar(pers4)


    #ACTIVIDAD 3
    a3 = Actividad("Informacion",extraccion_1)
    a3.tipo_actividad = extraer_dinero.id
    a3.persona_id = pers3.id
    actividad_DAO.guardar(a3)

    #ACTIVIDAD 4
    a4 = Actividad("Informacion",extraccion_2)
    a4.tipo_actividad = extraer_dinero.id
    a4.persona_id = pers4.id
    actividad_DAO.guardar(a4)

    #ACTIVIDAD 5
    extraccion_3 = cajero2.extraer_dinero(10000) #Extraccion inconrrecta
    a5 = Actividad("Informacion",extraccion_3)
    a5.tipo_actividad = extraer_dinero.id
    a5.persona_id = pers1.id
    actividad_DAO.guardar(a5)

    
    personas = persona_DAO.buscarTodos()
    for persona in personas:
        print(persona)

#sudo docker-compose rm && sudo docker rmi tp4_aplicacion:latest  && sudo docker-compose up aplicacion