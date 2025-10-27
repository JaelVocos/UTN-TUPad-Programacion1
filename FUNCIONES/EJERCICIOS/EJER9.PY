#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

#creamos una funcion llamada celsius_a_fahrenheit que recibe como parametro celsius
def celsius_a_fahrenheit(celsius):
    #hacemos la formula para convertir de celsius a fahrenheit
    return (celsius * 9 / 5) + 32

#pide al usuario que ingrese la temperatura en celsius
celsius = float(input("Ingrese temperatura en grados celsius: "))

#llama a la funcion y guarda el valor en resultado
resultados = celsius_a_fahrenheit(celsius)
print(f"La conversion de {celsius} grados celsius a fahrenheit es {resultados} grados fahrenheit")