#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#creo una funcion llamada informacion_personal que recibe como parametro un nombre,apellido,edad y residencia que el usuario debe ingresar el usuario 
#e imprime una oracion concatenando todos los datos ingresados.

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#le pedimos al usuario todos los datos requeridos
nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad= input("ingrese su edad: ")
residencia=input("ingrese su lugar de residencia: ")

#llamamos a la funcion
informacion_personal(nombre,apellido,edad,residencia)
