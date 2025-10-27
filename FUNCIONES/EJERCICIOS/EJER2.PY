#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario

#creo una funcion llamada saludar_usuario que recibe como parametro un nombre que ingrese el usuario y devuelve un saludo personalizado
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#aca le pide al usuario que ingrese un nombre
nombre = input("Ingrese su nombre: ")
#Y por ultimo llama a la funcion 
saludar_usuario(nombre)