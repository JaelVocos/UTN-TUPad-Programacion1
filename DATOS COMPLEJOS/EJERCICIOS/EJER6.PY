#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

# Creamos un diccionario vacío para guardar los alumnos y sus notas
alumnos = {}

# le pedimos al usuario que ingrese los datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    print(f"Ingrese las 3 notas de {nombre}:")
    
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    # Guardamos las notas en una tupla
    notas = (nota1, nota2, nota3)
    
    # Agregamos al diccionario los nombres y notas
    alumnos[nombre] = notas

# Mostramos el promedio de cada alumno
print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
