"""
Reglas generales de las funciones:
1- no se ejecuta la funcion a menos que la llames
2- la puedo llamar la cantidad de veces que quiera
3- primero hay que definir la funcion, y despues llamarla
4- primero van los parametros requeridos, y al final los opcionales
5- para cambiar el scope de una variable, utilizar return
"""


#FUNCIONES SIN PARAMETROS
"""
def miFuncion():
    #conjunto de instrucciones
"""

def derechos_humanos():
    print("Derecho a la vida")
    print("Derecho a la igualdad ante la ley")
    print("Derecho a la libertad")

derechos_humanos()

def derechos_mayorDeEdad():
    print("Derecho a votar")
    print("Derecho al trabajo")


# FUNCIONES CON PARAMETROS
"""
def miFuncion2(parametro1,parametro2):
    #conjunto de instrucciones
"""
def mayoria_de_edad(nombre,edad):
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()




#FUNCIONES CON PARAMETROS OPCIONALES
"""
def miFuncion3(parametro1,parametro2=valorpordefecto):
    #conjunto de instrucciones
"""
def mayoria_de_edad2(edad,nombre='DESCONOCIDO'):
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()

mayoria_de_edad2(15,'Pepito')