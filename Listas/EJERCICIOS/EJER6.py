#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

numeros  = [2,3,8,6,4,7,9]

print("LISTA DE NUMEROS")
print(numeros)


# numeros[-1] agarra el último. numeros[:-1] agarra todos menos el último. Se suman (+) como listas  formando la lista rotada.
rotada = [numeros[-1]] + numeros[:-1]

print("Lista original:", numeros)
print("Lista rotada:", rotada)

