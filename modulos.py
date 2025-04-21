#son el equivalente a las librerias y su importacion. son archivos con funciones o datos que queramos utilizar


#sintaxis de importacion:
import libreria

#sintaxis de ejecucion:
libreria.saludo("Facundo") #nombre del modulo.funcion a usar

#un modulo tambien puede prestar objetos, variables, colecciones, etc...

x = libreria.auto["modelo"]
print(x)

#se le pueden dar alias a los modulos con la palabra clave as

import modulo2 as lib2 

lib2.saludo() #a l llamar, hay que usar el alias


#hay varios modulos pre establecidos:
 
import platform #platform recolecta datos de la maquina 

q = platform.system()
print(f"tu sistema es {q}")

#el modulo dir() da una lista de las funciones o variables de un modulo

w = dir(platform)
print(w)

#esto es curiosidad nomas
e = platform.processor()
print(e)

#se pueden importar partes seleccionadas de un modulo, con la palabra clave from

from modulo2 import persona #sintaxis: from MODULO import LO QUE NECESITES TRAER
print(persona["edad"])

#al usar from no hay que referir al objeto traido como modulo.objeto