### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_float_variable = 1.8
print(my_float_variable)
print(type(my_float_variable))

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)
print(type(my_bool_variable))


# Concatenacion de variables en un print 
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
# len obtiene largo de la cadena 
print(len(my_string_variable))

# variables en una sola linea
name, surname, alias, age = "Jorge", "Perez", 'George', 28
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)


# inputs
name = input('¿Cual es tu nombre? ')
age = input('¿Cuantos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo 
name = "Jorge"
age = "28"
print(name)
print(age)
print(type(name))
print(type(age))


# ¿Forzamos el tipo?
adress: str = "Mi direccion"
adress = input('¿Cual es tu direccion? ')
adress = True
adress = 5
adress = 1.2
print(type(adress))