#es lo contrario a join, corta un array en multiples

#se hace con array_split(). argumentos: el array y la cantidad de splits

import numpy as np

a = np.array([1,2,3,4,5,6])
b = np.array_split(a, 3)

print(b)

#en caso que el array no quede parejo, se ajusta automaticamente

c = np.array([1,2,3,4,5,6])
d = np.array_split(c, 4)

print(d) #quedan 2 splits con 2 scalars y 2 con 1

#en este caso, tambien se puede usar split() pero fallaria. con array_split() funciona

#este metodo devuelve arrays que pueden seraccedidos y trabajados con indexes

e = np.array([1,2,3,4,5,6])
f = np.array_split(e, 3)

print(f[0])
print(f[1])
print(f[2])

#misma sintaxis para un 2d

g = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
h = np.array_split(g, 3)

print(f"h: {h}")

#otro ejemplo donde cada elemento del 2d tiene 3 scalars

i = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

j = np.array_split(i, 3)

print(f"j: {j}")

#tambien se puede aclarar en que eje se quiere splitear

k = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
l = np.array_split(k, 3, axis=1)

print(f"l: {l}") #devuelve 3 arrays, donde cada scalar se toma segun su orden en cada elemento(primero, segundo, tercero del elemento)

#hsplit se usa como opuesto a hstack, lo mismo con vsplit y dsplit

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
n = np.hsplit(m, 3) #corta similar a axis = 1

print(f"n: {n}")

o = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
p = np.vsplit(o, 3) #corta "normal"

print(f"p: {p}") 

q = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
r = np.dsplit(q, 3)

print(f"r: {r}") 