#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

#recorremos los numeros de 100 a 0 de forma decreciente
for i in range(100,-1,-1):#aca -1 indica que vamos hacia atras
    if i % 2 ==0: #verificamos si el numero es par
        print(i)