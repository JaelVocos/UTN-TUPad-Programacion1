#Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad


# creamos con open un archivo de texto llamado productos.txt y abrimos el archivo en modo escritura ("w")
with open("productos.txt", "w") as archivo:
    #archivo.write escribe exactamente esos caracteres en el archivo. Y \n es salto de línea (pasa a la línea siguiente).
    archivo.write("Pan,150,20\n")
    archivo.write("Leche,200,15\n")
    archivo.write("Azucar,300,10\n")

print("Archivo 'productos.txt' creado correctamente y guardado en el directorio actual.")
