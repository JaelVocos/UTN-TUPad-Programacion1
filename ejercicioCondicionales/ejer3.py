# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

#le pido al usuario que ingrese un numero par
numPar = int(input("ingrese un numero par: "))

#creo una condicion que dice, si el modulo numPar es 0, entonces muestra por pantalla
#ha ingresado un numero par
if numPar % 2==0:
    print("ha ingresado un numero par")
#si no se cumple la condicion if, muestra por pantalla el mensaje
#por favor,ingrese un numero par
else:
    print("por favor, ingrese un numero par")
