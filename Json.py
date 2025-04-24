# python tiene metodos para traducir a y de json

#hay que importar el modulo json
import json
#de json a python = json.loads()
#devuelve un dicccionario

x = '{"nombre":"Facundo", "edad": 36, "ciudad": "Haedo"}'

y = json.loads(x)
print(y["edad"])

#traducir de python a json = json.dumps() 

persona = { 
    "nombre": "Lucia",
    "edad": None,
    "ciudad": "Haedo"
}

persojson = json.dumps(persona)
print(persojson)

#se pueden traducir todas las colecciones menos los sets, int, floats, strings, booleanos y el valor None

#ejemplo

print(json.dumps({"name": "John", "age": 30})) #traduce a objeto
print(json.dumps(["apple", "bananas"])) #traduce a array
print(json.dumps(("apple", "bananas"))) #array
print(json.dumps("hello"))  #string
print(json.dumps(42))   #numero
print(json.dumps(31.76)) #numero
print(json.dumps(True)) #true
print(json.dumps(False)) #false
print(json.dumps(None)) #null

#dumps tambien puedo usar su parametros para darle formato mas legible y para ordenar el resultado

j = {
    "nombre": "Jonathan",
    "apellido": "Petrini",
    "edad": 36,
    "mascotas": None,
    "hijos": "Vera",
    "vehiculos": [
        {"marca": "ford", "modelo": "fiesta"}
    ]
}

jj = json.dumps(j, indent = 4, separators= (" . ", " = "), sort_keys=True)
#indent da la sangria, separators los separadores, sort acomoda las claves por orden alfabetico

print(jj)