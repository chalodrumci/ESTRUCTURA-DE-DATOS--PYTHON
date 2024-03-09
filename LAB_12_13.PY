

"""ESTRUCTURA DE DATOS FUNDAMENTALES Y ALGORITMOS
                                                GUÍA DE LABORATORIO 12-13
                                                COLAS Y ARBOLES"""

#%%
"""Ejercicio parte 01 Colas:
Verificar si una palabra es palíndroma
1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para 
comparar los caracteres de la palabra en orden original y reverso."""

from collections import deque
def es_palindromo(palabra):
    # Convertir la palabra a minúsculas y eliminar espacios para eso
    #usamos Lower que es convierte en minusculas
    palabra = palabra.lower().replace(" ", "")
    cola = deque(palabra)
    palabra_inversa = palabra[::-1]
    # Comparar cada caracter de la palabra con el caracter correspondiente en la cadena inversa
    while cola:
        if cola.popleft() != palabra_inversa[len(palabra) - len(cola) - 1]:
            return False
    return True

# Ejemplo 
palabra = "lala"
print(f"¿'{palabra}' es un palíndromo?: {es_palindromo(palabra)}")


#%%
"""Diseño de un sistema de gestión de pedidos
2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que 
fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado 
actual de la cola."""
from collections import deque
#creamos la estructura
class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)
        print(f"Pedido '{pedido}' agregado.")

    def procesar_pedido(self):
        if self.cola_pedidos:
            pedido = self.cola_pedidos.popleft()
            print(f"Procesando pedido: {pedido}")
        else:
            print("No hay pedidos para procesar.")

    def mostrar_estado(self):
        if self.cola_pedidos:
            print("Estado de la cola de pedidos:")
            for idx, pedido in enumerate(self.cola_pedidos, start=1):
                print(f"{idx}. {pedido}")
        else:
            print("La cola de pedidos está vacía.")

# Ejemplo de uso
sistema_pedidos = SistemaGestionPedidos()

sistema_pedidos.agregar_pedido("Café")
sistema_pedidos.agregar_pedido("Té")
sistema_pedidos.agregar_pedido("Jugo de naranja")

sistema_pedidos.mostrar_estado()

sistema_pedidos.procesar_pedido()
sistema_pedidos.procesar_pedido()

sistema_pedidos.mostrar_estado()

sistema_pedidos.agregar_pedido("Pastel de chocolate")
sistema_pedidos.agregar_pedido("Galletas")

sistema_pedidos.mostrar_estado()

sistema_pedidos.procesar_pedido()
sistema_pedidos.procesar_pedido()

sistema_pedidos.mostrar_estado()



"""Búsqueda de rutas en un laberinto
3. Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola 
para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.
Diseño de un sistema de gestión de tareas (Avanzado)"""

#%%
"""4. Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como 
completadas y mostrar la próxima tarea pendiente."""
from collections import deque

class SistemaGestionTareas:
    def __init__(self):
        self.cola_tareas = deque()

    def agregar_tarea(self, tarea):
        self.cola_tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def marcar_completada(self):
        if self.cola_tareas:
            tarea_completada = self.cola_tareas.popleft()
            print(f"Tarea '{tarea_completada}' marcada como completada.")
        else:
            print("No hay tareas pendientes.")

    def mostrar_proxima_tarea(self):
        if self.cola_tareas:
            print("Próxima tarea pendiente:", self.cola_tareas[0])
        else:
            print("No hay tareas pendientes.")

# Ejemplo de uso
sistema_tareas = SistemaGestionTareas()

sistema_tareas.agregar_tarea("Lavar la ropa")
sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Preparar la cena")

sistema_tareas.mostrar_proxima_tarea()

sistema_tareas.marcar_completada()
sistema_tareas.mostrar_proxima_tarea()

sistema_tareas.marcar_completada()
sistema_tareas.mostrar_proxima_tarea()

sistema_tareas.marcar_completada()
sistema_tareas.mostrar_proxima_tarea()


"""Ejercicios parte 02 - Arboles:
Contar nodos:"""

"""5. Implementar una función que cuente la cantidad de nodos en el árbol."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = [] #vacio

def cantidad_nodos(arbol):
    if arbol is None:
        return 0
    else:
        contador = 1  # Contador para incluir el nodo actual
        for hijo in arbol.hijos:
            contador += cantidad_nodos(hijo)  # Recursivamente contar los nodos de los hijos
        return contador


# Creamos un árbol de ejemplo
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]
nodo3.hijos = [nodo6]

# Llamamos a la función para contar los nodos
cantidad = cantidad_nodos(nodo1)
print("La cantidad de nodos en el árbol es:", cantidad)


#%%
"""6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos)."""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_hoja(arbol):
    # Caso base: si el nodo es nulo, retorna 0
    if arbol is None:
        return 0
    # Caso base: si el nodo no tiene hijos, es un nodo hoja, retorna 1
    elif not arbol.hijos:
        return 1
    else:
        # Caso recursivo: suma la cantidad de nodos hoja de cada hijo
        return sum(contar_nodos_hoja(hijo) for hijo in arbol.hijos)
# Creamos un árbol de ejemplo
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]
nodo3.hijos = [nodo6]

# Contamos la cantidad de nodos hoja
cantidad_nodos_hoja = contar_nodos_hoja(nodo1)
print("La cantidad de nodos hoja en el árbol es:", cantidad_nodos_hoja)


"""7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).
Calcular altura y profundidad:"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_internos(arbol):
    if arbol is None or not arbol.hijos:
        return 0
    else:
        cantidad_nodos_internos = 1  # Contador para incluir el nodo actual si es interno
        for hijo in arbol.hijos:
            cantidad_nodos_internos += contar_nodos_internos(hijo)
        return cantidad_nodos_internos

def calcular_altura(arbol):
    if arbol is None:
        return 0
    elif not arbol.hijos:
        return 0
    else:
        altura_subarboles = [calcular_altura(hijo) for hijo in arbol.hijos]
        return 1 + max(altura_subarboles)

def calcular_profundidad(arbol):
    if arbol is None:
        return 0
    else:
        profundidad_padre = 0
        if arbol.hijos:
            profundidad_subarboles = [calcular_profundidad(hijo) for hijo in arbol.hijos]
            profundidad_padre = 1 + max(profundidad_subarboles)
        return profundidad_padre

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]
nodo3.hijos = [nodo6]

# Contamos la cantidad de nodos internos
cantidad_nodos_internos = contar_nodos_internos(nodo1)
print("La cantidad de nodos internos en el árbol es:", cantidad_nodos_internos)
# Calculamos la altura del árbol
altura_arbol = calcular_altura(nodo1)
print("La altura del árbol es:", altura_arbol)
# Calculamos la profundidad del árbol
profundidad_arbol = calcular_profundidad(nodo1)
print("La profundidad del árbol es:", profundidad_arbol)


#%%
"""8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz 
hasta una hoja)."""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def calcular_altura(arbol):
    if arbol is None:
        return 0  # Si el árbol es nulo, su altura es 0
    elif not arbol.hijos:
        return 0  # Si el nodo no tiene hijos, su altura es 0
    else:
        # Calculamos la altura de cada hijo recursivamente
        altura_subarboles = [calcular_altura(hijo) for hijo in arbol.hijos]
        # La altura del árbol es la máxima altura de sus subárboles más 1 (para contar la raíz)
        return 1 + max(altura_subarboles)

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]
nodo3.hijos = [nodo6]

# Calculamos la altura del árbol
altura_arbol = calcular_altura(nodo1)
print("La altura del árbol es:", altura_arbol)



#%%
"""9. Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz 
hasta el nodo)."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
#creamos una funcion para saber la profundidad de un nodo
def calcular_profundidad(arbol, valor_nodo, profundidad_actual=0):
    if arbol is None:
        return None  # Si el árbol es nulo, retorna None
    elif arbol.valor == valor_nodo: #comparamos el valor 
        return profundidad_actual  # Si encontramos el nodo, retorna la profundidad actual
    else:
        # Buscamos el nodo en los hijos del árbol
        for hijo in arbol.hijos:
            profundidad_nodo = calcular_profundidad(hijo, valor_nodo, profundidad_actual + 1)
            if profundidad_nodo is not None:
                return profundidad_nodo  # Si encontramos el nodo en alguno de los hijos, retornamos su profundidad
        return None  # Si no encontramos el nodo en ningún hijo, retornamos None

# Ejemplo de uso
# Creamos un árbol de ejemplo
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]
nodo3.hijos = [nodo6]

# Calculamos la profundidad del nodo 4
profundidad_nodo_4 = calcular_profundidad(nodo1, 4)
print("La profundidad del nodo 4 es:", profundidad_nodo_4)
# Calculamos la profundidad del nodo 6
profundidad_nodo_6 = calcular_profundidad(nodo1, 6)
print("La profundidad del nodo 6 es:", profundidad_nodo_6)


#%%
"""Buscar el mínimo y el máximo:
10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol."""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_valor_minimo(arbol):
    if arbol is None:
        return float('inf')  # Retorna el mayor valor posible para iniciar la búsqueda
    else:
        minimo_actual = arbol.valor
        for hijo in arbol.hijos:
            minimo_actual = min(minimo_actual, encontrar_valor_minimo(hijo))
        return minimo_actual
nodo1 = Nodo(10)
nodo2 = Nodo(5)
nodo3 = Nodo(30)
nodo4 = Nodo(40)
nodo5 = Nodo(3)
nodo6 = Nodo(60)

nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]
nodo3.hijos = [nodo6]

minimo_valor = encontrar_valor_minimo(nodo1)
print("El valor mínimo en el árbol es:", minimo_valor)


#%%
"""11. Implementar una función que encuentre el nodo con el valor máximo en el árbol."""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_valor_maximo(arbol):
    if arbol is None:
        return float('-inf')  # Retorna el menor valor posible para iniciar la búsqueda
    else:
        maximo_actual = arbol.valor
        for hijo in arbol.hijos:
            maximo_actual = max(maximo_actual, encontrar_valor_maximo(hijo))
        return maximo_actual
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)
nodo5 = Nodo(50)
nodo6 = Nodo(60)

nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]
nodo3.hijos = [nodo6]

# Encontramos el valor máximo en el árbol
maximo_valor = encontrar_valor_maximo(nodo1)
print("El valor máximo en el árbol es:", maximo_valor)
