#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.


frasePalabra = input("ingrese frase o palabra: ")

if frasePalabra.lower().endswith(("a","e","i","o","u")):
    print(frasePalabra + "!")
else:
    print(frasePalabra)
