#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.


nombre = input("ingrese su nombre: ")

print("elegi una opcion:")
print("1.Si queres tu nombre en mayusculas")
print("2.Si queres tu nombre en minusculas")
print("3.Si queres tu nombre con la primera letra mayuscula")

#aca le damos al usuario que ingrese las opciones 1,2,3 mostradas en pantalla anteriormente
opcion = int(input("ingrese opcion 1,2,3: "))

if opcion == 1:
    print(nombre.upper()) #upper convierte el nombre en mayusculas
elif opcion == 2 :
    print(nombre.lower()) #lower convierte el nombre en minusculas
elif opcion == 3:
    print(nombre.title()) #y title convierte la inicial del nombre en mayuscula
else:
    print("ingrese una opcion valida")
