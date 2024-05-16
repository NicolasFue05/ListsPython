#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista para almacenar las asignaturas a repetir
asignaturas_a_repetir = []

# Preguntar la nota de cada asignatura y eliminar las aprobadas de la lista
for asignatura in asignaturas:
    nota = float(input("Ingrese la nota de {}: ".format(asignatura)))
    if nota < 5.0:  # Si la nota es menor que 5.0, la asignatura se agrega a la lista de repetición
        asignaturas_a_repetir.append(asignatura)

# Mostrar las asignaturas que el usuario tiene que repetir
print("\nLas asignaturas que debes repetir son:")
for asignatura in asignaturas_a_repetir:
    print(asignatura)
