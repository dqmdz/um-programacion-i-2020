import datetime
from functools import wraps


# Haciendo llamadas "manualmente"
'''
Este metodo utiliza funciones como parametro de otras funciones,
creacion de funciones dentro de funciones,
devoucion de funciones como resultado de otras y
hace el cambio del nombre de una funcion y su comportamiento
Se estaria reescribiendo la funcion "funcion1"
'''


def funcion1():
    print("No hace mucho, solo este cartel")


def timmer1(funcion):

    def wrapper():
        antes = datetime.datetime.now()
        funcion()
        print("La funcion tomó: {} tiempo".format(datetime.datetime.now() -
                                                  antes))

    return wrapper


print("Vamos a tomar el tiempo que toma mi funcion de forma manual:")
funcion1 = timmer1(funcion1)
funcion1()


# Haciendo el metodo con decoradores
'''
Hace lo mismo recien, pero mucho mas rapido
'''


@timmer1
def funcion2():
    print("No hace mucho, solo este cartel")


print("\nVamos a tomar el tiempo que toma mi funcion con el decorador:")
funcion2()


# Metiendo un numero indefinido de parametros
'''
'''


def timmer2(funcion):

    def wrapper(*parametros):
        antes = datetime.datetime.now()
        print(*parametros)
        print(parametros)
        funcion(*parametros)
        print("La funcion tomó: {} tiempo\n".format(datetime.datetime.now() -
                                                    antes))

    return wrapper


@timmer2
def funcion3(uno, dos):
    print("Tenemos dos variables, que loco:")
    print(uno, dos)


@timmer2
def funcion4(uno, dos, tres, cuatro):
    print("Tenemos cuatro variables, que loco:")
    print(uno, dos, tres, cuatro)


print("\nVamos a tomar el tiempo que toma mi funcion con el decorador"
      " y parametros variables:")
funcion3("uno", "dos")
funcion4("uno", "dos", "tres", "cuatro")


# Pasando parametros multiples como lista y como diccionario
'''
Creo que se explica solo
'''


def funcion5(*args, **kargs):
    print("Los parametros metidos a *args:")
    for elem in args:
        print("valor: {}".format(elem))
    print("Los parametros metidos a *args:")
    for key in kargs:
        print("Clave: {} - valor: {}".format(key, kargs[key]))


print("\nVamos a tomar parametros multiples como lista y como diccionario:")
funcion5("parametro1", "parametro2", param1="par1", param2="par2",
         param3="par3",)


# Pasando parametros al decorador
'''
Para poder hacer funciones utiles en el decorador
'''


def decorador_parametrizado(parametro_decorador):
    def decorador_de_los_de_antes(funcion):
        def decorador_al_fin():
            print("Que locura lo que hay que hacer para"
                  " parametrizar un decorador")
            print("Pero bueno, '{}'".format(parametro_decorador))
            funcion()
        return decorador_al_fin
    return decorador_de_los_de_antes


@decorador_parametrizado("Esto es un parametro")
def funcion6():
    print("Y hasta esto llegamos....")


print("\n\nComplete madness...")
funcion6()


# Una forma de hacer lo mismo pero con un cambio
'''
Esto ayuda a que cuando se arroba (decora)
una funcion, esta no pierda su identidad, que no
deje de apuntar el nombre de esa funcion a la funcion
misma y empiece a apuntar al decorador.
Esto hacer que cuando se decora una funcion, la
funcion decorada permanece siendo la funcion definida
y mantiene su identidad de funcion decorada. No es un
decorador como en el otro caso.

Mantiene su identidad de funcion no decorada.
Util si se necesita usar la funcion para otra cosa y no
queres usar el decorador

Se necesita importar wraps
'''


def decorador_1(param1, param2):
    def decorador_param(f):
        @wraps(f)
        def decorador_codigo():
            print("Parametros del decorador: {}, {}"
                  .format(param1, param2))
            print("Antes")
            f()
            print("Despues")
        return decorador_codigo
    return decorador_param


@decorador_1("param1", "param2")
def func_decorada_1():
    print("Durante")


def decorador_2(f):
    @wraps(f)
    def decorador_codigo():
        print("Antes")
        f()
        print("Despues")
    return decorador_codigo


@decorador_2
def func_decorada_2():
    print("Durante")


print("\n\nEl resultado final de toda esta clase con parametros:")
func_decorada_1()

print("\n\nEl resultado final de toda esta clase sin parametros:")
func_decorada_2()
