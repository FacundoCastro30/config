import numpy as np

#for sirve como siempre, pero itera solo por dimension. para acceder a los scalars, debemos repetir el bucle tantas veces como dimensiones haya

a = np.array([1,2,3,4,5])

for x in a:
    print(x)

b = np.array([[1,2,3],[4,5,6]])

for x in b:
    for y in x:
        print(y)

c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in c:
    for y in x:
        for z in y: 
            print(z)

#iterar sobre una dimension menos devuelve el array

#con la funcion nditer() podemos acceder directamente a los scalars sin tener qeu escribir dimension por dimension
print("con nditer")
for x in np.nditer(c):
    print(x)

#iterar con distintos tipos de datos: se puede usar el argunemto op_dtypes y pasarle el tipo de dato esperado mientras itera
#como numpy no ejecuta el cambio en el momento, necesita un espacio extra (buffer) para hacerlo. para habilitarlo hay que pasarle el parametro flags=['buffered']

d = np.array([1,2,3])
for x in np.nditer(d, flags=['buffered'], op_dtypes=['S']):
    print(x) 

#con nditer tambien podemos cambiar el step de la iteracion
print("array e" )
e = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(e[:, ::2]): #printear cada dos numeros
    print(x) 

#ndenumerate permite tambien acceder al indice de un elemento

#1d:
f = np.array([1,2,3,4,5])
for idx, x in np.ndenumerate(f):
    print(idx, x)

#2d:

g = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(g):
    print(idx, x)