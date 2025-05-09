
"""
EJercicio 1
1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos.
"""
def es_primo(numero):
    if numero < 2:
        return False
    #
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
def numeros_primos(conjunto):
    primos = {num for num in conjunto if es_primo(num)}
    return primos
#este es un ejemplo de 1 al 10 tambien se puede hacer una lista vacia y mediante una entrada poner datos
conjunto_de_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_de_primos = numeros_primos(conjunto_de_numeros)

print("Conjunto original:", conjunto_de_numeros)
print("Conjunto de números primos:", conjunto_de_primos)


#%%
"""
============================================================================================================
EJercicio 2
Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
comienzan con una letra determinada.
"""
def funcion(conjunto, letra):
    cadena = {palabra for palabra in conjunto if palabra.startswith(letra)}
    return cadena
set1 = {"perro", "pollo", "caballo", "cocodrilo", "gusano"}
letra = input("ingrese una letra de lconjunto: ")
palabras_con_letra = funcion(set1, letra)

print(f"Palabras que comienzan con la letra '{letra}':", palabras_con_letra)

#%%

"""============================================================================================================
ejercicio 3
3. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
son divisibles por un número determinado."""

def numeros_divisibles(conjunto, divisor):
    numeros_divisibles = set()
    for numero in conjunto:
        if numero % divisor == 0:
            numeros_divisibles.add(numero)
    return numeros_divisibles

# Ejemplo de uso:
conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 2
numeros_divisibles_por_dos = numeros_divisibles(conjunto_numeros, divisor)
print("Números en el conjunto divisibles por", divisor, ":", numeros_divisibles_por_dos)

#%%
"""
============================================================================================================
Ejercicio 4.
Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que 
están en ambos conjuntos."""
def numeros_comunes(conjunto1, conjunto2):
    return conjunto1 & conjunto2

# Ejemplo de uso:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(numeros_comunes(A, B))  # Output: {4, 5}
"""============================================================================================================
ejercicio5
5. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que 
están en el primer conjunto pero no en el segundo."""

"""============================================================================================================
ejercicio6
6. Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que 
están en el segundo conjunto pero no en el primero.
"""
"""============================================================================================================
ejercicio7
7. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
anagramas."""

"""============================================================================================================
ejercicio 8
8. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
palíndromos."""

"""============================================================================================================
ejercicio 9
9. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
tienen una longitud determinada."""

"""============================================================================================================
ejercicio 10
10. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
contienen una letra determinada."""

"""============================================================================================================
ejercicio 11
11. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
están ordenados de menor a mayor.
"""
"""============================================================================================================
ejercicio 12
12. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
están ordenados de mayor a menor."""

"""============================================================================================================
ejercicio 13
13. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
están duplicados."""

"""============================================================================================================
ejercicio 14
14. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no 
están duplicados."""

"""============================================================================================================
ejercicio 15
15. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
son primos y están ordenados de menor a mayor."""

"""============================================================================================================
ejercicio 16
16. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
palíndromos y están ordenadas de menor a mayor.
"""
"""============================================================================================================
ejercicio 17
17. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
tienen una longitud determinada y están ordenadas de menor a mayor.
"""
"""============================================================================================================
ejercicio 18
18. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
contienen una letra determinada y están ordenadas de mayor a menor."""

"""============================================================================================================
ejercicio 19
19. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que 
están ordenados de menor a mayor y que no están duplicados."""

"""============================================================================================================
ejercicio 20
20. Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son 
palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor."""
