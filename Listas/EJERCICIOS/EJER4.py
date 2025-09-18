#Dada una lista con valores repetidos:
#datos = [1,3,5,3,7,1,9,5,3]
#• Crear una nueva lista
#  sin elementos repetidos.
#• Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]
print(datos)
#Aplico el metodo set que quita automaticamente los duplicados de la lista
N_datos = list(set(datos)) 

print ("La nueva lista sin datos repetidos es: ",N_datos)



