#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
n = input("Ingresa una palabra: ")
if n == n[::-1]:
    print("La palabra es un polidromo")
else:
    print("La palabra no es un polidromo")