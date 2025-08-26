# escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

#la linea 6 nos va a permitir calcular media,mediana y moda
import statistics as stats
#aca importamos el modulo random para generar numeros aleatorios
import random

#el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = stats.mean(numeros_aleatorios)#aca calcula la media, y guarda el resultado en la variable media
mediana = stats.median(numeros_aleatorios)#calcula la mediana y lo guarda en la variable mediana
moda = stats.mode(numeros_aleatorios)#calcula la moda y lo guarda en la variable moda


print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

#si media es mayor a mediana y mediana mayor a moda entonces, tiene sesgo positivo
if media > mediana > moda:
    print("tiene sesgo positivo")
#si media es menor a mediana y mediana es menor a moda entonces,tiene sesgo negativo
elif media < mediana < moda:
    print("tiene sesgo negativo")
#sino se cumplen las anteriores se considera sin sesgo
else:
    print("sin sesgo")