#Python posee cuatro tipos de colecciones de datos: Listas, Tuplas, Sets y Diccionarios
#Las listas son colecciones ordenadas de datos que pueden ser modificadas y las cuales aceptan datos repetidos

#Para crear una lista hay dos formas: con una función built-in o con corchetes

countries = list() #Lista vacía creada con la función built-in list()
cities = [] #Lista vacía creada con corchetes

print(len(countries)) #Es posible utilizar la función len() para saber la cantidad de datos guardados en la lista, en este caso 0

cities = ["Montevideo", "Cali", "Valparaíso", "Río de Janeiro", "Lima"] #Lista con elementos guardados
countries = ["Argentina", "Colombia", "México", "Finlandia", "Canada"]
print(len(cities)) #len() devuelve la cantidad de elementos, en este caso 5

#Se puede acceder a los elementos de la lista mediante su índice de la siguiente forma
print(cities[2]) #Entre corchetes escribo el índice de la ciudad que quiero mostrar
print(cities[-3]) #Si el índice se escribe en negativo empieza a contar de atrás para adelante

#Desempaquetar elementos de una lista
city1, city2, *other_cities = cities #La última variable guarda el resto de las ciudades
print(city1)
print(city2)
print(other_cities)

#Se pueden modificar elementos de una lista
print(cities)
cities[3] = "Buenos Aires"
print(cities)

#Con el operador in es posible chequear si un elemento existe dentro de una lista o no 
search_city1 = "Helsinki" in cities
search_city2 = "Cali" in cities
print(search_city1, search_city2)

#Añadir elementos a una lista
cities.append("Sidney") #Añade un elemento al final de la lista
print(cities)
cities.insert(2, "Asunción") #Añade un elemento en un índice específico, en este caso entre Cali y Valparaíso
print(cities)

#Eliminar elementos de una lista
cities.remove("Lima") #Remueve el elemento especificado en la lista
print(cities)
cities.pop() #Elimina el último elemento de la lista 
print(cities)
cities.pop(0) #Si se le proporciona un índice elimina el elemento especificado
print(cities)
del cities[1] #De esta forma, la keyword del elimina un elemento de la lista
print(cities)
del cities #De esta otra forma, del elimina la lista

#Al igual que con los strings, es posible cortar las listas y guardarlas en variables
two_countries = countries[1::2] #Los cortes y los intervalos funcionan de la misma manera que los strings
print(two_countries)

#Copiar listas
countries2 = countries.copy()
print(countries2)

#Vaciar listas
countries.clear()
print(countries, len(countries))

#Es posible unir listas con el operador +
countries = countries + countries2
print(countries)
countries.extend(countries2) #De esta forma también se unen ambas listas
print(countries)

print(countries.count("Argentina")) #Cuenta y devuelve la cantidad de veces que se encuentras los parámetros en la lista
print(countries.index("Finlandia")) #Devuelve la posición de la primera coincidencia
countries.reverse() #Revierte el orden de los objetos en la lista
print(countries)
countries.sort() #Reordena los elementos de forma ascendente
print(countries)
countries.sort(reverse = True) #Reordena los elementos de forma descendente
print(countries)