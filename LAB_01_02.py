# -*- coding: utf-8 -*-
"""
Ejercicio 1
"""
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

resultado = num1+num2
resultado1 = num1-num2
resultado2 = num1*num2
resultado3 = num1//num2
print(f" resultado:\nsuma:{resultado}\nresta:{resultado1}\nmultiplicacion{resultado2}\ndivision{resultado3} ")
#%%
"""
Ejercicio 2
2) Solicita un número al usuario y determina si es par o impar
"""
num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print(num, "es par.")
else:
    print(num, "es impar.")



#%%
"""Ejercicio 3
3) Pide la base y la altura de un triángulo al usuario y calcula su área

"""
print("AREA DEL TRIANGULO")
num1 = int(input("ingrese el numero de la base del triangulo: "))
num2 = int(input("ingrese la la altura del triangulo: "))
operacion = (num1*num2)/2
print(operacion)
#%%
"""Ejercicio 4
3) Crea una función que calcule la factorial de un número.
"""
def funcion(n):
    if n == 0 or n==1:
        resultado = 1
    elif n >1:
        resultado = n*funcion(n-1)
    return resultado
numero = int(input("ingrese un numero: "))

print(funcion(numero))


#%%
"""
ejercicio 5
Verifica si un número ingresado por el usuario es primo o no.

"""

def primo(num):
    for i in range(2, num):
        if num % i == 0:
            print("No es primo", i, "es divisor")
            return False
    print("Es primo")
    return True
numero = int(input("Ingrese un numero: "))
print(primo(numero))

#%%

"""
EJercicio 6
Toma una cadena de texto y muestra su inversión.
"""
def cadena(string):
    if len(string) == 0:
        return string
    else:
        return cadena(string[1:]) + string[0]


string = input("ingresa un texto: ")

print("resultado : ", end="")
print(cadena(string))
#%%
"""
Ejercicio 7
Calcula la suma de los números pares en un rango especificado por el usuario.
"""
i = int(input("ingrese un numero: "))
f = int(input("ingrese el segundo numero: "))
suma=0
while i <= f:
    if i % 2 ==0: 
        print(i)
        suma = suma + i
    i+= 1


#%%
"""
ejercicio 11
Ordena una lista de números ingresados por el usuario de menor a mayor
"""
numeros = [1,2,34,4311,23,3,2,4,4,12,3,2,3,4,4,4,4,4,]
numeros.sort()
print(numeros)

while True:
    num = int(input("ingrese los numeros: "))
    

#%%
"""ejercicio 12 
12) Verifica si una palabra ingresada por el usuario es un palíndromo.

"""
palabra = input("ingrese una palabra: ")
palabra_resulta = palabra[::-1]
if(palabra == palabra_resulta):
    print("es palindromo")
else:
    print("no es palindromo")

