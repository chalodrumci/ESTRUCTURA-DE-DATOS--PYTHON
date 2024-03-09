"""
 ESTRUCTURA DE DATOS FUNDAMENTALES Y ALGORITMOS
GUÍA DE LABORATORIO 
GESTIONAR ASERCIONES – LISTAS ENLAZADAS SIMPLES, Y CIRCULARES
 """

"""EJERCICIO 1
Validar la edad de un usuario."""

"""La función 'isinstance' es una función incorporada en Python que se utiliza para determinar 
si un objeto es una instancia de una clase determinada. 
Esto significa que puedes comprobar si un objeto es una instancia de una clase, una subclase o un tipo específico"""
def validar(edad):
    #La sintaxis de la función isinstance es la siguiente:
    # isinstance(object, classinfo)
    assert isinstance(edad, int), "la edad debe ser entero"
    assert edad >= 18, "La edad debe ser mayor a 18 años"
    print("edad validado")
    
try:
    edad_usuario = int(input("introduce tu edad: "))
    validar(edad_usuario)
except ValueError:
    print("porfavor introduce una edad entera")
except AssertionError as e:
    print(e)
#%%
"""=========================EJERCICIO 2=======================================================
Verificar el tipo de dato de una variable."""
x = 5
assert isinstance(x, int), "x no es de tipo entero"
print("x es un entero")

y = "Hola"
assert isinstance(y, str), "y no es de tipo cadena"
print("y es una cadena")

#%%
"""=========================EJERCICIO 3=======================================================
3. Validar el rango de una calificación."""
calificacion = int(input("ingrese un numero: "))
# Verificamos si  la calificación esté dentro del rango deseado (0-100)
assert 0 <= calificacion <= 100, "La calificación debe estar en el rango de 0 a 100"
print("La calificación es válida:", calificacion)

#%%
"""=========================EJERCICIO 4=======================================================
4. Asegurar que una lista no esté vacía.."""
mi_lista = [1, 2, 3,4,6,5,6,7,8]
# Verificar que la lista no esté vacía
assert len(mi_lista) > 0, "La lista no debe estar vacía"
print("La lista contiene elementos:", mi_lista)

#%%
"""=========================EJERCICIO 5=======================================================
5. Validar la igualdad de dos objetos."""
class MiObjeto:
    def __init__(self, valor):
        self.valor = valor
    
    def __eq__(self, otro):
        if isinstance(otro, MiObjeto):
            return self.valor == otro.valor
        return False

# Ejemplo 
objeto1 = MiObjeto(5)
objeto2 = MiObjeto(5)
objeto3 = MiObjeto(10)

print(objeto1 == objeto2)  #esto sera True
print(objeto1 == objeto3)  #esto sera False

#%%
"""=========================EJERCICIO 6=======================================================
6. Asegurar que un ciclo while se ejecuta al menos una vez."""
primera_vez = True

while primera_vez or not validado:
    entrada = input("Ingrese un número mayor que 10: ")
    numero = int(entrada)
    
    if numero > 10:
        print("Número válido:", numero)
        validado = True
    else:
        print("Número inválido. Intente nuevamente.")
    
    primera_vez = False

#%%
"""=========================EJERCICIO 7=======================================================
7. Asegurar que una función retorna un valor específico."""
def mi_funcion():
    return 822
resultado = mi_funcion()
valor_esperado = 822
assert resultado == valor_esperado, f"La función debería retornar {valor_esperado}, pero retornó {resultado}"

print("La función retornó el valor esperado:", resultado)


#%%
"""=========================EJERCICIO 8=======================================================
8. Validar el estado de una variable después de una operación."""

# Inicialización de la variable
x = 5
# Operación que modifica el estado de la variable
x += 3  # Incrementar x en 3
# Validar el estado de la variable después de la operación
assert x == 8, f"El valor de x debería ser 8, pero es {x}"
print("El estado de la variable después de la operación es correcto:", x)

#%%
"""=========================EJERCICIO 9=======================================================
9. Asegurar que un módulo se ha importado correctamente."""
# Importar el módulo
import random
# Verificar que el módulo se haya importado correctamente
assert 'randint' in dir(random), "Error: No se pudo importar correctamente el módulo random"
print("El módulo random se ha importado correctamente.")


#%%
"""=========================LISTA ENLAZADA Y LISTA CIRCULARES==================================================="""

"""=========================EJERCICIO 10=======================================================
10. Desarrollar el código de buscar nodo en la lista enlazada simple.
Suma de Nodos"""
#estructura
class Nodo:
    def __init__(self, dato):
        #self hace referencia al objeto
        self.dato = dato
        #asigna al nodo que esta vacio
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def buscar_nodo(self, valor):
        actual = self.cabeza
        while actual:
            if actual.dato == valor:
                return actual
            actual = actual.siguiente
        return None

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma

# Ejemplo
lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(7)
lista.insertar_al_inicio(10)

# Busca el nodo
nodo_buscado = lista.buscar_nodo(7)
if nodo_buscado:
    print("Nodo encontrado:", nodo_buscado.dato)
else:
    print("Nodo no encontrado")

#Sumar los nodos
suma_nodos = lista.sumar_nodos()
print("Suma de los nodos:", suma_nodos)


"""=========================EJERCICIO 11======================================================
11. Implementa una función que sume todos los nodos de una lista enlazada simple.
Longitud de la Lista"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma

    def longitud_lista(self):
        longitud = 0
        actual = self.cabeza
        while actual:
            longitud += 1
            actual = actual.siguiente
        return longitud

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(7)
lista.insertar_al_inicio(10)

# Sumar los nodos
suma_nodos = lista.sumar_nodos()
print("Suma de los nodos:", suma_nodos)

# Longitud de la lista
longitud = lista.longitud_lista()
print("Longitud de la lista:", longitud)


#%%
"""=========================EJERCICIO 12======================================================
12. Crea una función que devuelva la longitud de una lista enlazada simple.
Concatenar Listas"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def longitud_lista(self):
        longitud = 0
        actual = self.cabeza
        while actual:
            longitud += 1
            actual = actual.siguiente
        return longitud

    def concatenar_listas(self, otra_lista):
        if self.cabeza is None:
            self.cabeza = otra_lista.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = otra_lista.cabeza

# Ejemplo 1
lista1 = ListaEnlazada()
lista1.insertar_al_inicio(3)
lista1.insertar_al_inicio(7)
lista1.insertar_al_inicio(10)
# Ejemplo 2
lista2 = ListaEnlazada()
lista2.insertar_al_inicio(20)
lista2.insertar_al_inicio(15)

# Longitud de la lista
longitud1 = lista1.longitud_lista()
print("Longitud de la lista 1:", longitud1)

longitud2 = lista2.longitud_lista()
print("Longitud de la lista 2:", longitud2)

# Concatenar listas
lista1.concatenar_listas(lista2)

# Verificar la longitud después de la concatenación
longitud_concatenada = lista1.longitud_lista()
print("Longitud de la lista concatenada:", longitud_concatenada)



#%%
"""=========================EJERCICIO 13======================================================
13. Implementa una función que concatene dos listas enlazadas simples.
Eliminar Duplicados"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def concatenar_listas(self, otra_lista):
        if self.cabeza is None:
            self.cabeza = otra_lista.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = otra_lista.cabeza

    def eliminar_duplicados(self):
        nodos_vistos = set()
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato in nodos_vistos:
                # Eliminar el nodo actual
                anterior.siguiente = actual.siguiente
                actual = actual.siguiente
            else:
                # Agregar el dato al conjunto de nodos vistos
                nodos_vistos.add(actual.dato)
                anterior = actual
                actual = actual.siguiente

# Ejemplo de uso
lista1 = ListaEnlazada()
lista1.insertar_al_inicio(3)
lista1.insertar_al_inicio(7)
lista1.insertar_al_inicio(10)

lista2 = ListaEnlazada()
lista2.insertar_al_inicio(7)
lista2.insertar_al_inicio(20)
lista2.insertar_al_inicio(15)

# Concatenar listas
lista1.concatenar_listas(lista2)

# Eliminar duplicados
lista1.eliminar_duplicados()

# Imprimir la lista resultante
actual = lista1.cabeza
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente


#%%
"""=========================EJERCICIO 14======================================================
14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
Invertir Lista"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar_duplicados(self):
        nodos_vistos = set()
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato in nodos_vistos:
                # Eliminar el nodo actual
                anterior.siguiente = actual.siguiente
                actual = actual.siguiente
            else:
                # Agregar el dato al conjunto de nodos vistos
                nodos_vistos.add(actual.dato)
                anterior = actual
                actual = actual.siguiente

    def invertir_lista(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

# Ejemplo
lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(7)
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(7) 

# Eliminar duplicados
lista.eliminar_duplicados()
# Invertir la lista
lista.invertir_lista()
# Imprimir la lista resultante
actual = lista.cabeza
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente


#%%
"""=========================EJERCICIO 15======================================================
15. Implementa una función que invierta el orden de una lista enlazada simple."""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def invertir_lista(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior
lista = ListaEnlazada()
lista.insertar_al_inicio(1)
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(4)

print("Lista original:")
lista.imprimir_lista()

lista.invertir_lista()

print("Lista invertida:")
lista.imprimir_lista()

# %%
