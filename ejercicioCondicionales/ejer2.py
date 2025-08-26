# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

#aca le pido al usuario que ingrese la notad
nota = int(input("ingrese la nota: "))

#creo una condicional que dice, si nota es mayor o igual a 6,entonces muestra por pantalla un mensaje de aprobado
if nota >= 6:
    print("APROBADO")
#si no se cumple la condicion if, pasa a la condicion else, monstrando por pantalla desaprobado
else:
    print("DESAPROBADO")