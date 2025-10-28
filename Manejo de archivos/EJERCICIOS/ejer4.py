#Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

# Creamos una lista vacía para guardar los productos
productos = []

# Abrimos el archivo productos.txt en modo lectura
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        # Limpiamos la línea y la dividimos por comas
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")

        # Creamos un diccionario con los datos convertidos a tipos apropiados
        producto = {
            "nombre": nombre,
            "precio": float(precio),   # lo convertimos a número decimal
            "cantidad": int(cantidad)  # lo convertimos a entero
        }

        # Agregamos el diccionario a la lista
        productos.append(producto)

# Mostramos la lista de productos cargados
print("Productos cargados desde el archivo:\n")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
