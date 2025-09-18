#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.


alumnos = ["Juan","Jeremias","Luz","Maia","Carlos","Pablo","Julia","Candela","David","Camila"]

print("LISTA DE ALUMNOS")
print(alumnos)

#creo una variable opcion, que me permite saber lo que quiere el usuario, si eliminar o agregar
opcion = input("¿Quieres 'agregar' un alumno o quieres 'eliminar' a un alumno de la lista?: ")

#en base a lo anterior, creo una condicion if que dice: si opcion es igual a agregar entonces le pide al usuario ingresar el nombre del alumno nuevo
if opcion == "agregar":
    nuevo = input("Ingresa el nombre del alumno que quieres agregar: ")
    alumnos.append(nuevo) #agregamos el nombre nuevo a la lista alumnos
#si opcion es igual a eliminar, entonces le pide al usuario que ingrese el nombre del alumno que quiere eliminar
elif opcion == "eliminar":
    elim = input("Ingresa el nombre del alumno que quieres eliminar: ") 
    alumnos.remove(elim) #elimina el alumno de la lista alumnos
#si el usuario ingresa una opcion valida, aparece por pantalla, "INGRESE UNA OPCION VALIDA"
else:
    print("Ingrese una opcion valida: ")

#Y por ultimo mostramos la lista actualizada
print("Lista actualizada")
print(alumnos)

