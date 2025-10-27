#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#importamos la funcion math para poder utilizar pi
import math
#definimos una funcion que recibe radio como parametro, que va a ser ingresado por el usuario
def calcular_area_circulo(radio):
    #calculamos el area del circulo
    return math.pi * (radio **2)

#definimos otra funcion que tambien recibe radio como parametro
def calcular_perimetro_circulo(radio):
    #hacemos el calculo del perimetro de un circulo
    return 2 * math.pi * radio

#aca le pedimos al usuario que ingrese el numero del radio
radio = float(input("Ingresa el radio del círculo: "))

#aca llama a las funciones y guardamos los resultados en las variables area y perimetro
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

#imprimimos un mensaje por pantalla los resultados
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)


