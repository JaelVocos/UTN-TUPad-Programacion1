#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.



tablero = [["-","-","-"],
           ["-","-","-"],
           ["-","-","-"]]

def ver(): #Define la función ver, para mostrar el tablero
    for fila in tablero: #recorre cada fila del tablero
        print(*fila) #imprime los elementos de la fila separados por espacio
    print()

ver()  #Muestra el tablero inicial

for turno in range(9): #Bucle de máximo 9 jugadas
    ficha = "X" if turno % 2 == 0 else "O" #Esta línea sirve para alternar automáticamente la ficha entre "X" y "O" en cada turno.

    #Pide al usuario dos números (fila y columna) separados por un espacio.
    f, c = map(int, input(f"Juega {ficha} (fila columna 1-3)(ingresa un numero, espacio y el otro numero): ").split())
    #Coloca la ficha en la casilla elegida.
    tablero[f-1][c-1] = ficha  
    ver() #Muestra el tablero después de cada jugada.

