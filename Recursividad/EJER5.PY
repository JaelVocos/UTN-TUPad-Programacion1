#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es

#creamos una funcion para verificar si una cadena de texto es palindromo
def es_palindromo(palabra):
     # Caso base 1: una palabra vacía o de 1 letra siempre es palíndromo
    if len(palabra) <= 1:
        return True
    # Caso base 2: si la primera y la última letra son distintas, no es palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    # Caso recursivo: verificar el resto (sin la primera y la última letra)
    else:
        return es_palindromo(palabra[1:-1])

#le pedimos al usuario que ingrese una palabra sin espacios ni tildes y la convertimos en minusculas con lower
texto = input("Ingrese una palabra sin espacios ni tildes: ").lower()
#si es palindromo entonces muestra un mensaje diciendo "es un palindromo"
if es_palindromo(texto):
    print(f"'{texto}' es un palíndromo.")
else:
    #sino muestra que no lo es
    print(f"'{texto}' no es un palíndromo.")