# -*- coding: utf-8 -*-
"""
REPASOS DE PYTHON!!
cpaitulo 2
"""
"""
saber el conteo de una variable
"""
nombre = "chalo"
print(len(nombre))

######################

name = "perrita"
print(name[0][-1])

#%%
"""
"""
suma = 46 + 85
print(f"el resultado de la suma es : {suma}")

elevado = 10**5
print(f"el resultado es : {elevado}")
#%%
"""conversion de tipos de datos"""
numero1 = 1285.23
numero2 = 78874.7
print(int(numero1))
print(int(numero2))

#%%

num1 = int(input("ingrese el primer numero: "))
exponente = int(input("ingrese el exponente: "))

resultado = num1**exponente
print(resultado)
#%%
"""repaso de condicionales y anidados"""
edad = int(input("ingrese su edad: \n"))
respuesta = None

if edad >= 18:
    print("es mayor de eadad y puede tomar alcohol")
    respuesta = input("que desea tomar \n 1. pinga\n 2. agua\n 3. old times\n")
    if respuesta == "1":
        print(" quiere pinga")
    elif respuesta == "2":
        print("quiere agua")
    elif respuesta == "3":
        print("quiere old times")
    else:
        print("opcion invalida")
           
else:
    print("Es menor de edad y no puede tomar alcohol")



#%%
"""REPÁSO DE OPERADORES LOGICOS EN PYTHON """
"""AND - OR - NOT"""
color = "rojo"
forma = "circulo"    

if color == "rojo" and forma == "circulo":
    print("ta bien causa")
else:
    print("no cumple la condidicion")



#%%
"""repaso de match con case"""
error = input("introduzca un error de codigo: \n ")

match error:
    case "200":
        print("todo bien")
    case "300":
        print("Movimiento permanente de la pagina")
    case "404":
        print("pagina no encontrada")
    case _:
        print("no se encontro los datos necesarios")
        

#%%
"""REPASO DE CLASE LSITAS Y TUPLAS"""
#METODOS IMPORTANTES
""" saber cuantos 4 hay en la lista"""
numeros = [1,2,34,4311,23,3,2,4,4,12,3,2,3,4,4,4,4,4,]
print(numeros.count(4))


#para liminar de una lista

nombres_ejem = ["perrito", "zorra", "chupacabra", "lagarto"]
nombres_ejem.pop(0)
print(nombres_ejem)



#%%

nombres_ejem = ["perrito", "zorra", "chupacabra", "lagarto"]

for i in nombres_ejem:
    print(f"-{i}")

#%%
"""ESTAS LISTAS SE ORDENAN DE MENOR A MAYOR"""
numeros = [1,2,34,4311,23,3,2,4,4,12,3,2,3,4,4,4,4,4,]
numeros.sort()
print(numeros)

#%%
"""REPASO FUNCIONES"""
























