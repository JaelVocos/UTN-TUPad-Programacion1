#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

# creamos una función recursiva que suma los dígitos de un número entero positivo
def suma_digitos(n):
    if n < 10: #Si n es un solo dígito (menor que 10), devuelve ese número.
        return n
    else:
        return (n % 10) + suma_digitos(n // 10) #n % 10 obtiene el último dígito del número. n // 10 elimina el último dígito. Luego suma el último dígito con el resultado de llamar a la función sobre el resto del número.

#le pide al usuario que ingrese un numero positivo
num = int(input("Ingrese un número entero positivo: "))

resultado = suma_digitos(num)
print(f"La suma de los dígitos de {num} es: {resultado}")
