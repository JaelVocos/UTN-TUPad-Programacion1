#Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.


#inicializo una lista vacia
productos = []

#creo un bucle con un range de 5, que es la cantidad de productos que va a pedirle al usuario
for i in range(5):
    p = input(f"ingrese un producto a la lista{i+1}: ") 
    productos.append(p) #append lo que hace es ir agregando los productos que va ingresando el usuario a la lista productos

    #sorted va a ordenar la lista alfabeticamente
    print(sorted(productos))

#le pedimos al usuario ingresar el producto que quiere eliminar
borrar = input("Ingrese el producto que quiere eliminar: ")

#la condiciion if pregunta si el producto que quiere eliminar el usuario se encuentra en la lista productos
if borrar in productos:
    productos.remove(borrar) #si es asi, el metodo remove se encarga de borrar el producto de la lista
else:
    print("No existe ese producto") # sino nos dice que el producto no existe

# por ultimo mostramos la lista actualizada de los productos
print("lista actualizada: ",productos) 