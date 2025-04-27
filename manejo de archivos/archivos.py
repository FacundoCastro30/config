#open() es clave para trabajar con archivos

#toma dos parametros: nombre del archivo Namefile y modo Mode

#metodos/modos:
#"r" read, es default. solo abre para leer, genera error si el archivo no existe
#"a" append, abre el archivo para apendar (agregar al final). si no existe, lo crea
#"w" write, abre el archivo para escirbir. si no existe, lo crea
#"x" crear. crea el archivo, si ya existe genera error

#tambien se puede aclarar si es texto o binario con "t" o "b". (texto es default, binario pueden ser imagenes)

# f = open("demo.txt")
# f open("demo.txt", "rt") es igual, serian los valores por default

# a = open("prueba.txt", "x") crea el archivo prueba, ya se creo
# a = open("prueba.txt", "w") para escribir