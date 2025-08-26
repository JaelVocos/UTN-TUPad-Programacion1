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

if magTerremoto < 3: #si magTerremoto es menor a 3 entonces: muestra el mensaje muy leve por pantalla
    print("muy leve(imperceptible)")
elif magTerremoto >= 3 and magTerremoto <4: #si magTerremoto es mayor o igual a 3 y menor a 4 entonces muestra leve por pantalla
    print("leve(ligeramente perceptible)")
elif magTerremoto >=4 and magTerremoto <5: #si magTerremoto es mayor o igual a 4 y menor a 5 muestra moderado
    print("moderado(sentido por personas,pero generalmente no causa daños)")
elif magTerremoto >=5 and magTerremoto <6: #si magTerremoto es mayor o igual a 5 y menor a 6 muestra fuerte
    print("fuerte(puede causar daños en estructuras debiles)")
elif magTerremoto >=6 and magTerremoto <7: #si magTerremoto es mayor o igual a 6 y menor a 7 muestra muy fuerte
    print("muy fuerte(puede causar daños significativos)")
else: #sino se cumplen ninguna de las anteriores muestra extremo
    print("extremo(puede causar daños a gran escala)")
