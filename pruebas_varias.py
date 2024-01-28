# name = "Mi nombre es bogdan"
# print(name + str(5))
# print(type(name))

# print("Bogdan" " " * 5)

# print(5 > 6) 

# print(len("Holaaaaaa"))


my_tuple = tuple()
my_tuple = ("Bogdan", "George", "Vintila", "Vintila")
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple.count("Vintila")) # Sale 2 veces.
print(my_tuple.count("George")) # Sale 1 vez.
print(my_tuple.index("Bogdan")) # Posición 0

my_list = list()
my_other_list = []
print(type(my_list))
my_list = (35, 25, 33, 45)
print(my_list)
print(len(my_list))
print(my_list[2])
print(my_list.count(35))

my_other_list = "BOGDAN", "George", "George",5, "Vintila"
print(my_other_list)
print(my_other_list.count("George"))
print(my_other_list + my_list)
print(len(my_list + my_other_list))

name = "Bogdannnnn"
print(name)
print(name.count("n"))
print(name.isnumeric()) 
print(name.upper())


