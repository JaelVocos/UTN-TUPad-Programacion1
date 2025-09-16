#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#cantidad de numeros a ingresar
cantidad = 100

#inicializamos par, impar,negativo y positivo en 0
par = 0
impar = 0
negativo = 0
positivo = 0


#le pedimos al usuario que ingrese 100 numeros enteros
print(f"ingrese {cantidad} numeros enteros: ")

#agrego un bucle for que genera una secuencia de numeros de 0 a cantidad.
for i in range(cantidad):
    num = int(input(f"numero {i+1}: ")) #Cada repetición le pide un número al usuario, lo guarda en num, y luego se procesa.
    
    if num %2 ==0: #aca verificamos si el numero es par.Si lo es, se suma uno en la variable par
        par +=1
    else: #si lo anterior no se cumple, se suma 1 en la variable impar
        impar += 1

    if num > 0: #aca verificamos si el numero es positivo. Si lo es, se suma uno a la variable positivo
        positivo +=1
    elif num <0: #si no es positivo, se suma uno en la variable negativo
        negativo += 1

# Mostrar resultados
print("\nResultados:")
print(f"Pares: {par}")
print(f"Impares: {impar}")
print(f"Positivos: {positivo}")
print(f"Negativos: {negativo}")


