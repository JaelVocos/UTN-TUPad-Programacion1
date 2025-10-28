#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.

#creo una agenda con varios eventos, con sus dias y horas
agenda = {
    ("Lunes","10:30"): "Reunion",
    ("Martes","15:00"): "Clase de yoga",
    ("Miercoles","14:00"): "Gimnasio",
    ("Jueves","17:15"): "Clase de aleman",
    ("Viernes","18:00"): "Reunion de amigas"
}

#le pido al usuario que ingrese dia y hora que quiera consultar
print("Consulta de evento")
dia_consulta = input("Ingresá el día: ")
hora_consulta = input("Ingresá la hora: ")

# Mostramos el resultado, si los dias y horarios que ingreso el usuario aparecen en la agenda se imprime por pantalla, sino imprime un mensaje que dice que no hay ningun evento ese dia
if (dia_consulta, hora_consulta) in agenda:
    print("Tenés:", agenda[(dia_consulta, hora_consulta)])
else:
    print("No hay ningún evento en ese día y hora.")