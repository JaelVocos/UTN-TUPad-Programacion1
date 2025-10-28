#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

precios_frutas = {'Banana': 1330, 'Anana': 2500, 'Melon': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

#creamos una lista que muestre solo las keys del diccionario (solo frutas)
frutas = list(precios_frutas.keys())
print(frutas)