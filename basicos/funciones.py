#son bloques de codigo que se ejecutan solo cuando se los llama

#se les puede pasar datos, conocidos como parametros

#pueden devolver data como resultado

#se crean con la palabra reservada def

#creacion
def mi_funcion():
    print("hola mundo desde una funcion")

#llamado
mi_funcion()

#los argumentos son informacion que se le puede pasar a la funcion. se especifican dentro de parentesis. pueden ser cualquier cantidad separados con ,

def saludo (nombre):
    print("hola " + nombre)

saludo("Facundo")
saludo("Lucia")

#la funcion siempre espera recibir la misma cantidad de argumentos que parametros definidos. si no coinciden, se usa un * antes del parametro, sino genera error

#al usar *, los argunemtos se reciben como tupla. y se los llama argumentos arbitrarios o *args en documentaciones

def mis_autos(*auto):
    print("mi auto actual es " + auto[1])

mis_autos("gol", "march", "golf", "uno")

#se pueden pasar argumentos como palabra clave. a estos se los llama kwargs en las documentaciones

def ninios(ninio1, ninio2, ninio3):
    print("mi sobrina es " + ninio3)

ninios(ninio1 = "Lucio", ninio2 ="Mauro", ninio3= "Pia")

#tambien existen argumentos arbitrarios con palabra clave. en este caso, el parametro lleva dos asteriscos antes, y la funcion recibe un diccionario de argumentos y se trabaja acorde

def yo(**persona):
    print("mi apellido es " + persona["apellido"])

yo(nombre = "Facundo", apellido = "Castro")

#para usar un parametro por default:

def pedimos_helado (sabor="chocolate"):
    print("pedime de " + sabor)

pedimos_helado("Dulce de leche")
pedimos_helado()
pedimos_helado("tramontana")

#a las funcoines se les puede pasar cualquier tipo de dato com oparametro, y mantiene sus caracteristicas al usarse

def comida(dulce):
    for x in postres:
        print(x)

postres = ["helado", "lemon pie", "alfajor"]

comida(postres) #en este caso, va le nombre de la lista, no del argumento

#return se usa cuando la funcion tiene que devolver un valor

def multip(x):
    return 3* x

#hasta aca no imprime nada en este caso, pero se creo un valor

print(multip(15))
print(multip(20))
print(multip(33))

#pass se usa como en bucles, si una funcion esta vacia, para evitar error

def vacia():
    pass

#para usar SOLO argumentos posicionales se agrega ,/ despues de los argumentos. en este caso no se pueden usar kwargs

def posi (x,/):
    print(x)

posi(3)
#posi(x = 3) generaria error

#y al reves, para usar SOLO kwargs, se usa *, antes de los argumentos

def argu(*, x):
    print(x)

argu(x = 2)
#argu(2) generaria error 

#combinacion: cualquier argumento ANTES de /, es posicional, y cualquier argumento DESPUES de *, es kwarg

def combo(a, b, /, c, *, d, e):
    print(a+b+c+d+e)

combo("hola ", "como estas? ", "yo bien ", d = "me alegro ", e = "chau")

#funciones recursivas
#son las que se llaman a si mismas en su ejecucion. hay que tener cuidado de que no se ejecuten en infinito

#ejemplo de w3s

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

"""
se lee: 
result es 6 mas ejecutar para 6 -1
o sea, result es 5 mas ejecutar para 5-1
o sea...

cuando k = 0, salta al else, returnea result como 0, y como estamos en nivel de 1 + k-1, muestra 1

y asi sigue "trepando" para volver a 6 en este caso
"""