#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for i in range(len(asignaturas)):
    nota = int(input((f"Ingresa la nota que sacaste en: {asignaturas[i]}: ")))
    notas.append(nota)
print("Asignaturas:")
for j in range(len(asignaturas)):
    print(f"{asignaturas[j]} has sacado: {notas[j]}")
