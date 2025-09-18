#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia.#

notas = [
    [3,6,4],
    [6,8,5],
    [7,9,4],
    [1,4,3],
    [5,10,8]

]

#Recorre los índices de las filas (0 a 4).
for i in range(len(notas)):   
    fila = notas[i] #Toma la fila i (las 3 notas del estudiante)
    prom_est = sum(fila) / len(fila) #calcula el promedio sumando los numeros de la fila y los divide por la cantidad de notas de la fila.
    print("Estudiante", i+1, ":", prom_est) #Muestra el promedio

# -------------------------------
# Promedio de cada materia
materias = len(notas[0])  #Determina cuántas materias hay contando las columnas de la primera fila          
for j in range(materias): # recorre columnas
    suma = 0
    for i in range(len(notas)):  #Recorre todas las filas y va sumando la nota de la columna j en cada estudiante.
        suma += notas[i][j] 
        
    #Calcula el promedio de la materia j: divide la suma por la cantidad de estudiantes.
    prom_mat = suma / len(notas)
    print("Materia", j+1, ":", prom_mat)