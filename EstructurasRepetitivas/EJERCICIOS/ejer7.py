#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#le pedimos al usuario que ingrese un numero positivo
numero = int(input("Ingrese un numero positivo: "))

#inicializamos la suma en 0
suma = 0

#la condicion if nos dice que si el numero que ingreso el usuario es negativo, le pide al usuario que ingrese un numero positivo
if numero <0:
        print("ingrese numero positivo")
else: #aca si la condicion if es falsa pasa a el bucle for.
    for i in range(0,numero): #aca range suma los numeros comprendidos entre el 0 y el numero que ingresa el usuario como valor final.
        suma +=i #aca se va guardando el nuevo valor de suma
    print("la suma de los numeros entre 0 y",numero,"es: ",suma)
