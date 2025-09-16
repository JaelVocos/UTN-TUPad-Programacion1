#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num = int(input("ingrese un numero: ")) #aca le pido al usuario ingresar dos numeros.
num2 = int(input("ingrese otro numero: "))

if num < num2: #si num es menor a num2 entonces:
    primerNum = num + 1 #aca lo que hace es excluir el numero ingresado por el usuario sumandole 1 y asi empezar por el numero que le sigue, ejemplo(si ingresa 5, va a empezar a sumar desde 6)
    ultimoNum = num2 #aca termina antes del 10, ya que en el range se excluye el ultimo numero.
else: #si llega a ser falso pasa a else y hace exactamente lo mismo que lo anterior
    primerNum = num2 + 1
    ultimoNum = num
#Si no hacemos esta comprobación de if, y el usuario ingresa los números en orden descendente, el bucle for no funcionaría,
# porque el inicio sería mayor que el fin, y no generaría ningún número.

suma = 0

for i in range (primerNum,ultimoNum): #aca genera los numeros 6,7,8,9
    suma += i #aca suma todos los numeros hasta llegar a 9

print("La suma de los numeros entre ",num ,"y",num2,"es:",suma)