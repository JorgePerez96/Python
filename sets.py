

### Sets ###

# Definicion 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario 

my_other_set = {"Jorge", "Perez", 27}
print(type(my_other_set))

print(len(my_other_set))

# Insercion

my_other_set.add("JorgeP")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("JorgeP") #Un set no admite repetidos

print(my_other_set)

# Busqueda

print("Jorge" in my_other_set)
print("Joge" in my_other_set)

# Eliminacion

my_other_set.remove("Perez")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) # name 'my_other_set' is not defined

# Transformacion

my_set = ("Jorge", "Perez", 28)
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"John", "Jones", "Phyton"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"javascript", "C#"}))
print(my_new_set.difference(my_list))

