# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("ingrese su edad: "))

if edad >= 18:
    print ("es mayor de edad")
else:
    print ("es menor de edad")