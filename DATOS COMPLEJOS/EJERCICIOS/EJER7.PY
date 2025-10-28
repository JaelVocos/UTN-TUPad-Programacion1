#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

#2 sets con los nombres que aprobaron parcial1 y parcial2
parcial1 = {'Ana','Lorena','Jael','Juan','Jeremias','Alejandro'}
parcial2 = {'Ana','Alejandro','Jael','Julieta','Lola'}

#los que aprobaron ambos parcicales, utilizando interseccion
ambos = parcial1 & parcial2

#los que aprobaron solo 1, usando diferencia y union
solo_uno = (parcial1 - parcial2) | (parcial2 - parcial1)

#los que aprobaron al menos uno usando union
al_menos_uno = parcial1 | parcial2


print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)


      
      

