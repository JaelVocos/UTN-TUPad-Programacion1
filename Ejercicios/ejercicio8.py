#) Crear un programa que pida al usuario su altura y 
# su peso e imprima por pantalla su índice de masa corporal. 

altura = float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kg: "))

imc = peso / altura**2
print(f"su indice de masa corporal es {imc}")