#Diccionarios

my_dict = {}
my_dict = {"Nombre": "Bogdan" , "Apellido": "George", "Segundo apellido": "Vintila", "Edad": 32 , "Altura": 1.73} 
print(my_dict)
print("Bogdan" in my_dict)
print(len(my_dict))
print(my_dict.items())

my_other_dict = {}
my_other_dict = {"Pepe": 31 , "Barri": 33 , "Feti":31 , "Angel": 32 , "Garito la era": "La era"}
print(my_other_dict)
print(type(my_other_dict))
print(my_dict.items())

my_other_dict.update(my_dict)
print(my_other_dict)
