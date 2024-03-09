# -*- coding: utf-8 -*-
"""
1 - Definir una función max() que tome como argumento dos números y
 devuelva el mayor de ellos. (Es cierto que python tiene una función max() 
incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""
num1 = int(input("introduce el numero1: "))
num2 = int(input("introduce el numero2: "))

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print(max())
#%%

nombre = input("Introduzca su nombre: ")
edad = int(input("Introduzca su edad: "))
pais = input("Introduzca su Pais de nacimiento: ")

print("Hola", nombre ,"usted tiene", edad ,"años y su pais de nacimiento es", pais)


#%%
"""
Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
palabra = input("escribe una palabra: ")
for i in range(10):
    print(palabra)
#%%
"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla
todos los años que ha cumplido (desde 1 hasta su edad).
"""

edad = int(input("escriba su edad: "))

for i in range(edad):
    i += 1
    print(f"has cumplido {i} años")

#con while =============================

edad = int(input("ingrese su edad: "))
i = 1
while i < edad:
    print(f"su edad es {i}.")
    i+= 1

#%%
"""
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1 hasta ese número
separados por comas.
"""

num = int(input("ingrese un numero positivo: "))

for i in range(1, num+1, 2):

    print(f"{i}",  end=",")


#%%
"""
Ejercicio 4
Escribir un programa que pida al usuario un número entero 
positivo y muestre por pantalla la cuenta atrás desde ese número
hasta cero separados por comas.
"""
numero = int(input("ingrese un numero positivo: "))

for i in range(numero,-1, -1):
    print(i, end=",")










