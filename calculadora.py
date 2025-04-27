x = 0
y = 0
def sumar (x, y):
    return print(f"su resutado es: {x+y}")

def calcu():
    x = int(input("ingrese un numero: "))
    y = int(input(f"su numero es {x}, ingrese otro numero: "))
    sumar(x, y)
    z = str(input("enter para continuar, salir para cerrar el programa: "))
    if z != "salir":
        calcu()
    else:
        print("gracias por urilizar la calculadora!")

calcu()