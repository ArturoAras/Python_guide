# 01 - Crea cuatro variables (un string de seis o más caracteres con todas sus letras en minúsculas, un int, un float y un boolean)

# 02 - Con el string realiza las siguientes acciones e imprímelas en pantalla:
#    a - Imprime en pantalla el string, su largo y las letras separadas por un guión
#    b - Convierte el string en mayúsculas y en título
#    c - Muestra en pantalla solamente las letras de posiciones impares del string
#    d - Muestra las primeras dos letras del string y sumalas al string original
#    e - Busca la letra "h" en la cadena y si no la encuentra devuelve "-1"
#    f - Averígua las primeras dos letras y certifica que el string comience con dichas letras
#    g - Voltea el orden de las letras

# 03 - Con el int realiza las siguientes acciones e imprímelas en pantalla:
#    a - Súmale 30
#    b - Divídelo en tres
#    c - Elevalo al cubo
#    d - Conviertelo en string y devuelve el tipo de dato

# 04 - Con el float realiza las siguientes acciones e imprímelas en pantalla
#    a - Restale 2.4 y asignale el resultado
#    b - Multiplicalo por siete y asignale el resultado
#    c - Averigua si es mayor que 22.1
#    d - Transformalo en int y devuelve el tipo de dato

# 05 - Con el boolean realiza las siguientes acciones e imprímelas en pantalla
#    a - Devuelve el contrario
#    b - Niega el valor y guárdalo en la misma variable

#01
my_string = "murcielago"
my_int = 21
my_float = 1.7
my_boolean = False

#02
a = "-" #A
print(f"Mi string es {my_string} \nTiene {len(my_string)} letras \nSus letras son: {a.join(my_string)}") #A
print(f"{my_string.upper()} y {my_string.capitalize()}") #B
print(my_string[1::2]) #C
my_string += my_string[:2] #D 
print(my_string) #D
print(my_string.find("h")) #E
print(f"Las dos primera letras son {my_string[:2]} y si las busco en el string me devuelve {my_string.startswith(my_string[:2])}") #F
print(my_string[::-1]) #G

#03
print(my_int + 30) #A
print(my_int / 3) #B
print(my_int ** 3) #C
print(f"{str(my_int)} está compuesto por {len(str(my_int))} caracteres") #D

#04
my_float -= 2.4 #A
print(my_float) #A
my_float *= 7 #B
print(my_float) #B
print(f"¿Es {my_float} mayor que 22.1?", my_float > 22.1) #C
my_float = int(my_float) #D
print(type(my_float)) #D

#05
print(not my_boolean)
my_boolean = not my_boolean
print(my_boolean)