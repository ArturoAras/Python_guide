#Python posee tres tipos de operadores: los matemáticos, los de comparación y los lógicos

#Al igual que en las matemáticas, en Python se pueden utilizar operadores matemáticos para trabajar con los datos de tipo numérico
a = 9
b = 5
print("------------------------TRABAJO CON OPERADORES------------------------")
print("Operamos con los números 9 y 5")

print("------------------------EMPIEZA EL FLUJO DE EJECUCIÓN------------------------")
print("------------------OPERADORES ARITMÉTICOS------------------")
print("Suma:",a + b) #El operador + suma las variables
print("Resta:",a - b) #El operador - resta las variables
print("Multiplicación:",a * b) #El operador * multiplica las variables
print("División:",a / b) #El operador / de división devuelve siempre un dato flotante
print("Exponente:",a ** b) #El operador ** eleva un número por otro
print("Módulo:",a % b) #El operador de módulo devuelve el resto de una división entera
print("División baja:",a // b) #El operador de división baja devuelve el resultado de la división pero siempre elimina todos los decimales


################################################################################################################################################


#Los operadores de comparación también son utilizados en matemática básica y sirven para comparar dos o más datos y obtener un resultado booleano
print("------------------------OPERADORES DE COMPARACIÓN------------------------")
print("¿Es 9 mayor que 5?", a > b) #Operador "mayor que", en este caso devuelve TRUE
print("¿Es 9 menor que 5?",a < b) #Operador "menor que", en este caso devuelve FALSE
print("¿Es 9 mayor o igual que 5?",a >= b) #Operador "mayor o igual que", en este caso devuelve TRUE
print("¿Es 9 menor o igual que 5?",a <= b) #Operador "menor o igual que", en este caso devuelve FALSE
print("¿Es 9 igual que 5?",a == b) #Operador "igual que", en este caso devuelve FALSE
print("¿Es 9 distinto que 5?",a != b) #Operador "distinto que", en este caso devuelve TRUE


################################################################################################################################################


#En Python también existen operadores que le asignan un valor a una variable
print("---------------------------OPERADORES DE ASIGNACIÓN---------------------------")
print("a = 9 |", a)
print("b = 5 |", b)
a += b # Suma el valor de B a A y lo guarda en A
print("a += b |", a)
a  = 9 #Devolvemos el valor original a A, ya que en la línea 39 se convirtió en 14
a -= b #Resta el valor de B a A y lo guarda en A
print("a -= b", a)

#####################
print("Todos los operadores aritméticos pueden ir seguidos con un signo \"=\" para convertirlos en operadores de asignación, así realizarán la operación matemática correspondiente y sobreescribirán el resultado en la variable")
#####################


################################################################################################################################################


#El último grupo de operadores se llaman operadores lógicos y se utilizan para evaluar condiciones booleanas entre si
print("------------------------OPERADOR AND------------------------")
print(True and True) #El operador AND devolverá True siempre y cuando ambas condiciones sean True
print(True and False) #Ejemplo 2
print(False and True) #Ejemplo 3
print(False and False) #Ejemplo 4
print("------------------------OPERADOR OR------------------------")
print(True or True) #El operador OR devuelve True siempre y cuando al menos una de sus condiciones sea True
print(True or False) #Ejemplo 2
print(False or True) #Ejemplo 3
print(False or False) #Ejemplo 4
print("------------------------OPERADOR NOT------------------------")
print(not True) #El operador NOT devuelve el resultado contrario a la condición evaluada
print(not False) #Ejemplo 1
print( not (True and False)) #Ejemplo 2
print(not (False or True)) #Ejemplo 3


"""
Hay que tener en cuenta que todos los operadores funcionan con un orden de prioridad igual al de las matemáticas tradicionales, por lo tanto operadores como la división,
la multiplicación, el módulo, etc; tendrán prioridad por sobre operadores como la suma o resta.
"""