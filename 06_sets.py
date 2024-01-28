# Sets. Set es un tipo de dato.En Python, un set es una colección desordenada de elementos únicos e inmutables. Se define utilizando llaves {} y separando los elementos por comas. A diferencia de las listas o las tuplas, los sets no admiten elementos duplicados y no conservan un orden específico.

my_set = set()

my_other_set = {} # Se define con {}
print(type(my_set))
print(type(my_other_set)) # Inicialmente es de class dic.(diccionario)


my_set = ("Pepe", "Bogdan")
print(my_set)
my_other_set = {"Bogdan", "George", 35} # Nosotros al meterle {} lo convertimos en class set y para meter datos tenemos que separarlos por comas.
print(type(my_other_set))
print(len(my_other_set)) # Tiene 3 elementos.


my_other_set.add("Vintila")
print(my_other_set) # Un set no es una estructura ordenada.
my_other_set.add("Vintila")# Un set no admite repeticiones.
print(my_other_set)

print("Bogdan" in my_other_set) # Esto nos perimite saber si es true o false que un elemento  esta dentro de nuestro set.
print("Pepe" in my_other_set)
print("Barri" in my_other_set)
#my_other_set.remove("Bogdan") Si que nos deja borrar un elemento y tambien nos deja borrar todo el set.


"""
my_set = {"Bogdan", "George", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # Al pasarlo a lista ya podemos acceder a los elementos.
"""
print(my_other_set.difference(my_set)) # Aqui le estamos preguntando cuales son las diferencias entre un set y otro set.