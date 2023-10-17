#Como bien se especificó en el documento 00-introduction.py, las variables son espacios en memoria. Estas variables pueden o no almacenar un dato
#En Python no es posible declarar una variable sin asignarle un valor o un tipo de dato pero si es posible asignarle un valor vacío

nombre = str() #Con la función str() declaro la variable nombre y le indico a Python que va a guardar un string vacío
print(nombre)
print(type(nombre)) #La función type() me confirma que nombre es una variable de tipo string

#A la hora de declarar una variable es una buena práctica utilizar nombres explícitos para identificar fácilmente los datos con contengan
nombre = "Michael"
apellido = "Jordan"
dorsal_club = 23

#Otra buena práctica en Python nos indica que a la hora de nombrar una variable tenemos que utilizar el estilo snake_case y no el camelCase
primer_nombre = "Lionel"
segundo_nombre = "Andrés"
primer_apellido = "Messi"
numero_hijos = 3

#Es posible declarar más de una variable en una misma línea de código 
a, b, c = "Carlos", "Salvador", "Bilardo"
print(a, b, c)
print(c, b, a)
print(a, c)

#Las variables pueden sobreescribirse
ciudad = "Nueva York"
print(ciudad)
ciudad = "Roma"
print(ciudad)


