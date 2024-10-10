

### Classes ###

#  Definicion 

class MyEmptyPerson:
    pass # Para poder dejar la clave vacia


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y politicas


class Person:
    def __init__(self, name, lastname, alias="Sin alias"):
        self.full_name = f"{name} {lastname} ({alias})" #Propiedad publica
        self.__name = name #Propiedad privada
        
    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} esta caminando")
        
        
my_person = Person("Jorge", "Perez")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Giovanni", "Perez", "Cerrillo")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Jorge (tazo dorado)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
