#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media.

muestra = input("Ingresa una muestra de numeros separados por coma: ")

numeros = [float(numero) for numero in muestra.split(",")]

media = sum(numeros) / len(numeros)

print(f"La media de los numeros es: {media}") 