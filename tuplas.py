#las tuplas van entre ()

#es ordenada y no cambiable (no acepta agregar o eliminar elementos). acepta duplicados. acepta todos los tipos de datos, incluso mezclados

pilotos = ("Verstappen", "Tsunoda", "Leclerc", "Hamilton", "Leclerc")

#para crear una tupla con un solo elemento, hay que agregarle una coma (sino cuenta como string)

tupla = ("elemento",)

#se pueden construir con el constructor tuple()

construida = tuple(("1", "2", "3")) #de esta manera necesita doble parentesis

#al ser inmutable no acepta cambios por medio de metodos. para hacerlo, hay que transformarla en lista, mutarla y volverla a transformar en tupla

mutar_tupla = list(construida)
mutar_tupla.append(4)
tupla_mutada = tuple(mutar_tupla)
print(tupla_mutada)

#unpacking de una tupla

#podemos tomar los items de una tupla y crear variables. a esto se le llama unpacking

frutas = ("manzana", "mandarina", "banana")
(roja, naranja, amarilla) = frutas

print(roja)
print(naranja)
print(amarilla)

#si no coincide el numero de items con el de variables, se puede poner un * a la variable para asignar como lista al resto

verduras = ("tomate", "zanahoria", "acelga", "espinaca", "lechuga")
(rojo, anaranjado, *verde) = verduras

print(rojo)
print(anaranjado)
print(verde)

#si el * se usa en una variable que no sea la ultima, los elementos se acomodan de manera que coincidan con los restantes

#se pueden loopear las tuplas con for o while. se puede utilizar i=0 y len() si no se sabe el numero de items

#las tuplas se pueden unir o multiplicar con los operadores + o *
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

tupla3 = tupla1 + tupla2
tupla4 = tupla3*2
print(tupla3)
print(tupla4)

#el metodo count() devuelve cuantas veces se encuentra un item en la tupla

contar = tupla4.count(6)
print(contar)

#el metodo index() muestra el index de un elemento. de repetirse, muestra el primero

indice = pilotos.index("Leclerc")
print(indice)