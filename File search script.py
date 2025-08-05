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
    # Directorio de entrada
    while True:
        directorio_val = input("Enter directory: ").strip('"\'')

        if os.path.isdir(directorio_val):
            break

        print("Wrong directory")
    
    # Solicitar el nombre del archivo (o parte del nombre)
    nombre_archivo = input("Enter file name: ")
    
    print("------------------------------------")
    
    # Buscar el archivo en el directorio
    rutas_encontradas = buscar_archivo(directorio_val, nombre_archivo)
    
    # Mostrar los resultados
    if rutas_encontradas:
        for ruta_val in rutas_encontradas:
            print(ruta_val)
    else:
        print("File not found")
    
    print("------------------------------------\n")
