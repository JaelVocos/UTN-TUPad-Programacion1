#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

#creamos una función recursiva para contar el total de bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1  # Caso base: una sola fila tiene un solo bloque
    else:
        return n + contar_bloques(n - 1)  # Caso recursivo

# le pedimos al usuario que ingrese l cantidad de bloques mas bajo
nivel = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
total = contar_bloques(nivel)
print(f"Total de bloques necesarios: {total}")
