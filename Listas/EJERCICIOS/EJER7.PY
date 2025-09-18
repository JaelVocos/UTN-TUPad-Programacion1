#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#• Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.



temperatura = [
    [15,30],
    [20,32],
    [14,25],
    [15,28],
    [16,30],
    [10,20],
    [8,19]

]

#Recorre cada fila (dia) y toma la columna 0
minima = [fila[0]for fila in temperatura]
#Recorre cada fila y toma la columna 1
maxima = [fila[1] for fila in temperatura]

#calcula el promedio de la maxima y minima
prom_min = sum(minima)/len(minima) 
prom_max = sum(maxima)/len(maxima)

#Calcula la amplitud térmica diaria = máxima − mínima, para cada día.
amplitudes = [fila[1] - fila[0] for fila in temperatura]
#max() encuentra la mayor amplitud
dia_mayor_Amplitud = amplitudes.index(max(amplitudes))+1

print("El dia con mayor amplitud termica es el dia: ",dia_mayor_Amplitud)


