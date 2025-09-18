# Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

#importa numeros random
import random

#crea una lista vacia
num_aleatorio = []

#el bucle permite iterar hasta 15 numeros
for i in range(15):
    n = random.randint(1,100) #genera numeros enteros al azar entre 1 y 100
    num_aleatorio.append(n) #guarda los nuemeros generados en la lista num _aleatorios

#muestra la lista de numeros aleatorios 
print(num_aleatorio)

#inicializo las listas par e impar vacias
par = []
impar = []

#el bucle for lo que hace es que por cada numero que se genera al azar en la lista num_aleatorio, analiza si es par o impar
for n in num_aleatorio:
    if n % 2 == 0:
        par.append(n) #si es par, actualiza la lista par 
    else:
        impar.append(n) #si es impar, se actualiza la lista impar


print(f"Todos los números: {num_aleatorio}") #muestra todos numeros
print(f"Pares ({len(par)}): {par}") #muestra la cantidad de numeros pares
print(f"Impares ({len(impar)}): {impar}") #muestra la cantidad de numeros impares
print(f"Total comprobación: {len(par) + len(impar)}") #muestra la cantidad de los numeros al azar, para comprobar si se cumplio el bucle for qeue hicimos al principio
