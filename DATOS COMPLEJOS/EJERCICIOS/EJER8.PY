#Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe

# Diccionario con productos y su stock inicial
stock_productos = {'Leche': 7,'Pan': 9,'Huevo':2,'Harina':4,'Arroz': 3}

# Mostramos los productos disponibles
print("Productos disponibles:")
for producto, cantidad in stock_productos.items():
    print(f"- {producto}: {cantidad} unidades")

# Consultamos el stock de un producto
producto = input("Ingrese el nombre del producto que desea consultar: ")

if producto in stock_productos:
    print(f"El stock actual de {producto} es de {stock_productos[producto]} unidades.")

    # Preguntamos si quiere agregar unidades
    agregar = input("¿Desea agregar unidades a este producto? (si/no): ")
    if agregar == "si":
        cantidad = int(input("¿Cuántas unidades desea agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Stock actualizado: {producto} ahora tiene {stock_productos[producto]} unidades.")
else:
    print(f"El producto '{producto}' no existe.")
    # preuntamos si desea agregar un nuevo producto
    nuevo = input("¿Desea agregarlo al stock? (si/no): ").lower()
    if nuevo == "si":
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock_productos[producto] = cantidad
        print(f"Producto agregado: {producto} con {cantidad} unidades.")

# Mostrar stock final
print("Stock actual:")
for producto, cantidad in stock_productos.items():
    print(f"- {producto}: {cantidad} unidades")






