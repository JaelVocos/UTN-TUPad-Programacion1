#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

#creamos una funcion llamada factorial 
def factorial(n):
    #si el numero es 0 o 1 retorna 1(caso base)
    if n == 0 or n == 1:
        return 1
    else:
        #sino el factorial se calcula como: n* factorial(n-1)
        return n * factorial(n - 1)

#le pide al usuario ingresar un numero
num = int(input("Ingrese un número entero: "))

print(f"\nFactoriales desde 1 hasta {num}:\n")

#creamos un bucle for. El range(1, num + 1) recorre desde 1 hasta el número indicado. En cada iteración, se llama a la función recursiva para calcular el factorial de i.
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

