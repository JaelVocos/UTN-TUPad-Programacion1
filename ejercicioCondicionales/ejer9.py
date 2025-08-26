#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magTerremoto = int(input("ingrese la magnitud del terremoto: "))

if magTerremoto < 3:
    print("muy leve(imperceptible)")
elif magTerremoto >= 3 and magTerremoto <4:
    print("leve(ligeramente perceptible)")
elif magTerremoto >=4 and magTerremoto <5:
    print("moderado(sentido por personas,pero generalmente no causa daños)")
elif magTerremoto >=5 and magTerremoto <6:
    print("fuerte(puede causar daños en estructuras debiles)")
elif magTerremoto >=6 and magTerremoto <7:
    print("muy fuerte(puede causar daños significativos)")
else:
    print("extremo(puede causar daños a gran escala)")
