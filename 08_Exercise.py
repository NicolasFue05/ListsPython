#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Ingrese una palabra: ")
palabra = palabra.lower() 
recuento_de_vocales = []
for letra in palabra: 
    if letra in "aeiou":
        recuento_de_vocales.append(letra)

for i in range(len(recuento_de_vocales)):
    print(f"la vocal {recuento_de_vocales[i]} se encuentra: {recuento_de_vocales.count(recuento_de_vocales[i])} vez")     