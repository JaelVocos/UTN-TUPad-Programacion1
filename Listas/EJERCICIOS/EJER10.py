# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [3,2,5,6,9,4,1],
    [4,1,5,7,3,8,7],
    [2,1,3,9,8,4,1],
    [1,4,7,3,8,2,3]
    
]

totales_productos = []

for i in range(4):
    totales_producto = 0
    for j in range(7):
        totales_producto += ventas[i][j]
    totales_productos.append(totales_producto)
    print(f"Producto {i+1}: {totales_producto}")


mayor_Ventas = 0
mayor_Dia = 0

for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia+= ventas[i][j]
    print(f"total del dia {j+1}: {total_dia}")
    if total_dia > mayor_Ventas:
        mayor_Ventas = total_dia
        mayor_Dia = j
print(f"el dia con mayores ventas fue: {mayor_Dia+1}, con {mayor_Ventas} ventas")


mayor_producto = 0
indic_mayor= 0

for i in range (4):
    if totales_productos[i] > mayor_producto:
        mayor_producto = totales_productos[i]
        indic_mayor = i

print(f"el producto que mas se vendio fue {indic_mayor+1}, con {mayor_producto} ventas en la semana.")