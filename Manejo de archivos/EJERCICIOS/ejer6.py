#Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

# cargamos productos desde el archivo en una lista de diccionarios
productos = []

#abrimos el archivo productos en modo lectura
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostramos los productos actuales
print("Lista actual de productos:\n")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

#aca permitimos agregar o actualizar un producto
print("\nAgregar o actualizar producto:")
nombre_nuevo = input("Nombre del producto: ")
precio_nuevo = float(input("Precio: "))
cantidad_nueva = int(input("Cantidad: "))

#Verificamos si el producto ya existe y actualiza si está, sino agrega
existe = False
for p in productos:
    if p["nombre"].lower() == nombre_nuevo.lower():
        p["precio"] = precio_nuevo
        p["cantidad"] += cantidad_nueva  # suma unidades
        existe = True
        print(f"\nProducto existente. Se actualizó la cantidad a {p['cantidad']} unidades.")
        break

#aca si el producto no existe, lo agrega
if not existe:
    productos.append({
        "nombre": nombre_nuevo,
        "precio": precio_nuevo,
        "cantidad": cantidad_nueva
    })
    print("\nNuevo producto agregado a la lista.")

#Guardamos todos los productos actualizados en el archivo (sobrescribir)
with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("\nArchivo 'productos.txt' actualizado correctamente.")
