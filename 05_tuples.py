# Tuples (tuplas)
# Una tupla es un conjunto de valores. En Python, una tupla es una estructura de datos similar a una lista, pero con la particularidad de ser inmutable, es decir, una vez creada, no se pueden modificar sus elementos. Se define utilizando paréntesis () y puede contener cualquier cantidad de elementos, separados por comas.

my_tuples = tuple()
my_other_tuple = ()

my_other_tuple = (35, 60, 30 )
print(my_other_tuple)
my_tuple = (35, 1.70, "Bogdan", "Bogdan", "George")

print(my_tuple)
print(type(my_tuples))
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Bogdan")) # Esta función nos permite contar cuantas veces sale lo que nosotros le marquemos, en este caso un un str que seria Bogdan.
print(my_tuple.count("George"))
print(my_tuple.index("George")) # Con index nos permite ver en que posición esta situado.


print(my_other_tuple + my_tuple)

"""
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple.insert(2, "Verde")
print(tuple(my_tuple))
"""
# Para que nos deje insertar algo dentro de la tupla tenemos que cambiarla a class list ya que las tuplas son inamovibles.

