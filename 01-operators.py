#Python posee tres tipos de operadores: los matemáticos, los de comparación y los lógicos

#Al igual que en las matemáticas, en Python se pueden utilizar operadores matemáticos para trabajar con los datos de tipo numérico
a = 9
b = 5

print("------------------------ACÁ EMPIEZA EL FLUJO DE EJECUCIÓN------------------------")
print(a + b) #El operador + suma las variables
print(a - b) #El operador - resta las variables
print(a * b) #El operador * multiplica las variables
print(a / b) #El operador / divide la primera variable por la segunda
print(a ** b) #El operador ** eleva un número por otro
print(a % b) #El operador de módulo devuelve el resto de una división entera
print(a // b) #El operador de división baja devuelve el resultado de la división pero siempre elimina todos los decimales


################################################################################################################################################


#Los operadores de comparación también son utilizados en matemática básica y sirven para comparar dos o más datos y obtener un resultado booleano
print("------------------------OPERADORES DE COMPARACIÓN------------------------")
print(a > b) #Operador "mayor que", en este caso devuelve TRUE
print(a < b) #Operador "menor que", en este caso devuelve FALSE
print(a >= b) #Operador "mayor o igual que", en este caso devuelve TRUE
print(a <= b) #Operador "menor o igual que", en este caso devuelve FALSE
print(a == b) #Operador "igual que", en este caso devuelve FALSE

#Estos últimos cinco operadores son solamente de COMPARACIÓN


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