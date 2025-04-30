#numpy maneja mas tipos de datos que los default de python (str, int, float, bool, complex). los identifica con una sola letra

import numpy as np

#los tipos son
"""
i = integer
b = booleano
u = integer sin firmar (?)
f = float
c = complejo float
m = timedelta
M = datetime
O = objeto
S = string
U = string unicode
V = espacio reservado de memoria para otros tipos (void)
"""

#con el metodo dtype podemos ver el tipo de elementos de un array

a = np.array([1,2,3,4,5])
b = np.array(["Facundo", "Lucia", "Mila"])

print(a.dtype)
print(b.dtype)

#al crear arrays se le peude definir el tipo de datos a incluir

c = np.array([1,2,3,4], dtype = 'S') 
print(c.dtype)

#se puede definir el tamaño de i, u, f, S, U

d = np.array([1,2,3,4], dtype='i4')
print(d)
print(d.dtype)

#si son datos que no se pueden convertir, np eleva un ValueError

#con el metodo astype() podemos cambiar el tipo de datos del array

e = np.array([1.2, 2.3, 3.4])
f = e.astype('i')

print(f)
print(f.dtype)

g = np.array([1,0,4])
h = g.astype(bool)

print(h)
print(h.dtype)