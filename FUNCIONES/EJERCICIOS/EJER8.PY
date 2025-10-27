#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#creo una funcion llamada calcular_imc que recibe como parametro altura y peso
def calcular_imc(peso,altura):
    #calcula el imc
    return peso / altura ** altura

#pide al usuario los valores de peso y altura
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

#llama a la funcion y guarda el valor en resultado
resultado = calcular_imc(peso,altura)
print(f"su imc es {resultado}")


