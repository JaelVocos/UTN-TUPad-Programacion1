#Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

#pide una frase al usuario
frase = input("Ingrese una frase: ")

#separa las palabras
palabras = frase.split()

#aca obtenemos las palabras unicas con set
palabras_unicas = set(palabras)
print("palabras unicas: ")
print(palabras_unicas)

#creamos un diccionario con el conteo de cada palabra
cant_veces = {}

for palabra in palabras:
    if palabra in cant_veces:
        cant_veces[palabra] += 1
    else:
        cant_veces[palabra] = 1

print("\nCantidad de veces que aparece las palabras:")
print(cant_veces)
