#sets

#se define entre {}, sus datos son desordenados, inmutables y no tienen indice. no aceptan duplicados
#sus items no se pueden modificar, pero si agregar o eliminar

#acepta el metodo len () para determinar cantidad de elementos

#su constructor es set()

#los sets no se pueden modificar pero se pueden agregar items mediante add() para individuales o update()
#con update se puede agregar cualquier iterable (incluso otros tipos de colecciones)

circuitos = {"Monza", "Spa", "Suzuka", "Imola"}
pistas = {"RBRing", "Albert Park"}
callejeros = ["Monaco", "Singapur"]

circuitos.add("Barcelona")
print(circuitos)
circuitos.update(pistas, callejeros)
print(circuitos)

#borrar items, metodos remove(), discard(), pop(), clear()
#pop() al no tener indexado, borra un elemento al azar. remove y duscard funcionan igual, borran el parametro

#la diferencia es qe si el elemento no existe, remove da error y discard no

#uniones de sets

#union() une todos los elementos de dos sets

a = {1, 2, 3}
b = {4, 5, 6}

c = a.union(b)
print(c)

#tambien se puede simplificar con el simbolo | pero limita solo a sets

d = a|b
print(d)

#union() tambien acepta el agregado de varios iterables por vez, incluso otro tipos de colecciones

e = a.union(b, c, d)
print(f"e: {e}")

#tambien valido con |
# ejemplo1 = 2|4|5|6

#update() agrega items a un set existente, sin crear uno nuevo
#intersection() solo suma los items repetidos. simplificado con el signo & pero limita solo a sets

set1 = {"hola", "mundo"}
set2 = {"mundo", "extraño"}

set3 = set1.intersection(set2) #set3 = set1 & set2 
print(set3)

#intersection_update hace lo mismo pero sobre un set existente sin crear otro

#difference() devuelve un set nuevo con los items del primer set que no aparezcan en el segundo
#simplificado con el signo - pero limita solo a sets
#difference_update() es lo mismo pero sobre un set existente


#symmetric_difference() crea un set nuevo con elementos no repetidos
#simplificado con ^ pero limita solo a sets
#symmetric_difference_update() funciona igual pero sin crear un set nuevo, modifica uno existente
