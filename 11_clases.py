#Clases
#Las clases se definen con la primera letra en mayusculas y todo junto.
#En Python, una función es un bloque de código que realiza una tarea específica cuando es llamada. Sirve para encapsular una pieza de lógica o tarea repetitiva, permitiendo reutilizar ese código en diferentes partes de un programa.


class MyEmptyPerson:
    pass
print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "sin alias", mote = "sin mote"):
     self.full_name = f"{name} {surname} ({alias} ({mote})"
    def walk (self):
       print(f"{self.full_name} esta caminando")


my_person = Person("Bogdan", "Vintila")
print(my_person.full_name)
my_person.walk()

my_other_person = Person ("Bogdan", "George", "Vintila")
print(my_other_person.full_name)



