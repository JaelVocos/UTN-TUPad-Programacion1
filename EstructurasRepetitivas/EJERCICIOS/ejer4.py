#Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0 #inicializo la suma en 0
numero = int(input("Ingrese un número entero (0 para finalizar): ")) #le pido al usuario que ingrese un numero y le informo que para finalizar el bucle ingrese 0


while numero != 0: # creo un bucle que se cumple solo si numero es distinto a 0
    suma += numero #aca sumamos el numero
    numero = int(input("Ingrese un número entero (0 para finalizar): ")) # y aca le pedimos al usuario que ingrese otro numero, y asi sucesivamente hasta que el usuario ingrese 0

print("El total acumulado es:", suma)
