import numpy as np

#las dimensiones hacen mencion de la "profundidad" de los arrays anidados. se expresan con numeros y una D para referenciar

#0-D es un array con un elemento simple, tambien se llaman Scalars

a = np.array(15) #notese la ausencia de corchetes

#1-D es un array con varios Scalars. tambien se llaman unidimensionals. son lso arrays mas comunes

b = np.array([1, 2, 3])

#2-D es un array que contiene varios arrays. se suelen usar para representar matrices o tensores de 2do orden ->investigar

c = np.array([[1, 2, 3],[4, 5, 6]])

#3-D es un array que contiene arrays 2-D (matrices). representan tensores de 3er orden

d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

#para saber la cantidad de dimensiones de un array podemos usar ndim:
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
#nos devuelve un int con el numero de dimensiones del array

#los arrays pueden tener cualquier numero de dimensiones. se puede configurar al crearlos con el metodo ndmin

e = np.array(["a", "b", "c"], ndmin=5)
print(e)
print("dimensiones del array: ", e.ndim)

#boluregla: las dimensiones son la cantidad de corchetes