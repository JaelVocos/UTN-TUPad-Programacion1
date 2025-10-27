#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

#crea una funcion llamada operaciones_basicas que recibe como parametro 2 numeros y devuelve una tupla con operaciones basicas
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicar = a * b
    dividir = a / b
    return suma,resta,multiplicar,dividir

#le pide al usuario 2 numeros
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

#llama a la funcion y guarda el valor en la variable resultados
resultado = operaciones_basicas(num1,num2)

#imprime los resultados linea por linea
print("Resultados:")
print("Suma:", resultado[0])
print("Resta:", resultado[1])
print("Multiplicación:", resultado[2])
print("División:", resultado[3])

