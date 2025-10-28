#Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.


# creamos una función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0: #si el n es igual a 0 su repressentacion binaria es esa cadena
        return "0"
    elif n == 1: #si n es igual a 1 su binario es 1 
        return "1"
    else:
        #Llama recursivamente a decimal_a_binario(n // 2) para convertir el cociente y concatena al final el resto convertido a texto con str(n % 2).
        return decimal_a_binario(n // 2) + str(n % 2)

# le pedimos al usuario ingresar un numero entero positivo
num = int(input("Ingrese un número entero positivo: "))

#si el numero ingresado no es positivo, muestra un mensaje pidiendole al usuario ingresar un  numero positivo
if num < 0:
    print("Por favor, ingrese un número positivo.")
else:
    binario = decimal_a_binario(num)
    print(f"El número {num} en binario es: {binario}")
