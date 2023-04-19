"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

#ordena una lista en orden ascendentey la devuelve ordenada
def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))

#elimina duplicados de un ista de elementos y devuelve la lista resultante
def remove_duplicates_from_list(items):
    return list(set(items))

"""
este bloque e codigo verific sise han proporcionado dos argumentos al script, 
si es asi los utiliza como el nombre del archivo y un indicador booleano para eliminar duplicados
si no se daningun argumento se imprime un error y sale del script
"""
if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)
    print(f"Se leerán las palabras del fichero {filename}")
    """
    en este bloque de codigo se lee las palabrasdel archivo especificado, encaso de no tener un archivo
    se crea una lista de palabras por defecto, de ahi s elimina losduplicados si es necesario
    """
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)
#se imprime la lista ordenada de palabras
    print(sort_list(word_list))
