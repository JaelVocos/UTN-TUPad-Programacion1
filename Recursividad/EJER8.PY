#Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

# creamos una función recursiva para contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    # Caso base: si el número llega a 0, ya no hay más dígitos que revisar
    if numero == 0:
        return 0
    else:
        # Tomamos el último dígito
        ultimo = numero % 10
        
        # Comparamos si coincide con el buscado
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# le pedimos al usuario que ingrese numero enter positivo y digito a buscar
num = int(input("Ingrese un número entero positivo: "))
d = int(input("Ingrese el dígito a buscar (0-9): "))

resultado = contar_digito(num, d)
print(f"El dígito {d} aparece {resultado} veces en el número {num}.")
