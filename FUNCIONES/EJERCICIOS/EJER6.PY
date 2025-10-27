#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#definimos una funcion llamada tabla_multiplicar que recibe numero como parametro, que va a ser ingresado por el usuario

def tabla_multiplicar(numero):
    #imprime la tabla de multiplicar del número que el usuario ingresa, recorriendo los valores del 1 al 10 mediante un bucle for.
    for i in range (1,11):
         print(numero, "x", i, "=", numero * i)

#le pide al usuario un numero
num = int(input("Ingresa un número: "))
#llama a la funcion
tabla_multiplicar(num)
