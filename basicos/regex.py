# reg ex (regular expression) se usa para buscar si un string contiene un patron de busqueda

#se importa como modulo

import re

texto = "nos, los representantes del pueblo de la nacion Argentina"
x = re.search("^nos.*Argentina$", texto)

if x:
    print("existe")
else: 
    print("no existe")


y = re.search("^hola.*mundo$", texto)

if y:
    print("existe")
else: 
    print("no existe")

#findall() devuelve una lista con todos los matches en el orden que estan. si no hay, devuelve una lista vacia

z = re.findall("lo", texto)
print(z)

#search() busca si un elemento se encuentra en el string. devuelve un objeto match, o None si no existe. de haber varios match, devuelve el primero

a = re.search("Argentina", texto)
print(a.start()) #start() devuelve en que ubicacion se encentra

#split() corta el string en cada instancia
b = re.split("\s", texto) #"\s" significa espacios
print(b)

#maxsplit se usa como parametro posicional en ultimo lugar. se usa para determinar las instancias maximas del split
c = re.split("\s", texto, 2)
print(c)

#sub() reemplaza la ocurrencia con un texto a eleccion
u = re.sub("Argentina", "Uruguaya", texto)
print(u)

#el parametro count al final controla la cantidad de reemplazos

"""
u = re.sub("Argentina", "Uruguaya", texto, 5) si fuera el caso
print(u)
"""

#el objeto match devuelvo por search() contiene varrios metodos
#.span() devuelve una tupla con las posiciones de inicio y fin de lo buscado
#.string devuelve el string de la funcion
#.group() devuelve la parte del string donde hubo match

d = re.search("lo", texto)
print(d.string)

e = re.search("nacion", texto)
print(e.span())

f = re.search(r"\bA\w+", texto)  #busca palabras con A mayuscula, devuelve la palabra
print(f.group())

#referencias en w3s de todas las posibilidades de busqueda