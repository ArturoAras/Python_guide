#Cualquier dato escrito entre comillas simples, dobles o triples es un string
#Para crear una variable de tipo string es posible hacerlo con el signo igual o utilizando la función str() de Python 

pi_number = 3.1416
my_string = "Hello world"
my_second_string = str(pi_number)
print(type(my_second_string))


#Los strings pueden concatenarse mediante los operadores ya vistos
my_string = "Hello "
my_second_string = "world"
print(my_string + my_second_string)
print(my_string * 3)

#En Python un \ seguido de un caracter en específico funciona como secuencia de escape que no es leída como parte del string
print("Hello \n world") #Genera un salto de línea
print("Hello \t world") #Aplica una tabulación (8 espacios)
print("Hello \\ world") #Barra invertida
print("Hello \' world") #Comilla simple
print("Hello \" world") #Comilla doble

#Hay muchas formas de formatear un string, a continuación se detallan las tres más importantes

#Formateo antiguo de strings con el operador %
name = "Pablo"
last_name = "Aimar"
profession = "footbaler"
formated_string = "I am %s %s. I am a professional %s" %(name, last_name, profession) #El %s indica que en ese lugar irá una variable de tipo string
print(formated_string)

age = 43
number = 10
formates_int = "I am %d years old and my favourite number is %.2f" %(age, number) #El %d indica que en ese lugar irá una variable de tipo int y el %.2f que se mostrará una variable con los primeros dos dígitos decimales 
print(formates_int)

#Nuevo formateo de strings con la función format()
a = 4
b = 7
print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {:.2f}".format(a, b, a/b)) #Limita a dos dígitos
#Los ejemplos pueden seguir con el resto de los operadores anteriormente vistos


#F-Strings
#Se pueden inyectar los datos en un string si se le agrega una f al comienzo
name = "Cristiano"
last_name = "Ronaldo"
print(f"My name is {name} and my surname is {last_name}")
#Esta última es la más recomendable



#Strings como secuencias de caracteres
#Los strings de Python son secuencias de caracteres y tienen métodos básicos para acceder a ellos como secuencias ordenadas de objetos

#La forma más sencilla es acceder a ellos guardándolos en sus correspondientes variables
city = "Manchester"
a, b, c, d, e, f, g, h, i, j = city #Cada letra del string es guardado en una varible diferente
print(d)

#También se puede acceder a un string a través de su índice. En programación siempre se comienza contando desde el cero
first_letter = city[0]
print(first_letter)

#Si se quiere empezar a contar desde el último caracter se cuenta hacia atrás
last_letter = city[-1]
print(last_letter)

#Para asignar un rango en específico se indica de la siguiente manera
first_five_letters = city[0:5] #Arranca en la posición cero y finaliza antes de la quinta
print(first_five_letters)
letters = city[5:] #Comienza en la quinta posición y termina en el final
print(letters)
letters = city[:-3] #Deja afuera las últimas tres letras
print(letters)



#Datos de color

#Se puede hacer saltos en la selección de los strings
letters = city[::2] #Asigna cada dos letras
print(letters)

#Saltos dentro de una selección específica
letters = city[1:9:3]
print(letters)

#Dar vuelta un string
letters = city[::-1]
print(letters)