#) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#le pido al usuario que ingrese su edad
edad = int(input("ingrese edad: "))

#si edad es menor a 12, entonces muestra por pantalla, es niño
if edad < 12:
    print("es niño/a")
#si lo anterior no se cumple,pasa a la sig. condicion
#si edad es mayor o igual a 12 y edad es menor a 18,entonces es adolescente
elif edad >= 12 and edad < 18:
    print("es adolescente")
#si lo anterior no se cumple,pasa a la sig. condicion
#si edad es mayor o igual a 18 y edad es menor a 30, entonces es adulto joven
elif edad >= 18 and edad < 30:
    print("es adulto/a joven")
#si ninunguna de las anteriores se cumple, entonces termina en else con un mensaje en pantalla 
#es adulto
else:
    print("es adulto/a")


