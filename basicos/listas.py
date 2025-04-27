#lista

# similar a los arrays en JS, se establecen con []
# elementos estan odrenados, son cambiables y admite repetidos
#tipos de datos admitidos: bool, numeros, strings

equipos = ["Ferrari", "Mercedes", "Red Bull", "Williams", "McLaren"]

print(equipos)
print(equipos[2]) 
print(equipos[1:])
print(equipos[:3]) #esta notacion siempre excluye el index escrito
print(equipos[1:3])
print(len(equipos)) #cantidad de elementos en la lista

#constructor de listas = list()

F2 = list(("MP", "Campos", "ART", "Prema", "Trident"))
print(F2)

#chequear si existe un elemento con un if
if "Ferrari" in equipos:
    print("mas vale")

#cambiar items en una lista
print(f"antes de cambiar: {equipos}")
equipos[2] = "Sauber"
print(equipos)
equipos[1:4] = ["Aston Martin", "Racing Bulls", "Haas"] #aplicable inverso tambien
print(equipos)

#cambiando con rangos los items deben coincidir. agregar mas items hara mover el resto
#ejemplo agregar [1:2] y dos items, agrega 2 items en index 1 y 2 y mueve el resto para atras
print(f"antes de cambiar: {equipos}")
equipos [1:2] = ["Alpine", "Cadillac"]
print(equipos)
#mismo caso al reves, agregar 1 item al rango [1:3] hara desaparecer el item en index 2
equipos[1:4] = ["Mercedes", "Red Bull"]
print(equipos)


#el metodo insert() funciona similar pero desplaza los items, no los reemplaza
equipos.insert(3,"Williams")
print(equipos)

#el metodo append() siempre agrega al final
equipos.append("Sauber")
print(equipos)

#el metodo extend() permite agregar otra lista o coleccion
equipos.extend(F2)
print(equipos)

#el metodo remove() permite remover un item especifico, si se repite, remueve solo el primero
#el metodo pop() hace lo mismo pero con indice. si no es especifica, remueve el ultimo item
#del tambien borra un indice puntual, o puede usarse para borrar toda la lista. no es metodo
#el metodo clear() vacia la lista

del equipos [7:]
print(equipos)
print("hasta aca fue manejo general")

#Comprension de listas
#es una manera abreviada de crear una lista con elementos de una existente
#"expresion" para "item" en "iterable" si cumple con "condicion"
equipos_con_a = [x for x in equipos if "a" in x]
print(equipos_con_a)

#la condicion puede omitirse y no llevaria IF
