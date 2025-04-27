#Generalidades de colecciones

#listas, tuplas, sets y diccionarios

#sintaxis de los metodos -> nombre.metodo(argumentos)
#lista.remove(2)

#index arranca siempre con 0
#al acceder con -1 por ejemplo, toma el anteultimo elemento
#rangos se definen con []. pueden ser indice unico o rango separado con :

# la ausencia de un indice da a entender que el inicio o final son el correspondiente de la coleccion
# [:4] accederia desde el principio al 5to elemento, [4:] accederia desde el 5to hasta el final
# rangos con final definidi nunca incluyen el index escrito. ejemplo [1:4] seria del segundo al cuarto elemento
# tambien aplica a rangos desde el final [-4:-1]

#las colecciones son iterables con bucles for y while

#metodo len() se aplica a listas, tuplas, sets, diccionarios
#indica cuantos elementos tiene la coleccion

#aceptan todos tipos de datos. considerar que True y 1 los toma como equivalentes o repetidos. mismo para False y 0

#clear() vacia la coleccion. del la borra del todo

#type() arroja: 
#class list para lista, tuple para tupla, set para set, y dict para diccionario