"""
ESTRUCTURA DE DATOS FUNDAMENTALES Y ALGORITMOS
GUÍA DE LABORATORIO 10-11
LISTAS ENLAZADAS DOBLES Y PILAS

"""

"""
ejercicio parte 01  Listas Enlazadas Dobles:
Duplicar Nodos:
1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista 
duplicada hacia adelante y hacia atrás.
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def duplicar_nodos(self):
        actual = self.cabeza
        while actual:
            nuevo_nodo = Nodo(actual.dato)
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            if nuevo_nodo.siguiente:
                nuevo_nodo.siguiente.anterior = nuevo_nodo
            actual = nuevo_nodo.siguiente

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        while actual:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print()

# Crear la lista con al menos 4 nodos
lista = ListaDoblementeEnlazada()
lista.insertar_final(1)
lista.insertar_final(2)
lista.insertar_final(3)
lista.insertar_final(6)


lista.duplicar_nodos()

print("Lista Original hacia adelante:")
lista.imprimir_adelante()
print("Lista Original hacia atrás:")
lista.imprimir_atras()


#%%
"""
=================================================================================
Contar Nodos Pares e Impares:
2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato 
impar e imprime la lista hacia adelante y hacia atrás
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def contar_pares_impares(self):
        actual = self.cabeza
        contador_pares = 0
        contador_impares = 0
        while actual:
            if actual.dato % 2 == 0:
                contador_pares += 1
            else:
                contador_impares += 1
            actual = actual.siguiente
        return contador_pares, contador_impares

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        def imprimir_atras_util(nodo):
            if nodo:
                imprimir_atras_util(nodo.siguiente)
                print(nodo.dato, end=" -> ")
        imprimir_atras_util(self.cabeza)
        print("None")

# Creamos la lista enlazada
lista_enlazada = ListaEnlazada()
datos_lista = [3, 6, 9, 12, 15, 18, 21, 24, 27]
for dato in datos_lista:
    lista_enlazada.insertar(dato)

# Contamos nodos con datos pares e impares
contador_pares, contador_impares = lista_enlazada.contar_pares_impares()
print("Número de nodos con datos pares:", contador_pares)
print("Número de nodos con datos impares:", contador_impares)

# Imprimimos la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista_enlazada.imprimir_adelante()
print("Lista hacia atrás:")
lista_enlazada.imprimir_atras()

#%%
"""
=================================================================================
Insertar Nodo en Posición Específica:
3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la 
lista hacia adelante y hacia atrás.
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        if posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for _ in range(posicion - 1):
                if actual is None:
                    print("Posición fuera de rango")
                    return
                actual = actual.siguiente
            siguiente_nodo = actual.siguiente
            nuevo_nodo.siguiente = siguiente_nodo
            nuevo_nodo.anterior = actual
            if siguiente_nodo:
                siguiente_nodo.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print()

lista = ListaEnlazada()

for dato in [1, 2, 3, 4, 5]:
    lista.insertar_al_final(dato)
lista.insertar_en_posicion(15, 2)
print("Lista hacia adelante:")
lista.imprimir_adelante()

print("Lista hacia atrás:")
lista.imprimir_atras()

#%%
"""
=================================================================================
Eliminar Nodos Duplicados:
4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando 
solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
        self.cola = nuevo_nodo

    def eliminar_duplicados(self):
        nodos_vistos = set()
        actual = self.cabeza
        while actual:
            if actual.dato in nodos_vistos:
                # Eliminar el nodo actual
                anterior = actual.anterior
                siguiente = actual.siguiente
                if anterior:
                    anterior.siguiente = siguiente
                if siguiente:
                    siguiente.anterior = anterior
            else:
                # Agregar el dato al conjunto de nodos vistos
                nodos_vistos.add(actual.dato)
            actual = actual.siguiente

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print()

# Crear la lista con nodos duplicados
lista = ListaEnlazada()
datos = [3, 7, 2, 7, 5, 3, 9, 7]
for dato in datos:
    lista.insertar_al_final(dato)

# Imprimir la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:")
lista.imprimir_adelante()
print("Lista original hacia atrás:")
lista.imprimir_atras()

# Eliminar los nodos duplicados
lista.eliminar_duplicados()

print("Lista sin duplicados hacia adelante:")
lista.imprimir_adelante()
print("Lista sin duplicados hacia atrás:")
lista.imprimir_atras()


#%%
"""
=================================================================================
Invertir la Lista:
5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el 
primero y viceversa) e imprime la lista hacia adelante y hacia atrás.
"""
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

    def invertir_lista(self):
        anterior = None
        actual = self.cabeza
        siguiente = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        actual = self.cabeza
        anterior = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        while anterior:
            print(anterior.dato, end=" ")
            anterior = anterior.siguiente
        print()

# Crear la lista con al menos 6 nodos
lista = ListaEnlazada()
datos = [1, 2, 3, 4, 5, 6]
for dato in datos:
    lista.insertar_al_inicio(dato)

# Imprimir la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:")
lista.imprimir_adelante()
print("Lista original hacia atrás:")
lista.imprimir_atras()

# Invertir la lista
lista.invertir_lista()

# Imprimir la lista invertida hacia adelante y hacia atrás
print("Lista invertida hacia adelante:")
lista.imprimir_adelante()
print("Lista invertida hacia atrás:")
lista.imprimir_atras()

#%%
"""
=================================================================================
Invertir una cadena:
6. Utilizar una pila para invertir el orden de los caracteres de una cadena
"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def invertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)
    
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()
    
    return cadena_invertida

# Ejemplo 
cadena = "ingenieriaaaaa"
#llamamos a la funcion
cadena_invertida = invertir_cadena(cadena)
print("Cadena original:", cadena)
print("Cadena invertida:", cadena_invertida)

#%%
"""
=================================================================================
Convertir número decimal a binario:
7. Implementar un programa que convierta un número decimal a su representación en sistema binario 
utilizando una pila
"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def decimal_a_binario(numero_decimal):
    pila = Pila()
    while numero_decimal > 0:
        residuo = numero_decimal % 2
        pila.apilar(residuo)
        numero_decimal //= 2
    
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())
    
    return binario if binario else "0"

# Ejemplo 
numero_decimal = 50
binario = decimal_a_binario(numero_decimal)
print(f"El número decimal {numero_decimal} en binario es: {binario}")

#%%
"""
=================================================================================
Evaluar expresión posfija:
8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.
"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operandos = expresion.split()

    for token in operandos:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            if pila.esta_vacia():
                return "Expresión inválida: no hay suficientes operandos."
            
            segundo_operando = pila.desapilar()
            if pila.esta_vacia():
                return "Expresión inválida: no hay suficientes operandos."
            
            primer_operando = pila.desapilar()

            if token == '+':
                pila.apilar(primer_operando + segundo_operando)
            elif token == '-':
                pila.apilar(primer_operando - segundo_operando)
            elif token == '*':
                pila.apilar(primer_operando * segundo_operando)
            elif token == '/':
                if segundo_operando == 0:
                    return "Error: División por cero."
                pila.apilar(primer_operando / segundo_operando)
            else:
                return "Operador desconocido."
    
    if pila.esta_vacia():
        return "Expresión inválida: no hay suficientes operandos."
    
    resultado = pila.desapilar()
    if not pila.esta_vacia():
        return "Expresión inválida: hay operandos restantes."
    
    return resultado

# Ejemplo 
expresion = "5 3 + 2 *"
resultado = evaluar_expresion_posfija(expresion)
print(f"El resultado de la expresión '{expresion}' es: {resultado}")


#%%
"""
=================================================================================
Validar operadores anidados:
9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una 
pila.
"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def operadores_anidados(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter in "([{":
            pila.apilar(caracter)
        elif caracter in ")]}":
            if pila.esta_vacia():
                return False
            parentesis_abierto = pila.desapilar()
            if (caracter == ")" and parentesis_abierto != "(") or \
               (caracter == "]" and parentesis_abierto != "[") or \
               (caracter == "}" and parentesis_abierto != "{"):
                return False
    return pila.esta_vacia()

# Ejemplo
expresion1 = "(3 + 6) * (4 - 1)"
print(f"¿Los operadores en '{expresion1}' están correctamente anidados? {operadores_anidados(expresion1)}")



#%%
"""
=================================================================================
Validar operadores anidados:
Ordenar una pila:
10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.
"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

def ordenar_pila_ascendente(pila):
    pila_auxiliar = Pila()
    while not pila.esta_vacia():
        # Desapila un elemento de la pila original
        elemento = pila.desapilar()
        # Desapila elementos de la pila auxiliar hasta encontrar uno menor que el elemento actual
        while not pila_auxiliar.esta_vacia() and pila_auxiliar.ver_tope() > elemento:
            pila.apilar(pila_auxiliar.desapilar())
        # Apila el elemento en la pila auxiliar
        pila_auxiliar.apilar(elemento)
    # Desapila elementos de la pila auxiliar y apílalos en la pila original para obtener el orden ascendente
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

# Ejemplo 
pila = Pila()
elementos = [3, 1, 4, 1, 5, 9, 2, 6]
for elemento in elementos:
    pila.apilar(elemento)

print("Pila original:", pila.items)
ordenar_pila_ascendente(pila)
print("Pila ordenada de manera ascendente:", pila.items)


"""
=================================================================================
Eliminar duplicados:
11. Eliminar los elementos duplicados de una pila.
"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

def eliminar_elementos_duplicados(pila):
    pila_auxiliar = Pila()
    elementos_unicos = set()

    # Desapila elementos de la pila original y los apila en la pila auxiliar
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_unicos:
            pila_auxiliar.apilar(elemento)
            elementos_unicos.add(elemento)

    # Desapila elementos de la pila auxiliar y los apila en la pila original
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

# Ejemplo 
pila = Pila()
elementos = [3, 1, 4, 1, 5, 9, 2, 6, 3, 5,1,2,3,3,2,2,2,]
for elemento in elementos:
    pila.apilar(elemento)

print("Pila original:", pila.items)
eliminar_elementos_duplicados(pila)
print("Pila sin  duplica:", pila.items)


#%%
"""
=================================================================================
Implementar una calculadora sencilla:
12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar 
expresiones.
"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

def eliminar_elementos_duplicados(pila):
    pila_auxiliar = Pila()
    elementos_unicos = set()

    # Desapila elementos de la pila original y los apila en la pila auxiliar
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_unicos:
            pila_auxiliar.apilar(elemento)
            elementos_unicos.add(elemento)

    # Desapila elementos de la pila auxiliar y los apila en la pila original
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

# Ejemplo
pila = Pila()
elementos = [3, 1, 4, 1, 5, 9, 2, 6, 3, 5]
for elemento in elementos:
    pila.apilar(elemento)

print("Pila original:", pila.items)
eliminar_elementos_duplicados(pila)
print("Pila sin elementos duplicados:", pila.items)



#%%
"""
=================================================================================
Comprobar palíndromos:
13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo.
"""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def es_palindromo(cadena):
    # Eliminar caracteres no alfabéticos y convertir la cadena a minúsculas
    cadena = ''.join(c.lower() for c in cadena if c.isalpha())

    # Crear una pila y apilar la mitad de los caracteres
    longitud = len(cadena)
    pila = Pila()
    for i in range(longitud // 2):
        pila.apilar(cadena[i])

    # Desapilar y comparar con la segunda mitad de los caracteres
    for i in range(longitud // 2 + longitud % 2, longitud):
        if cadena[i] != pila.desapilar():
            return False
    
    return True

# Ejemplo
palabra = "me pica el "
print(f"¿'{palabra}' es un palíndromo?: {es_palindromo(palabra)}")


#%%
"""
=================================================================================
Simular el proceso de deshacer (undo):
14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los 
deshaceres.
"""
class SistemaDeshacer:
    def __init__(self):
        self.pila_acciones = []
        self.pila_deshaceres = []

    def realizar_accion(self, accion):
        self.pila_acciones.append(accion)
        # Limpiar la pila de deshaceres cuando se realiza una nueva acción
        self.pila_deshaceres = []

    def deshacer_accion(self):
        if self.pila_acciones:
            accion_deshacer = self.pila_acciones.pop()
            self.pila_deshaceres.append(accion_deshacer)
            return accion_deshacer
        else:
            return "No hay acciones para deshacer"

    def rehacer_accion(self):
        if self.pila_deshaceres:
            accion_rehacer = self.pila_deshaceres.pop()
            self.pila_acciones.append(accion_rehacer)
            return accion_rehacer
        else:
            return "No hay acciones para rehacer"

# Ejemplo de uso
sistema = SistemaDeshacer()

sistema.realizar_accion("Agregar elemento 1")
sistema.realizar_accion("Agregar elemento 2")
sistema.realizar_accion("Agregar elemento 3")

print("Acciones realizadas:", sistema.pila_acciones)
print("Deshacer la última acción:", sistema.deshacer_accion())
print("Acciones después de deshacer:", sistema.pila_acciones)
print("Deshacer la última acción:", sistema.deshacer_accion())
print("Acciones después de deshacer:", sistema.pila_acciones)
print("Rehacer la última acción deshecha:", sistema.rehacer_accion())
print("Acciones después de rehacer:", sistema.pila_acciones)



# %%
