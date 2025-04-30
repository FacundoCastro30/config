#es una libreria que se usa para trabajar con arrays. los arrays son mas rapidos de trabajar que las listas

#se instala con pip (pip install numpy) y se importa como otro modulo

import numpy as np #as np significa como alias. tipicamente numpy es np
print(np.__version__)

#ejemplo de creacion de array con la funcio n array()

arr = np.array([1, 2, 3, 4, 5])
print(arr)

#el tipo de objeto creado con numpy nos da ndarray
print(type(arr))

#numpy puede convertir en array una lista, tupla o cualquier objeto simil lista
arr2=np.array(("a", "b", "c"))
print(arr2)
print(type(arr2))

