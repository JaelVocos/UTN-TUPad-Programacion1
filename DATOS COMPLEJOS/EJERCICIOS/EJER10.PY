#Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

#creamos un diccionario con clave pais y valor capital
paises = {'Argentina': 'Buenos Aires','Peru': 'Lima','Uruguay': 'Montevideo'}

#imprimo el diccionario paises
print(paises)
#creamos otro diccionario para invertir 
capitales = {}

#con el bucle for se recorren los pares del diccionario original y se intercambian las posiciones
for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario invertido (capital -> país):")
print(capitales)