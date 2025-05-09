#numpy incorpora shape, que devuelve una tupla donde lso indices representan la cantidad de dimensiones y sus elementos

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a.shape)
#las dimensiones tienen que ser homogeneas en sus elementos

b = np.array([1, 2, 3, 4], ndmin=5)
print(b.shape)

#en este caso, se entiende que cada int representa una dimension, donde la ultima posee 4 elementos
