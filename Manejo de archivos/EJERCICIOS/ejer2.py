#Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# Abrimos el archivo productos.txt en modo lectura
with open("productos.txt", "r") as archivo:
    # Lee todas las líneas del archivo
    for linea in archivo:
        # Elimina espacios y salto de línea al final
        linea = linea.strip()
        
        # Separa los valores por coma y los guarda en variables
        nombre, precio, cantidad = linea.split(",")
        
        # Muestra los datos con el formato pedido
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
