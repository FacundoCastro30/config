#se puede buscar dentro de un array con where(). devuelve el indice de la coincidencia

import numpy as np

a = np.array([1,2,3,4,5,4,4,3,4])
b = np.where(a == 4)
print(b) #devuelve una tupla con los indices coincidentes, en este caso (array([3, 5, 6, 8]),)

#permite operaciones o logica

c = np.array([1, 2, 3, 4, 5, 6, 7, 8])
d = np.where(c%2 == 0) #busca numeros pares
e = np.where(c%2 == 1) #busca numeros impares

print(d)
print(e)

#searchsorted() hace una busqueda binaria en el array y devuelve un indice donde el valor especificado deberia insertarse para que el array permanezca ordenado

f = np.array([4,5,6,8,9])
g = np.searchsorted(f, 7)
print(g) #deberia devolver 3, donde eso es el indice qeu al insertar 7 se mantiene ordenado

h = np.array([4,5,6,7,8,9])
i = np.searchsorted(h, 10)

print(i) #misma logica, deberia ser 6

j = np.array([4,5,6,8,9])
k = np.searchsorted(j, 3)

print(k) #deberia ser 0

#searchsorted debe usarse en arrays ordenados
#tambien se le puede pasar side='right' como parametro, y busca desde atras 

l = np.array([4,5,6,8,9])
m = np.searchsorted(l, 7, side = 'right') #deberia dar 3
print(m)

#tambien admite varios valores

n = np.array([1, 3, 5, 7])
o = np.searchsorted(n, [2, 4, 6])

print(o) #devuelve un array con los indices deonde, ordenadamente, deben insertarse los elementos