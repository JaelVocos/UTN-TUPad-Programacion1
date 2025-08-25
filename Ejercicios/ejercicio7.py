#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("ingrese un numero que no sea 0: "))
num2 =int(input("ingrese otro numero que no sea 0: "))

suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2

print(f"la suma de ambos numeros es {suma}")
print(f"la division de ambos numeros es {division}")
print(f"la multiplicacion de ambos numeros es {multiplicacion}")
print(f"la resta de ambos numeros es {resta}")
