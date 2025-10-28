#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique

# creamos una función recursiva que calcula el valor Fibonacci en la posición indicada
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# le pedimos al usuario que ingrese la posicion de la serie que desea ver
n = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

print(f"\nSerie de Fibonacci hasta la posición {n}:")
#recorre desde 0 hasta n e imprime cada término calculado por la función recursiva
for i in range(n + 1):
    print(f"F({i}) = {fibonacci(i)}")
