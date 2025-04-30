#el indexado de los arrays es igual que el general

import numpy as np

a = np.array([1,2,3,4,5])
print(a[0])
print(a[2:5])
print(a[:3])
print(a[1:])

#para mas dimensiones, se va a usar numeros separados por comas, indicando array por array a acceder

#2d:
b = np.array([[1, 2, 3],[4, 5, 6]])
print(b[0,2]) #deberia dar 3

#3d:
c = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,7]]])
print(c[0,1,2]) #deberia dar 6

#tambien se puede usar indexado negativo
print(b[1,-1]) #deberia dar 6