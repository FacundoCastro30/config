#sort() se usa para ordenar una secuencia, alfabetica o numericamente, ascendiente o descendientemente

import numpy as np

a = np.array([3,7,2,1,0,5,4,6])
print(np.sort(a))

#esto devuelve una copia del array, el original se mantiene intacto

#alfabetico:

b = np.array(["banana", "damasco", "ciruela", "anana"])
print(np.sort(b))

#booleano

c = np.array([False, True, True, False, False, True])
print(np.sort(c))

#en 2d, ordena los scalars

d = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(d))