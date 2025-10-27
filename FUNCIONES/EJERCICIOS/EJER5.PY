#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#creamos una funcion segundos_a_horas que recibe como parametro una cantidad de segundos
def segundos_a_horas(segundos):
    #hacemos el calculo para pasar de segundos a horas
    return segundos / 3600

#le pedimos al usuario que ingrese los segundos
seg= float(input("Ingrese segundos: "))
#y por ultimo llamamos a la funcion y guardamos su valor en la variable horas
horas=segundos_a_horas(seg)

print("Equivale a", horas, "horas")