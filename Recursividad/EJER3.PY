#Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛
#𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

# creamos una función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1
    else:
        return base * potencia(base, exponente - 1)  # Caso recursivo

#le pedimos al usuario que ingrese la base y el exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

#guarda los valores ingresados en la variable resultado
resultado = potencia(base, exponente)

print(f"\n{base} elevado a la {exponente} es: {resultado}")
