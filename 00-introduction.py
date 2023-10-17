#Curso de Python por Ariel Aras

#En los lenguajes de programación, los comentarios son mensajes que dejan los programadores y que no son interpredados por ningún interprete de texto
#Hay varias formas de añadir comentarios al código en Python. La más sencilla y conocida es utilizando el símbolo de numeral o almohadilla (#)
#Otra manera de ingresar comentarios es con las comillas simples ('') o las comillas dobles("")
'Esto es un comentario'
"Esto también es un comentario"
#Por último se encuentran los comentarios multilíneas, que se realizan con tres comillas dobles o simples
'''
Esto es un
comentario multilínea
''' 
"""
Esto también
es un comentario
multilínea
"""


################################################################################################################################################


#Una variable es un espacio en la memoria del ordenador donde se guarda un dato
#La forma de crear una variable y asignarle un dato en Python es la siguiente =>   key = value
my_variable = 2023    #Cree una variable llamada my_variable y le guardé el dato 2023


################################################################################################################################################


#Python posee cuatro tipos de datos primitivos: cadenas de texto (strings), numéricos enteros (int), numéricos decimales/flotantes (float) y booleanos
#Los datos pueden guardarse en una variable para trabajar con ellos más adelante
my_string_data = "Esto es una cadena de texto" #Con las comillas creé un string y lo asigné a una variable
my_int_data = 26 #Los datos de tipo numérico no necesitan comillas
my_float_data = 2.6
my_boolean_data = True #Los datos booleanos solo pueden tomar los valores True o False y siempre inician com mayúscula


#################################################################################################################################################


#Python, como todo lenguaje, tiene funciones que vienen incluidas en el lenguaje

#La función print() muestra en consola lo que se le ingresa dentro de los paréntesis
print("------------------------ACÁ EMPIEZA EL FLUJO DE EJECUCIÓN------------------------")
print(2023)
print("Hello world") #Si se quiere mostrar un mensaje hay que ingresarlo entre comillas
print(my_string_data) #También se le pueden pasar variables a las funciones

#La función type() evalúa el tipo de dato que se ingresa dentro de los paréntesis
type("Hello world") #La función type evalúa pero no muestra en pantalla
print(type("Hello world")) #Se pueden combinar funciones para ver los resultados de type()
print(type(my_boolean_data)) #type() también evalúa variables

#Las combinaciones son infinitas

