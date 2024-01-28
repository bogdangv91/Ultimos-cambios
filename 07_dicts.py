#Diccionarios.
#En Python, un diccionario es una estructura de datos que te permite almacenar pares de clave-valor. Es similar a una lista, pero en lugar de indexar los elementos mediante números enteros como en las listas, en un diccionario se accede a los valores a través de claves únicas.

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {"Nombre": "Bogdan", "Apellido": "George", "Edad": 32, 1:"Python"}

my_dict = {"Nombre": "Bogdan",
           "Apellido": "George",
           "Edad": 32,
           "Lenguaje": {"Python", "Swift", "Kotlin"},
           1: 1.73
           }
print(my_other_dict)
print(my_dict)
print(len(my_other_dict)) # Estamos preguntando cuantos elementos tenemos. En este caso son 4.
print(len(my_dict))# Estamos preguntando cuantos elementos tenemos. En este caso son 5.
print(my_dict["Nombre"]) # Lo utilizamos para acceder a una elemento. 

"""
del my_dict["Edad"]
print(my_dict)
""" # Esta es la forma que tenemos para eliminar un elemento de nuestro diccionario. Tnemos que ponerle delante el DEL.
print("Bogdan" in my_dict)# Le estamos preguntando si Bogdan esta en my_dict. Nos dará true o false. En este caso nos dara false porque en realidad lo que estamos buscando es por clave y no por valor, si pusieramos nombre en lugar de Bogdan si que nos daria true.
print("Nombre" in my_dict)

print(my_dict.items())      # Nos retorna todo el diccionario de items.
print(my_dict.keys())       # Nos retorna solo las claves : Nombre, Apellido, edad, lenguaje.....
print(my_dict.values())     # Nos retorna todos los valores: Bogdan, George, 32 etc....
