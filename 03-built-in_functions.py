#En Python, como en todos los lenguajes de programación, hay palabras reservadas que cumplen una funcionalidad específica
#Estas keywords a las que nos referimos se llaman built-in functions y son funciones nativas de Python
#A continuación hacemos un repaso de las funciones más comunes en Python

help("keywords") #Comienza una sesión de ayuda interactiva con el parámetro con recibe. En este caso devuelve una lista de las keywords en Python
print("DIR() funcion: \n", dir(ciudad)) #Devuelve todas las propiedades y métodos de un objeto en específico sin sus valores

print("\n Print function") #Imprime texto en consola


edad = str(27) # str() crea o transforma una variable a tipo string
print(f"Mi número {edad} es de tipo {type(edad)}") # type() devuelve el tipo al que corresponde el objeto


edad = float(edad) # float() crea o transforma una variable a tipo flotante
print(f"Mi número {edad} es de tipo {type(edad)}")


edad = int(edad) # int() crea o transforma una variable a tipo entero
print(f"Mi número {edad} es de tipo {type(edad)}")


print(len("Longitud de texto")) #Devuelve la longitud del parámetro


user_input = input() #Permite al usuario inresar información por teclado y lo lee
print(f"El usuario escribió: {user_input}") 


my_list = list("MarceloGallardou") #Crea una lista con el argumento que se le proporciona
print(my_list)
print(sorted(my_list)) #Recibe una lista y devuelve una nueva ordenada de todos los artículos en orden ascendente
print(min(my_list)) #Devuelve el item más pequeño de una lista de elementos iterables. En este caso devuelve "G"
print(max(my_list)) #Devuelve el item más grande de una lista de elementos iterables. En este caso devuelve "u"
print(sum([3,4,2.2,1])) #Devuelve la suma de todos los componentes de un objeto iterable


my_dict = dict(nombre ="Kevin", apellido = "De Bruyne") #Crea un diccionario con los argumentos que se le poporciona. El orden siempre tiene que ser key=value
print(my_dict)



###################################################################################################
############# Las keywords no mencionadas serán tratadas más adelante en este guía ################
###################################################################################################