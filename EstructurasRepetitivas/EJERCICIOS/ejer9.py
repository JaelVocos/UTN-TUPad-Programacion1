#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

cantidad = 5

print(f"ingrese {cantidad} numeros enteros: ")

suma = 0
#agrego un bucle for que genera una secuencia de numeros de 0 a cantidad.
for i in range(cantidad):
    num = int(input(f"numero {i+1}: ")) #Cada repetición le pide un número al usuario, lo guarda en num, y luego se procesa.
    suma += num #acumulamos los valores en la variable suma

media = suma / cantidad #aca se calcula la media.Se divide la cantidad de numeros por la sumatoria de todos los numeros

print("\nResultados:")
print(f"media de los numeros: {media}")
    