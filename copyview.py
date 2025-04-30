import numpy as np

#copy() permite crear un array nuevo a base de otro, mientras que view() permite "reflejar" otro array. Copy posee datos propios, view solo muestra los del array original

#por ende, modificar un array de copy no altera el original ni viceversa, pero uno en view si lo hace

a = np.array([1,2,3,4,5])
b = a.copy()
c = a.view()
a[1] = 6

print(a)
print(b)
print(c)

#los cambios en el view son bidireccionales, cambios en el reflejo se aplican al original tambien

d = np.array(["a", "b", "c"])
e = d.view()

e[0] = "z"

print(d)
print(e)

#para saber si un array posee o no sus datos, se usa base

print(b.base) #un array hecho con copy devuelve None, sus datos son propios
print(c.base)