#Crear un programa que pida al usuario el radio 
# de un círculo e imprima por pantalla su área y su perímetro

radio = float(input("Ingrese el radio del circulo: "))
pi=3.14
area = pi * radio **2
perimetro = 2 * pi * radio

print(f"el area del circulo es {area} y el perimetro del circulo es {perimetro}")
