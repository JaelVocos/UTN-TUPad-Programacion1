# Biblioteca escolar             

#Importa el módulo csv para leer/escribir archivos .csv
import csv                                                      


# Define una función para limpiar el texto del título, quita espacios al inicio/fin y duplica internos
def limpiar_titulo(t):                                          
    return " ".join(t.strip().split())                          

#Pide un título por consola y valida que no sea vacío
def leer_titulo(msg):  
    # Bucle hasta que el usuario ingrese algo válido                                         
    while True:                                                 
        t = input(msg).strip()     
        #Si no está vacío,devuelve el título ya normalizado      
        if t != "":                                             
            return limpiar_titulo(t)                           
        print("El título no puede estar vacío.")             

#Pide un entero >= 0
def leer_entero(msg):   
    # Bucle hasta ingreso válido                                       
    while True:                                                 
        n = input(msg).strip()     
        #verifica que sean solo dígitos (entero no negativo)                             
        if n.isdigit():                                         
            return int(n)                                       
        print("Ingrese un número entero mayor o igual a 0.")  

def buscar_indice(cat, titulo):                                    
    clave = limpiar_titulo(titulo).lower()                      
    i = 0   
    # Recorre la lista cat (catálogo)                                                    
    while i < len(cat):    
# Compara título normalizado con la clave, si coincide, devuelve el índice i                                   
        if limpiar_titulo(cat[i]["TITULO"]).lower() == clave:   
            return i                                            
        i += 1                                                 
    return -1                                                   

# Sección que carga/guarda datos del catálogo
def cargar(ruta):       
    # Arranca con lista vacía                                        
    cat = []                                                    
    try:   
        # Abre el CSV en modo lectura con UTF-8                                                    
        with open(ruta, "r", newline="", encoding="utf-8") as f:
            # Crea un lector CSV
            lector = csv.reader(f)     
            # Bandera para saltar la primera fila (encabezado)                         
            encabezado = True 
            # Recorre cada fila del CSV                                  
            for fila in lector:      
                # Si es la primera fila, la salta (se asume "TITULO,CANTIDAD")                   
                if encabezado:                                  
                    encabezado = False         
                # Si la fila tiene 2 columnas y cantidad es numérica, agrega un diccionario al catálogo              
                elif len(fila) == 2 and fila[1].isdigit():      
                    cat.append({                                
                        "TITULO": limpiar_titulo(fila[0]),      
                        "CANTIDAD": int(fila[1])                
                    })
     # Si el archivo no existe
    except FileNotFoundError:  
         # Catálogo queda vacío (se creará al guardar)                                 
        cat = []   
    # Devuelve la lista cargada (o vacía)                                            
    return cat   
                                               
def guardar(ruta, cat):     
     # Abre el CSV en modo escritura (sobrescribe)                                    
    with open(ruta, "w", newline="", encoding="utf-8") as f: 
        # Crea un escritor CSV  
        escritor = csv.writer(f)                                
        escritor.writerow(["TITULO", "CANTIDAD"])               
        i = 0   
        # Recorre cada libro del catálogo                                               
        while i < len(cat): 
             # Escribe una fila por libro                                    
            escritor.writerow([                                 
                cat[i]["TITULO"],                              
                cat[i]["CANTIDAD"]                              
            ])
            i += 1                                              

 # Sección con las acciones del menú
def ingresar_varios(cat, ruta): 
     # Pide cuántos va a cargar                               
    n = leer_entero("¿Cuántos libros desea ingresar? ")        
    i = 0    
    # Repite n veces                                                  
    while i < n:    
        # Pide el título i+1                                            
        t = leer_titulo(f"Título #{i+1}: ")   
          # Si ya existe ese título,muestra aviso                 
        if buscar_indice(cat, t) != -1:                            
            print("✗ Ya existe ese título.")      
         # Si no existe, agrega al catálogo             
        else:                                                  
            c = leer_entero("Cantidad inicial: ")
            cat.append({"TITULO": t, "CANTIDAD": c})           
        i += 1                                                 
    guardar(ruta, cat)                                         
    print("Libros cargados correctamente.\n")                

def ingresar_ejemplares(cat, ruta):  
     # Pide el título                         
    t = leer_titulo("Título: ")   
    # Busca su índice                             
    i = buscar_indice(cat, t)    
     # Si no existe, informa y sale                               
    if i == -1:                                                
        print(" No existe ese título.\n")  
    # Si existe, pide cuántos sumar                  
    else:                                                       
        c = leer_entero("¿Cuántos ejemplares desea agregar? ")  
        # Aumenta el stock
        cat[i]["CANTIDAD"] += c                                 
        guardar(ruta, cat)                                     
        print("Stock actualizado.\n")                         

# Opción 3: mostrar todo el catálogo
def mostrar(cat):   
     # Si está vacío, lo indica                                           
    if len(cat) == 0:                                          
        print("(Catálogo vacío)\n")          
     # Si tiene elementos,recorre la lista       
    else:                                                      
        i = 0                                                   
        while i < len(cat):     
            # Muestra línea por libro                               
            print(f"- {cat[i]['TITULO']} | Stock: {cat[i]['CANTIDAD']}") 
            i += 1                                              
        print()                                       

# Opción 4: consultar cantidad disponible de un título
def consultar(cat):    
    # Pide el título                                         
    t = leer_titulo("Título: ")                                 
    i = buscar_indice(cat, t)  
    # Si no existe,informa                                
    if i == -1:                                                
        print("✗ No existe ese título.\n")      
    # Si existe,muestra stock           
    else:                                                       
        print(f"Disponibles: {cat[i]['CANTIDAD']}\n")           

# Opción 5: listar títulos con stock 0
def agotados(cat):     
    # Bandera para saber si hubo alguno                                         
    hay = False                                                 
    i = 0  
    # Recorre catálogo                                                     
    while i < len(cat): 
         # Si la cantidad es 0,lo muestra                                   
        if cat[i]["CANTIDAD"] == 0:                            
            print(f"- {cat[i]['TITULO']}")   
             # Marca que hubo al menos uno                   
            hay = True                                         
        i += 1     
     # Si no encontró ninguno,muestra mensaje                                         
    if not hay:                                                
        print("(Ninguno agotado)\n")                            
    else:                                                       
        print()                                                 

 # Opción 6: agregar un libro individual
def agregar_titulo(cat, ruta): 
    # Pide título                                
    t = leer_titulo("Título: ")   
    # Si ya existe, informa y no agrega                       
    if buscar_indice(cat, t) != -1:                                
        print("Ya existe ese título.\n")  
     # Si no existe, pide cantidad                 
    else:                                                      
        c = leer_entero("Cantidad inicial: ")                  
         # Agrega al catálogo 
        cat.append({"TITULO": t, "CANTIDAD": c})               
        guardar(ruta, cat)                                      
        print("Libro agregado.\n")                            

# Opción 7: préstamo o devolución
def prestamo_devolucion(cat, ruta):                             
    t = leer_titulo("Título: ")                               
    i = buscar_indice(cat, t)      
    # Si no existe,informa y sale                     
    if i == -1:                                                 
        print("No existe ese título.\n")                      
        return                                                 

    print("1) Préstamo (resta 1 si hay stock)")                 
    print("2) Devolución (suma 1)")    
     # Lee elección del usuario                         
    op = input("Opción: ").strip() 
    # Si elige préstamo,                            
    if op == "1":  
        # Verifica que haya stock,                                             
        if cat[i]["CANTIDAD"] > 0: 
             # Resta una unidad                             
            cat[i]["CANTIDAD"] -= 1                            
            guardar(ruta, cat)                                  
            print("Préstamo registrado.\n")      
        # Si no hay stock, informa       
        else:                                                   
            print("No hay ejemplares disponibles.\n")     
    # Si elige devolución,suma una unidad
    elif op == "2":                                             
        cat[i]["CANTIDAD"] += 1                                 
        guardar(ruta, cat)                                     
        print("Devolución registrada.\n")   
    # Opción inválida                 
    else:                                                       
        print("✗ Opción inválida.\n")                           

# Menú principal 
def menu():                                                     
    print("Biblioteca Escolar ")           
    print("1) Ingresar títulos (múltiples)")                    
    print("2) Ingresar ejemplares")                             
    print("3) Mostrar catálogo")                                
    print("4) Consultar disponibilidad")                        
    print("5) Listar agotados")                                 
    print("6) Agregar título")                                  
    print("7) Actualizar (préstamo / devolución)")              
    print("8) Salir")                                           

# Función principal del programa
def main():                                               
    ruta = "catalogo.csv"                                      
    catalogo = cargar(ruta) 
    # Control del bucle principal                                    
    seguir = True    
    # Bucle del menú                                           
    while seguir:  
        # Muestra el menú                                             
        menu()  
        # Pide una opción                                                
        op = input("Elija opción (1-8): ").strip()              
        match op:                                               
            case "1": ingresar_varios(catalogo, ruta)          
            case "2": ingresar_ejemplares(catalogo, ruta)      
            case "3": mostrar(catalogo)                        
            case "4": consultar(catalogo)                      
            case "5": agotados(catalogo)                       
            case "6": agregar_titulo(catalogo, ruta)           
            case "7": prestamo_devolucion(catalogo, ruta)      
            case "8":                                      
                print("¡Hasta luego!")                          
                seguir = False                               
            case _:                                             
                print("✗ Opción inválida.\n")                   

# Llama a main() para iniciar el programa                          
if __name__ == "__main__":
    main()                                                     












