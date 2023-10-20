#La tupla es otra colección de datos. Al igual que la lista puede guardar diferentes tipos de datos pero poseen varias diferencias respuesto una de otra

#Las tupas se declaran con paréntesis
#Una vez creada, una tupla no puede ser modificada
#Al ser un elemento inmutable, las tuplas poseen menos métodos que las listas

my_tuple = ("hello world", 12, True, 4.3, "amazing")

empty_tuple = tuple()

#Es posible separar elementos de una tupla si se guardan en otra variable

my_new_tuple = my_tuple[0:2]
print(my_tuple)
print(my_new_tuple)

#Métodos válidos de una tupla
print(my_new_tuple.count(12))
print(my_tuple.index(4.3))
print(len(my_new_tuple))

#También es posible utilizar operadores con las tuplas
other_tuple = my_new_tuple + my_tuple
print(other_tuple)

#Para editar una tupla se puede convertir a lista
random_list = list(my_tuple)
print(type(random_list))

print(65*1150)
