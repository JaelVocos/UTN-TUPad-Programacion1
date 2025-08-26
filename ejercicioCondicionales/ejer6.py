# escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import statistics as stats
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = stats.mean(numeros_aleatorios)
mediana = stats.median(numeros_aleatorios)
moda = stats.mode(numeros_aleatorios)


print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)


if media > mediana > moda:
    print("tiene sesgo positivo")
elif media < mediana < moda:
    print("tiene sesgo negativo")
else:
    print("sin sesgo")