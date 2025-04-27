#es el equivalente a los objetos de JS. Almacena caracteristicas por pares de clave-valor
#ordenados (desde 3.7), cambiables y no aceptan duplicados

#en caso de incorporar u nduplicado, lee el ultimo ingresado


#se escriben entre {}, acepta todo tipo de datos

#se puede referir a los items usando sus caracteristicas

miauto = {
    "marca": "Nissan",
    "modelo": "March",
    "año": 2019,
    "color": "gris"
}

print(miauto["modelo"])

#acepta listas como datos

otroauto = {
    "marca": "ford",
    "modelo": "fiesta",
    "turbo": False,
    "colores": ["negro", "blanco", "bordo"]
}

#su constructor es dict()

usuario = dict(nombre = "Facundo", apellido = "Castro", edad = 36)
print(usuario)

#se puede acceder a los items de dos formas, con [] o metodo get()

x = usuario["nombre"] 
y = usuario.get("apellido")
print(x,y)

#para obtener una lista de sus claves, existe el metodo keys()

z = miauto.keys()
print(z)

#para agregar un item nuevo al diccionario:

otroauto["combustible"] = "nafta"
print(otroauto)

#el metodo values() es similar a keys pero devuelve los valores

w = otroauto.values()
print(w)

#el metodo items() devuelve los pares como tuplas en una lista

v = miauto.items()
print(v)

#podemos usar in para determinar si una clave esta en el diccionario

if "color" in miauto:
    print("existe este item")

#para cambiar valoes podemos hacerlo con [] o con el metodo update(). estas dos maneras tambien permiten agregar items

otroauto["combustible"] = "diesel"
otroauto.update({"turbo": True})

print(otroauto)

#el metodo pop() permite eliminar un item segun su clave. el metodo popitem() remueve el ultimo item insertado

miauto.pop("color")
print(miauto)

#se puede usar del para borrar un item, o el diccionario por completo

del otroauto["combustible"]
print(otroauto)

# metodo clear() vacia el diccionario

#loop for itera por defecto sobre las claves del diccionario. hay metodos para iterar sobre los valores, o los items completos:

for x in miauto:
    print(x) #esto imprime las claves

for x in miauto:
    print(miauto[x]) #esto imprime los valores

#tambien se pueden usar los metodos

for x in miauto.keys():
    print(x)

for x in miauto.values():
    print(x)

#metodo items() devuelve los items completos

for x in otroauto.items():
    print(x)

#metodo copy() sirve para copiar el dic completo

auto_petri = otroauto.copy()

#tambien se puede hacer con el constructor dict()

auto_nadia = dict(otroauto)

#dicc anidados
#se puede agregar un dicc dentro de otro dicc

autos_familia = {
    "auto_facundo" : {
        "marca": "nissan",
        "modelo": "march",
        "año": 2019
    },
    "auto_nora":{
        "marca": "ford",
        "modelo": "ka",
        "año": 2016
    },
    "auto_reynaldo":{
        "marca": "renault",
        "modelo": "kangoo",
        "año": 2019
    }
}

#tambien pueden crearse los dicc por separado y agregarlos

auto_martin = {
    "marca": "volkswagen",
    "modelo": "gol g4"
}

auto_gus = {
    "marca": "volkswagen",
    "modelo": "gol g3"
}

auto_pablo = {
    "marca": "ford",
    "modelo": "ecosport"
}

autos_amigos = {
    "pablo" : auto_pablo,
    "martin" : auto_martin,
    "gus" : auto_gus
}

print(autos_amigos)


#para acceder a items de dicc anidados:

print(autos_amigos["martin"]["modelo"])

#para loopear en dicc anidados

for nombre, valor in autos_amigos.items():
    print(nombre)
    for clave in valor:
        print(clave + ":" + valor[clave])