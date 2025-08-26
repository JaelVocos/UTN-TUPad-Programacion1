#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.


frasePalabra = input("ingrese frase o palabra: ")

#aca convertimos la palabra o frase que ingresa el usuario a minusculas con lower
#use el metodo endswith para verificar si la cadena de texto termina con vocal, si es asi imprime al final de la cadena un signo de exclamacion
if frasePalabra.lower().endswith(("a","e","i","o","u")):
    print(frasePalabra + "!")
else:
    print(frasePalabra)
