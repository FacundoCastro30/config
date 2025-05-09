#significa unir el contenido de mltiples arrays en uno solo

#generalidad: los ejes son como en un cartesiano. 0 es x (horizontal), 1 es y (vertical)

#w3 aclara qeu en SQL se unen tablas basadas en claves, mientras que aca se unen por ejes, investigar

#se escribe concatenate() mas la secuencia de arrays que queremos unir junto con el eje. si no existe, se considera 0

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.concatenate((a, b))
print(c)

#unir dos 2d en filas

d = np.array([[1, 2], [3, 4]])
e = np.array([[5, 6], [7, 8]])

f = np.concatenate((d,e), axis = 1)
print(f)

#Stack es lo mismo que concatenate, pero sobre un nuevo eje. se pueden stackear 2 1D y resulta en encimarlos. si no se pasa el eje explicitamente se interpreta 0

g = np.array([1,2,3])
h = np.array([4,5,6])
i = np.stack((g, h), axis = 0)
j = np.stack((g, h), axis = 1)

print(i)
print(j)

#hstack y vstack nos permiten apilar de dos maneras distintas, en filas o columnas

k = np.array([1,2,3])
l = np.array([4,5,6])

m = np.hstack((k, l)) #une los arrays como fila
n = np.vstack((k, l)) #une los arrays como columna

print(m)
print(n)

#dstack apila los arrays segun profundidad

o = np.array([1,2,3])
p = np.array([4,5,6])

q = np.dstack((o, p))
print(q)

