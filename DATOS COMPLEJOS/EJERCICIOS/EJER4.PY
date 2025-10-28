#Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

# Creamos un diccionario vacío para almacenar los contactos
contactos = {}

# le pedimos al usuario que cargue 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número telefónico de {nombre}: ")
    contactos[nombre] = numero  # Se guarda en el diccionario

# aca le pedimos al usuario que consulte un número
nombre_buscar = input("\nIngrese el nombre que desea buscar: ")

#creamos un if que si el nombre que ingreso el usuario esta en contactos entonces imprime el numero del nombre que se ingreso, sino imprime que no existe en la agenda
if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print("Ese contacto no existe en la agenda")
