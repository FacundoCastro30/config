#filtrar significa tomar elementos puntuales de un array y crear otro

#en numpy se filtra con una lista booleana, que es una lista aparte con booleanos con indices correspondientes a los elementos del array

#el nuevo array se va a conformar con lso valores que sean True
import numpy as np

a = np.array([1,2,3,4,5])
b = [True, False, True, False, True]

c = a[b]
print(c) #imprime los valores True de a, o sea los impares

#en el ejemplo anterior los bools estan hardcodeados, la gracia es que el filtro sea logico

d = np.array([1,2,3,4,5,6,7,8,9,10])
#se crea una lista vacia

filtro = []
#se crea la logica del filtro
for x in d:
    if x%2 == 0:
        filtro.append(True)
    else:
        filtro.append(False)

#se aplica al array original
d_filtrado = d[filtro]

print(filtro)
print(d_filtrado)

#tambien se puede hacer de esta manera:

e = np.array([1,2,3,4,5,6,7,8,9,10])
filtro2 = e%2 == 1 #filtrar por numeros impares

e_filtrado = e[filtro2]

print(filtro2)
print(e_filtrado)