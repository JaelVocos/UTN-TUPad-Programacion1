#Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

# Lee y muestra los productos actuales
with open("productos.txt", "r") as archivo:
    print("Lista de productos actuales:\n")
    for linea in archivo:
        linea = linea.strip()  # elimina saltos de línea
        nombre, precio, cantidad = linea.split(",")  # separa por comas
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# Pedimos al usuario que ingrese un nuevo producto
print("\nAgregar un nuevo producto")
nombre = input("Nombre del producto: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

# Abrimos el archivo en modo 'a' para agregar sin borrar lo anterior
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("\nProducto agregado correctamente al archivo.")
