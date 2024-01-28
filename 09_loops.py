# Loops o bucle
#While es como un if infinito por lo tanto si que le podemos meter un else. De lo contrario un else siempre unido al if.
"""
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condicción es mayor o igual que 10")

print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
      print("Se detiene la ejecucción")
      break # Esto nos sirve para nosotros indicarle al bucle que se pare y se deje de ejecutar.

    print(my_condition)

  

print("La ejecucción continua")


# Bucle For, nos sirve para que un codigo se repita varias veces pero en funcción de una condición.

my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)
  

my_tuple = (35, 1.70, "Bogdan", "Bogdan", "George")
for element in my_tuple:
    print(element)


my_set = {"Bogdan", "George", 35}
for element in my_set:
    print(element)


my_dict = {"Nombre": "Bogdan", "Apellido": "George", "Edad": 32, 1:"Python"}
for element in my_dict:
    print(element)
"""