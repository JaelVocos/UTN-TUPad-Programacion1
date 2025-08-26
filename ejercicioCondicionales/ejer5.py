#) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("ingrese su contraseña: ")

#aca uso len para obtener la cantidad de letras de la palabra que ingresa el usuario
#si contraseña es mayor o igual a 8 y contraseña es menor o igual a 14 entonces muestra por pantalla 
#ha ingresado la contrasela correcta
if len(contraseña)>=8 and len(contraseña)<=14:
    print("Ha ingresado la contraseña correcta!")
#sino muestra contraseña incorrecta
else:
    print ("contraseña incorrecta")
