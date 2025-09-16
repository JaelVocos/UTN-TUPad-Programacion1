#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


numeros = int(input("ingresa un numero: "))


if numeros > 0:
        invertido = int(str(numeros)[::-1])  #str(numeros) lo convierte a cadena.[::-1] invierte la cadena.Int()devuelve el numero invertido

print(f"Número original: {numeros}  →  Invertido: {invertido}")