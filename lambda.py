#las funciones lambda son funciones anonimas. pueden tener cualquier cantidad de parametros pero solo una expresion

##la sintaxis es lambda argumentos : expresion

x = lambda a : a + 3
print(x(12))

#lambda con varios argumentos

y = lambda a, b : a * b
print(y(7,4))

#la gracia de las funcoines Lambda es usarlas dentro de otras funciones

def funcion(n):
    return lambda a: a*n

#de esta manera se puede reusar en varios casos

duplicador = funcion(2)
triplicador = funcion(3)

print(duplicador(5))
print(triplicador(5))