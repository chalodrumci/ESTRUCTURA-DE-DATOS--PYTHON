"""
=========================================RECURSIVIDAD===========================================================
1) Ejercicio 1: Escribe una función recursiva que imprima los números pares 
del 1 al 100.
"""

"""def par(num):
    if num <= 100:
        if num % 2 == 0:
            print(num)
        par(num + 2)
par(2)"""
############################################## OTRO METODO CON WHILE
"""x = 0
while x <= 100:
    if x % 2 == 0:
        print(f"el numero {x} es par ")
    x+=1"""
######################otro metodo    
for i in range(1, 101):
    if i % 2 ==0:
        print(f"numero par {i}")

"""
=====================================================================================================
Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n.
"""
#%%
def suma(n):
    if n == 1:
        return 1
    else:
        #en esta linea de codigo podemos ver la recursividad
        resultado = n + suma(n - 1)
        return resultado
numeroIngresado = int(input("ingrese un numero: "))
print(suma(numeroIngresado))
#por ejemplo si ponemos 10
10 + 5
6 + 4
3 + 3
1 + 2
1 + 0
0

#%%
"""
=====================================================================================================
3) Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n.
"""

def piramide(n):
    k = 2*n - 2
    for i in range(n, -1, -1):
        for j in range(k,0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i+1):
            print(n, end=" ")
        print("\r")
piramide(5)



#%%
"""
=====================================================================================================
Ejercicio 4: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.
"""
def Piramide_invertido(n):
    if n > 0:
        imprimir_linea(n)
        Piramide_invertido(n - 1)

def imprimir_linea(num):
    if num > 0:
        print(num, end=" ")
        imprimir_linea(num - 1)
    else:
        print()

# Ejemplo de uso
n = 5
Piramide_invertido(n)
#%%
"""
=====================================================================================================
5) Ejercicio 5 : Escribe una función recursiva que imprima la tabla de multiplicar del n.
"""
def multiplicar(n, multiplicador=1):
    if multiplicador <= 10:
        print(f"{n} x {multiplicador} = {n * multiplicador}")
        multiplicar(n, multiplicador + 1)
entrada = int(input("Ingresa un numero: "))
print(multiplicar(entrada))


"""======================================Arreglos y Matrices:=========================================
===============================================================================================================
"""
#%%
"""
ejercicio 6
6) Crea una matriz de números reales."""
#importamos numpy como np
import numpy as np
#luego usamos np.array para crear nuestra matriz
matriz =np.array([[1.9,2,3],
                 [4.8,5/2,6],  
                 [7,8,9.9]])
print(matriz)
# %%
"""
====================================================================================================
Ejercicio 7
7) Crea una matriz de números complejos
"""
import numpy as np
#es la misma cosa de arriba solo numeros mas complejos
matriz = np.array([[4,1,2,3],
                   [34,1,2,6],
                   [21,2.3,1,7],
                   [3,2,5,6.8]])
print(matriz)

#%%
"""
=======================================================================================================
ejercicio 8
8) Crea una matriz de matrices.
"""
import numpy as np

matriz = np.array([
    [[1,2,4], [9,5,6]], 
    [[34,56,7], [1,9,7]]
])
print(matriz)
# %%
"""=======================================================================================================
ejercicio 9
9) Accede al elemento central de una matriz.
"""

import numpy as np

matriz = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
#esto es facil accediendo al numero de la matricez sabiendo que se empieza desde 0 en una lista
print(matriz[1][1])
# %%
"""=======================================================================================================
ejercicio 10
10) Suma dos matrices de diferentes tamaños.
"""
import numpy as np
#creamos 2 maticez 
matriz1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
matriz2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
#creamos uan variable para sumar ambas matrices
resultado = matriz1 + matriz2
print(resultado)

# %%
"""=======================================================================================================
ejercicio 11
11) Multiplica una matriz por un número
"""
import numpy as np
#cree una funcion para poder poner una entrada que pida al usuario un numero
def multiplicar(x):
    matriz = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    result = matriz*x
    return result
#esta entrada sera igual al parametro que esta en la funcion
entrada = int(input("Ingresa un numero"))
print(multiplicar(entrada))
# %%
"""=======================================================================================================
ejercicio 12
12) Calcula la media de los elementos de una matriz
"""
import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calcular la media de los elementos de la matriz
#usamos mean que devuelve el promedio de los elemento
media = np.mean(matriz)
print("La media de la matriz es:", media)

# %%
