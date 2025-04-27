#try permite probar un codigo para ver si genera errores, except los maneja

#else ejecuta un bloque cuando no hay error, y finally ejecuta un bloque sin importar si hay error o no

#una excepcion es un error. cuando ocurre, python deja deejecutarse y muestra el error. las excepciones se pueden manejar usando try

try:
    print(x)
except:
    print("ocurrio un error")

#en este caso se ejecuta el except porque x no esta definida

#tambien úeden existir varios bloques de exception

try:
    print(y)
except NameError:
    print("la variable no existe")
except:
    print("error desconocido")    

#en w3s hay una lista de excepciones para aplicar segun el caso

#con else se puedeejecutar un codigo cuando no hay error

try:
    print("hola mundo")
except:
    print("hubo un error")
else: 
    print("la ejecucion fue correcta")

#el bloque finally se ejecutar haya error o no

try:
    print(z)
except NameError:
    print("z no existe")
finally:
    print("la ejecucion termino")

#aca en w3s hay un ejemplo de creacion/escritura de archivos, dejo marcado para mas adelante

#tambien se pueden generar una excepcion en determinadas condiciones con el comando raise

a = -1

if a < 0:
    raise Exception ("no se admiten numeros negativos")

#despeus de definido el error se puede printear al usuario

b = "hola"

if not type(b) in int:
    raise TypeError("solo se admiten integers")  

#TypeError tambien esta en la lista