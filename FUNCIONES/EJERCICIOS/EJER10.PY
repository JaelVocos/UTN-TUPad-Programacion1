#Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

#creamos una funcion llamada calcular promedio que recibe 3 notas como parametro
def calcular_promedio (a,b,c):
    #retorna el promedio de las 3 notas
    return (a + b + c) / 3

#le pide al usuario las 3 notas
a=float(input("Ingrese nota 1: "))
b= float(input("Ingrese nota 2: "))
c= float(input("Ingrese nota 3: "))

#llama a la funcion y guarda el valor en resultado
resultados = calcular_promedio(a,b,c)
print(f"El promedio es {resultados}")
