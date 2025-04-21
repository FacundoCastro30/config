#python tiene funciones incorporadas para matematica

#max() y min() devuelven los respectivos dentro de un iterable


milista = (10, 15, 20)
x = max(milista)
y = min(milista)

print(x, y)

#abs() devuelve el valor absoluto de un numero

j = abs(-3.14)

print(j)

#pow(x, y)devuelve la potencia

w = pow(3, 4)
print(w)

#el modulo math trae mas funciones y constantes

import math

#ejemplos
#sqrt() es raiz cuadrada
e = math.sqrt(64)
print(e)

#ceil() y floor() redondean para arriba y abajo respectivamente

midec = 3.14
r=math.ceil(midec)
t=math.floor(midec)

print(r, t)

#podemos traer el numero pi

pi = math.pi
print(pi)

#la lista completa del modulo esta en w3s