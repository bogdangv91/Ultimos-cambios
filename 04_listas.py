#Lists
my_list = list()
my_other_list = []
print(len(my_list)
      
      )
my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))


my_other_list = [35, 1.70,"Bogdan", "George"]
print(type(my_other_list))
print(len(my_other_list))
print(my_other_list[0]) # Esto nos permite acceder a los valores de la lista.
print(my_other_list[1])
print(my_other_list[-1])# Recordar que al ponerle un - delante estamos accediendo a los valores de la lista pero por el final y no por el principio.
print(my_other_list[-4])
print(my_list.count(30))# Esto nos ayuda a contar cuantas veces sale un elementos dentro de la propia lista.   my_list = [35, 24, 62, 52, 30, 30, 17] aqui lo tenemos 2 veces .... por lo tanto en la terminal nos pintaria 2.

age, height, name, surname = my_other_list

print(my_list + my_other_list)#Aqui estamos concatenando 2 listas.

my_other_list .append("Mouredev") # Con la operació Append va a insertar al final de nuestra lista lo que nosotros le pongamos.
print(my_other_list)

my_other_list.insert(1, "Azul") # El insert nos perite insertar algo que nosotros queramos en la posición que le marquemos. en este caso le hemos dicho que lo inserte en la posición 1.
my_other_list.insert(2, "Verde")
print(my_other_list)
my_other_list.remove("Azul") # Remove nos permite eliminar un valor que nosotros le hemos metido a la lista.

my_list.clear() # Esto nos permite borrar la lista entera.











my_list = "Hola Python"
print(my_list)
print(type(my_list))































"""
#Crear una variable
putos =["Bogdan George","Barri","Pepe","Angel","German","Feti","Bogdan George","Barri","Pepe","Angel","German","Feti","Bogdan George","Barri","Pepe","Angel","German","Feti"]
#Imprimir por pantalla: Hola, Bogdan!
print("Che puto, " + putos[-2] + "!")
for puto in putos:
    print("Che puto, " + puto.upper() + "!") 
    print("- - -") 
    """


   







