#slice permite "cortar" elementos de un array. se usa con las reglas generales de indexacion mas un int extra que se denomina STEP, o paso
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a[2:9:3]) #desde el index 2 hasta el index 9 saltando de a 3 numeros

#mismas reglas para indices negativos

#para mas dimensiones:
b = np.array([[1, 2, 3, "a", "b", "c"],[4, 5, 6, "d", "e", "f"]])
print(b[0:2, 2]) #tercer elemento de cada array
print(b[0:2, 1:4]) #ambos elementos, index 1 inclusive a 4 exclusive
print(b[0,-1]) #ultimo del primer elemento
