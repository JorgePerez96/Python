
my_String = "Mi String"
My_other_String = "Mi otro String"

print(len(my_String))
print(len(My_other_String))
print(my_String + " " + My_other_String)

my_new_line_String = "Este es un String\ncon salto de linea"
print(my_new_line_String)

my_tab_String = "\tEste es un String con tabulacion"
print(my_tab_String)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)


# Formato
name, lastname, age = "Jorge", "Perez", 28
print("Mi nombre es {} {} y mi edad es {} años".format(name, lastname, age))
print("Mi nombre es %s %s y mi edad es %d años" % (name, lastname, age))
print("Mi nombre es " + name + " " + lastname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {lastname} y mi edad es {age} años")


#Desempaquetado de caracteres 

language = "python"
a, b, c, d, e, f = language
#print(b)
#print(e)

# Division 

language_slice = language[1:3]
print(language_slice)

language_slice = language[0:5]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)


# Funciones del lenguaje con cadenas

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo 

