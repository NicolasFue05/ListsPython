# METODOS MAS UTILIZADOS PARA LAS LISTAS
#------------------------------------------------
# [1] Agregar un elemento al final de la lista 
# .append(elemento)
#--------------------------------------------
lista = ["a", "a", "b", "b", "c", "D", "E", "F", "G"]

elemento = "h"                             
lista.append(elemento)
print(lista)
#-----------------------------------------------------------------------------------
# [2] Amplia la lista utilizando todos los elementos del iterable (Lista o Tupla)
# .extend(iterable)
#--------------------------
iterable = [1, 2, 3, 4, 5]
lista.extend(iterable)     
print(lista)              
#--------------------------
# [3] Inserta un elemento (x) en una posicion determinada
# .insert(posicion, elemento)
#----------------------------
posicion = 8
x = 0
lista.insert(posicion,x) 
print(lista)
#---------------------------
# [4] Eliminar el primero elemento de la lista cuyo valor sea igual a x
# .remove(x)
#----------------
x = "a"
lista.remove(x)
print(lista) 
#-----------------
# [5] Quitar un elemento en una posicion dada de la lista y retorna ese elemento, si no se le especifica uno se elimina el ultimo valor de la lista
# .pop(posicion)
#------------------
posicion = 1
lista.pop(posicion)
print(lista)
#------------------
# [6] Para borrar todos los elementos de la lista
# .clear()
#--------------
lista.clear() 
print(lista)
#--------------
# [7] devuelve el numero de veces que aparece un elemento en la lista
# .count(elemento)
#-----------------
lista2 = ["a", "b", "b", "b", "c", "d"]
elemento = "b"
print(lista2.count(elemento))
#---------------------------------------
# [8] Ordena los elementos de la lista de forma ascendente
# .sort()
#------------------------------------------
lista_desordenada = [4,2,1,6,9,0,5,7,8,3]
lista_desordenada.sort()
print(lista_desordenada)
#--------------------------
# [9] Invierte los elementos de la lista
# .reverse()
#-------------
lista_desordenada.reverse()
print(lista_desordenada)
#---------------------------
# [10] Devuelve True or False si el elemento esta en la lista
# (in)
#--------------------
elemento = 9
if elemento in lista_desordenada:
    print("El elemento se encuentra en la lista")
else:
    print("El elemento no se encuentra en la lista") 
#-----------------------------------------------------
# [11] Devuelve True si dos variables (listas) se refieren al mismo objeto en memoria
#-------------------
lista3 = lista_desordenada 
if lista3 is lista_desordenada:
    print("Esta en la misma referencia de memoria")
else:
    print("No esta en la misma referencia de memoria")  
#-------------------------------------------------------
# [12] Devuelve True si un elemento es verdadero y False si todos los elementos son falsos
#-----------------------
if any(lista_desordenada):
    print("Al menos un elemento es verdadero")
else:
    print("Todos los elementos son falsos")
#----------------------------
# [13] Devolver una copia superficial de una lista
# .copy()
#---------------------------
lista_copia = lista.copy()
print()
#---------------------------------
# [14] Separa una cadena a una lista indicando por que elemento se separara (comunmente ",")
# .split(elemeto a separar)
#------------------------------------
elementos = "Azul,Rojo,Amarillo,Naranja"
lista = elementos.split(",")
print(lista)