#reformar implica cambiar el numero de elementos o dimensiones

import numpy as np

#de 1d a 2d
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
b = a.reshape(4,3) #4 arrays, 3 elementos cada uno

print(b)

#de 1d a 3d
c = a.reshape(2, 3, 2)
print(c) #2 dimensiones con 3 arrays con 2 elementos cada uno

#se puede reshapear cualquie cantidad de elementos y dimensiones siempre que queden "parejos", que en la reforma no falte ni sobre ningun elemento

d = np.array([1,2,3,4,5,6,7,8])
#e = d.reshape(3,3) da error porque tengo 8 elementos repartidos en 9

#reshape retorna un view, o sea que si se altera elelemento creado tambien se altera el original

#se puede tener una "dimension desconocida", en caso de no saber cuantos elementos compoen el original, se puede poner un unico -1 y numpy formula automaticamente
e = d.reshape(2, 2, -1)
print(e)

#aplanar arrays: pasar de multiples dimensiones a 1d:

f = np.array([[1,2,3],[4,5,6]])
g = f.reshape(-1)
print(g)