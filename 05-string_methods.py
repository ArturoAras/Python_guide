#Así como existen las built-in functions (ver doc 03), Python posee métodos nativos para trabajar con strings

city = "manchester"
cities = ["london", "brighton", "liverpool", "leicester"]

print(city.capitalize()) #Convierte el primer caracter en mayúscula
print(city.count("e")) #Cuenta cuantas veces se repite el parámetro en el string
print(city.endswith("er")) #Compara el final del string contra el parámetro y devuelve un booleano si hay o no hay coincidencia
print(city.endswith("zzz"))
print(city.startswith("man")) #Compara el comienzo del string contra el parámetro y devuelve un booleano si hay o no hay coincidencia
print(city.startswith("zzz"))
print(city.find("e")) #Busca el parámetro dentro del string y devuelve la posición de la primera coincidencia, si no lo encuentra devuelve "-1"
print(city.rfind("e")) #Busca el parámetro dentro del string y devuelve la posición de la ultima coincidencia, si no lo encuentra devuelve "-1"
print("My city is {}".format(city.capitalize())) #Formatea el string para reemplazar valores en una cadena de texto
print(city.index("e")) #Busca el parámetro dentro del string y devuelve la posición de la primera coincidencia, si no lo encuentra devuelve ValueError
print(city.rindex("e")) #Busca el parámetro dentro del string y devuelve la posición de la última coincidencia, si no lo encuentra devuelve ValueError
print(city.isalnum()) #Chequea si el string es alfanumérico y devuelve un booleano
print(city.isalpha()) #Chequea si todos los caracteres del string son alfabéticos y devuelve un booleano
print("IsDecimal", "91".isdecimal()) #Chequea si todos los caracteres son decimales (0-9)
print("IsNumeric", "1".isnumeric()) #Chequea si todos los caracteres del string son dígitos (0-9 y algunos otros símbolos)

my_cities = " ".join(cities)
print("Ciudades: ", my_cities) #Devuelve un string concatenado
print(city.strip("er")) #Remueve todos los caracteres que empiecen o terminen con lo que se le pasa como parámetro
print(my_cities.replace("brighton", city)) #Busca y Reemplaza el primer parámetro dentro del string por el segundo
print(my_cities.split()) #Separa el string y lo convierte en una lista
print(my_cities.title()) #Convierte la primera letra de cada palabra en mayúscula
print(my_cities.swapcase()) #Invierte mayúsculas y minúsculas
