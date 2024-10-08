



#Operadores aritmeticos
print("3+4 = ", 3+4)
print("3*4 = ", 3*4)
print("3/4 = ", 3/4)
print("3-4 = ", 3-4)

print("10 % 3 =", 10 % 3)
print("10 // 3 =", 10 // 3)
print("2 ** 3 =", 2 ** 3)
print("2 ** 3 + 3 - 7 / 1 // 4 =", 2 ** 3 + 3 - 7 / 1 // 4)

#Operaciones con cadena de texto
print("Hola " + "Python " + "¿Que tal?")
print("Hola " + str(5))

#Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))



### Operadores comparativos ###

# Operaciones con enteros
print("3 > 4 = ", 3 > 4)
print("3 < 4 = ", 3 < 4)
print("3 >= 4 = ", 3 >= 4)
print("3 <= 4 = ", 3 <= 4)
print("3 == 4 = ", 3 == 4)
print("3 != 4 = ", 3 != 4) #Es diferente o igual a 

# Operaciones con cadena de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python") #Ordenacion alfabetica por ASCII
print(len("aaaa")>= len("abaa")) #Cuenta caracteres 
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Logicos ###

# Basada en el algebra de Bolee
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
