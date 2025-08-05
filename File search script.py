import os

def buscar_archivo(directorio, nombre_archivo):
    rutas_encontradas = []
    
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            # Búsqueda parcial sin distinguir mayúsculas/minúsculas
            if nombre_archivo.lower() in archivo.lower():
                rutas_encontradas.append(os.path.join(raiz, archivo))
                
    return rutas_encontradas

while True:
    # Solicitar el directorio
    directorio = input("Enter directory: ")
    
    # Verificar si el directorio existe
    if not os.path.isdir(directorio):
        print("Directory not found\n")
        
        continue
    
    # Solicitar el nombre del archivo (o parte del nombre)
    nombre_archivo = input("Enter file name: ")
    
    print("------------------------------------")
    
    # Buscar el archivo en el directorio
    rutas_encontradas = buscar_archivo(directorio, nombre_archivo)
    
    # Mostrar los resultados
    if rutas_encontradas:
        for ruta in rutas_encontradas:
            print(ruta)
    else:
        print("File not found")
    

    print("------------------------------------\n")
