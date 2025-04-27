#para borrar archivos, hay que importar os

import os

#y usar os.remove

# os.remove("borrable.txt") -> esto se suele envolver en un if para ver primero si el archivo existe

if os.path.exists("borrable.txt"):
    os.remove("borrable.txt")
else:
    print("el archivo no existe")

#tambien se pueden borrar carpetas con os.rmdir()
# os.rmdir("bolucarpeta")

#solo borra carpetas vacias, primero habria que vaciarlas de sus archivos

#ejecute esto dos veces, el archivo ya no existe