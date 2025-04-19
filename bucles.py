#while

#ejecuta una orden mientras se cumpla una condicion

#debe incluir una condicion con incremento, sino se ejecuta eternamente (y tilda el programa)

i = 0

while i < 6:
    print(i)
    i+=1

#el comendo break corta la ejecucion incluso si se cumple la condicion

j = 0

while j < 6:
    print(j)
    if j == 4:
        break
    j += 1


#el comando continue "altea" una ejecucion

k = 0
while k < 6:
    k+=1
    if k == 3:
        continue
    print(k)

#en este caso es importante repasar el orden para evitar ejecucion infinita

#el comando else se usa para ejecutar un codigo cuando la condicion deje de cumplirse

l = 0
while l < 6:
    print(l)
    l+=1
else:
    print("L ya no es menor que 6")


#for

#se usa para iterar sobre una secuencia, sea coleccion o string

autos = ["Fiat Uno", "Nissan March", "Volkswagen Golf"]

for x in autos:
    print(x)

#caso de strings

for x in "Facundo":
    print(x)

#break se usa par acortar la secuencia

for x in "Facundo":
    print(x)
    if x == "u":
        break

#atencion al orden de ejecucion respecto de x para ver donde cortar

#continue tambien sirve para saltar una ejecucion

for x in "Lucia":
    if x == "c":
        continue
    print(x)

#con range() podemos ejecutar un numero definido de veces. tener en cuenta que no incluye el numero escrito. range() arranca en 0 e incrementea de a 1 por default

for x in range(11):
    print(x)

#se le puede especificar el numero de inicio al range dentro del parentesis, separado con una , del final

for x in range(4,15):
    print (x)

#tambien, se puede cambiar el incremento, tambien agregandolo con , al final del parentesis

for x in range (0, 12, 2):
    print(x)

#comando else como en while, se ejecuta cuando la condicion ya no se cumple

for x in range(5):
    print(x)
else:
    print("termino")

#el bloque else no se ejecuta si se hace un break antes

for x in range(6):
    if x ==3: break #la ejecucion termina aca
    print(x)
else:
    print("se termino")

#for anidados
#en este caso, se ejecuta de adentro hacia afuera

piso = ["primero", "segundo", "tercero", "cuarto"]

deptos = ["a", "b", "c", "d", "e", "f"]

#mi edificio
for x in piso:
    for y in deptos:
        print(x, y)
        if x == "cuarto" and y == "d":
            break

#si el bucle for esta vacio, se usa el comando pass para que no genere error

for x in [0, 1, 2]:
  pass