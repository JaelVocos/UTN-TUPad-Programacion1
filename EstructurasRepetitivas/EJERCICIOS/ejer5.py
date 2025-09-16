#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random #esto lo que hace es importar modulos para generar numeros aleatorios

numer_aleatorio = random.randint(0,9) #generamos un numero aleatorio del 0 al 9

#inicializamos intentos e intento
intentos = 0 
intento = -1

#este bucle se cumple hasta que el usuario adivine el numero aleatorio
while intento != numer_aleatorio:
    intento = int(input("adivina el numero entre 0 y 9: ")) #le pide al usuario ingresar un numero entre 0 y 9
    intentos += 1 #suma 1 al numero de intentos

    #si no acierta, aparece por pantalla el mensaje de incorrecto y el bucle vuelve a empezar
    if intento != numer_aleatorio:
        print("incorrecto, intenta de nuevo")

print("Perfecto! adivinaste el numero en",intentos,"intentos")
