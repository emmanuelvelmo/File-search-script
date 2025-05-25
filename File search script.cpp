#include <iostream>
#include <filesystem>
#include <vector>
#include <string>
#include <algorithm>

std::vector<std::string> buscar_archivo(const std::string &directorio, const std::string &nombre_archivo)
{
    std::vector<std::string> rutas_encontradas;

    for (const std::filesystem::directory_entry &entry : std::filesystem::recursive_directory_iterator(directorio))
    {
        // Archivo y no otro tipo
        if (entry.is_regular_file())
        {
            std::string nombre = entry.path().filename().string();
            
            std::string nombre_lower = nombre;
            std::transform(nombre_lower.begin(), nombre_lower.end(), nombre_lower.begin(), ::tolower);

            std::string nombre_archivo_lower = nombre_archivo;
            std::transform(nombre_archivo_lower.begin(), nombre_archivo_lower.end(), nombre_archivo_lower.begin(), ::tolower);

            if (nombre_lower.find(nombre_archivo_lower) != std::string::npos)
            {
                rutas_encontradas.push_back(entry.path().string());
            }
        }  
    }

    return rutas_encontradas;
}

int main()
{
    while (true)
    {
        std::string directorio;

        std::cout << "Enter directory: ";

        std::getline(std::cin, directorio);

        // Verificar si el directorio existe
        if (!std::filesystem::exists(directorio) || !std::filesystem::is_directory(directorio))
        {
            std::cout << "Directory not found" << std::endl;

            continue;
        }

        // Solicitar el nombre del archivo (o parte del nombre)
        std::string nombre_archivo;

        std::cout << "Enter file name: ";

        std::getline(std::cin, nombre_archivo);

        std::cout << "------------------------------------" << std::endl;

        // Buscar el archivo en el directorio
        std::vector<std::string> rutas_encontradas = buscar_archivo(directorio, nombre_archivo);

        // Mostrar los resultados
        if (!rutas_encontradas.empty())
        {
            for (const auto &ruta : rutas_encontradas)
            {
                std::cout << ruta << std::endl;
            }
        }
        else
        {
            std::cout << "File not found" << std::endl;
        }

        std::cout << "------------------------------------\n" << std::endl;
    }

    return 0;
}
