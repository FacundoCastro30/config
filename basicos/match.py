#match es el switch de JS o c++
#recibe una condicion, la evalua, compara contra todos los case y ejecuta el correcto

#sintaxis:

"""
match expresion:
    case condicion:
        codigo
    case condicion:
        codigo
    ...    
"""

dia = 2

match dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3: 
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")    


#se puede poner un _ para caso por default que no cumpla las condiciones

match dia: 
    case 6:
        print("sabado")
    case 7:
        print("domingo")
    case _:
        print("dia de semana")

#se puede usara | como operador para juntar carios cases

match dia:
    case 1|2|3|4|5:
        print("dia habil ")
    case 6|7:
        print("finde ")

#los cases pueden incluir ifs
mes = 4

match dia:
    case 1|2|3|4|5 if mes == 4:
        print("dia habil de abril")
    case 6|7:
        print("finde ")