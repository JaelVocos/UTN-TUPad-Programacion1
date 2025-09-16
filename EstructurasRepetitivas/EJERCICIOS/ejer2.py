#Actividad 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("ingrese un numero: ")) #aca le pido al usuario que ingrese un numero. Int convierte el numero a entero

digitos = len(str(abs(numero))) #len(str) convierte el numero en cadena de texto y cuenta los digitos. Y abs(numero) permite contar 
                                #los digitos de los numero negativos.

print("El numero ingresado tiene ",digitos,"digitos")
