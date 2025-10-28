#Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error

# Cargamos los productos desde el archivo en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip() #elimina los espacios y saltos de linea
        nombre, precio, cantidad = linea.split(",") # divide las lineas por coma
        #creamos un diccionario con los datos nombre,precio y cantidad
        producto = {
            "nombre": nombre,
            "precio": float(precio), #convertimos a decimal
            "cantidad": int(cantidad) #convertimos en entero
        }
        #agregamos el diccionario a la lista producto
        productos.append(producto)

# Pedimos al usuario el nombre del producto a buscar
buscado = input("Ingrese el nombre del producto a buscar: ")

# Bandera para saber si lo encontramos
encontrado = False

# Recorremos la lista buscando coincidencia
for p in productos:
    if p["nombre"].lower() == buscado.lower(): 
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

# Si no se encontró
if not encontrado:
    print("\nError: El producto no existe en la lista.")
