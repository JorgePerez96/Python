

### Tuples ###

# Definicion 

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Jorge", "Perez", "Jorge")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))
print(my_other_tuple)
print(type(my_other_tuple))

# Acceso a elementos y busqueda

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) Error
#print(my_tuple[-6]) Error 

print(my_tuple.count("Jorge"))
print(my_tuple.index("Perez"))
print(my_tuple.index("Jorge"))

#my_tuple[1] = 1.80 

# Concatenacion 

my_sun_tuple = my_tuple + my_other_tuple
print(my_sun_tuple)

# subtuples

print(my_sun_tuple[3:6])

# Tuple mutable con conversion a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "JorgeP"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminacion 

#del my_tuple[1] #TypeError: 'tuple' object doesn't support item deletion

del my_tuple
print(my_tuple) #NameError: name 'my_tuple' is not defined


