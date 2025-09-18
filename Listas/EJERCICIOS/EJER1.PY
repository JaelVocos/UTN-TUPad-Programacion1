#Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
# Indicar la nota más alta y la más baja


#creo una lista con las notas de 10 estudiantes
notas = [4,5.6,8,9,10,4.5,2,8.5,3,7]

#aca muestro la lista completa
print("Notas de los estudiantes: ",notas)

#calculo el promedio, sumando las notas con sum y dividiendolas por la cantidad de notas con len
promedio = sum(notas) / len(notas)

#muestro el promedio de todas las notas
print("el promedio es de: ",promedio)

#aca buscamos con max y min los valores mas altos y mas bajos de la lista notas
nota_min = min(notas)
nota_max= max(notas)

#por ultimo mostramos la nota mas alta y mas baja
print(f"La nota mas alta es {nota_max} y la mas baja es {nota_min}")