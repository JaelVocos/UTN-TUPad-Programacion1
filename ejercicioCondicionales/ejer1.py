# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#aca le pido al usuario que ingrese su edad,poniendo int para que el numero que ingrese el usuario sea entero
edad = int(input("ingrese su edad: "))

#aca creo una condicional donde dice que si edad es mayor o igual a 18,entonces va a aparecer un
#mensaje en pantalla diciendo "es mayor de edad"
if edad >= 18:
    print ("es mayor de edad")
#si no se cumple la condicion if, pasa a la linea 11 mostando por pantalla "es menor de edad"
else:
    print ("es menor de edad")