#Strings:

my_string = "Mi String"
my_other_string = "Mi otro String"
print(len(my_string)) #Con len en este caso..No estamos calculando la longitud de la variable, estamos calculando la longitud de la variable.Las comillas no cuentan, pero los espacios si.
print(len(my_other_string))#Con len en este caso..No estamos calculando la longitud de la variable, estamos calculando la longitud de la variable. Las comillas no cuentan, pero los espacios si.
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" #Aqui nos dejara un espacio al principio de la línea que seria la tabulación.
print(my_tab_string)

my_scape_string = "\tEsto es un tring \n escapado" #Aqui nos va a imprimir lo mismo que antes pero al meterle la \n nos lo imprimirá sin la tabulación pero si con un salto de línea.
print(my_scape_string)

#Formateo.
name, surname, age = "Bogdan","George", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #la f sirve para formatear las variables que tenemos (name, surname, age).

#Desempaquetado de caracteres.
languaje = "python"
a, b, c, d, e, f = languaje #estos serian los caracteres que tenemos definidos empezando por la letra A que se refiere a la primera letra del valor de la variable que en este caso es "Python" que en este caso seria la P.
print(a)
print(b)


 #División
languaje_slice = languaje[1:3] #nos pinta las letras de la 1 a la 3 en este caso pintaría las letras y, t porque la numero 0 seria la P.
print(languaje_slice)

languaje_slice = languaje[1:] #aqui al no meterle nada despues del 1: nos pintaria la primera letra y hasta el final.
print(languaje_slice)

languaje_slice = languaje[-2] #para empezar por el final del valor de la variable   tendriamos que ponerle un - delante del numero de la letra que queramos pintar.
print(languaje_slice)

 #Reverse, para darle la vuelta al valor de la variable.
reversed_languaje = languaje[::-1]
print(reversed_languaje) #aqui nos daria la vuelta y el valor de la variable lo pintaria al revés.


# languaje = "Elefante"
# a, b, c, d, e, f, g, h = languaje
# print(a)
# print(b)
# print(c)
# print(d)

# languaje_slice = languaje[1:3]
# print(languaje_slice)

# languaje_slice = languaje[-2]
# print(languaje_slice)

# reversed_languaje = languaje[::-1]
# print(reversed_languaje) 

#Funciones.
print(languaje.capitalize())#esto nos hace que se imprima la primera letra en mayuscula.
print(languaje.upper()) #Esta función nos deja ponerlo todo en mayusculas.
print(languaje.count("t")) #Esta función nos dice cuantas letras tiene de lo que nosotros le marquemos en el parentesis, en este caso la T.
print(languaje.isnumeric()) #Esta función nos permite preguntarle si es  numerico. en este caso nos pintaria False.
print("1".isnumeric()) #Esta función nos permite preguntarle si es un numero que en ester caso nos pintaria TRUE.
print(languaje.lower()) #Esta función nos permite pintarlo todo en minusculas.
print(languaje.upper()) #PREGUNTAR A PEPE!!!!!!!!!!!! #PREGUNTAR A PEPE!!!!!!!!!!!! #PREGUNTAR A PEPE!!!!!!!!!!!! #PREGUNTAR A PEPE!!!!!!!!!!!! #ISUPER nos permite preguntarle si esta en minusculas y nos pintaria un true o false.
print(languaje.lower().isupper()) #PREGUNTAR A PEPE!!!!!!!!!!!! #PREGUNTAR A PEPE!!!!!!!!!!!! #PREGUNTAR A PEPE!!!!!!!!!!!! #PREGUNTAR A PEPE!!!!!!!!!!!! #ISUPER nos permite preguntarle si esta en minusculas y nos pintaria un true o false.

print(languaje.startswith("py")) #Esta función nos permite preguntar si empieza por (lo que le marquemos en el parentesis) que en este caso le hemos dicho PY y nos pintara un true.

#Crear una variable
name = "Bogdan George"
#Imprimir por pantalla: Hola, Bogdan!
print("Hola, " + name + "!")
print(name.count("o"))
print(name.upper())
print(name.isnumeric())
print(len(name))
print(type(name))
