#Variables
my_string_variable = "My String varible"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_city_variable = "Altura"
print(my_city_variable)


#Concatenacion de variables en un print:
#En el momento que le pasamos todas las variables separadas por comas nos sirve para pasarle diferentes datos que va a montar dentro de  una cadena, Para transforfarmo en una cadena de texto.
print(my_string_variable,my_bool_variable,my_int_variable,my_city_variable)
print("Este es el valor de:",my_bool_variable)


#Algunas funciones del systema.
print(len(my_string_variable)) #Esto nos cuenta cuantos caracteres tiene dicha variable , contando los espacios.

#Variables en una sola línea.
name, surname, alias, age = "Bogdan", "George", "Boxan", 32
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias) 

#Cambiamos su tipo :
name = 32
age = "Bogdan"
print(name)
print(age)

address: str = "Mi dirección"
address = 33
print(address)
print(type(address))
