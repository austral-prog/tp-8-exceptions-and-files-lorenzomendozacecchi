# Ejercicio 5 - CSV a lista de diccionarios

import os
def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    lista = []
    if not os.path.exists(filename):
        raise FileNotFoundError
    with open(filename, 'r') as file:
        lineas = file.readlines()
        if len(lineas) <= 1:
            return []
        header = lineas[0].strip()
        etiquetas = header.split(",") #[name, age, city]
        for linea in lineas[1:]:
            diccionario = {}
            linea = linea.strip()
            datos = linea.split(",")
            nombre = datos[0]
            age = int(datos[1])
            city = datos[2]
            diccionario[etiquetas[0]] = nombre
            diccionario[etiquetas[1]] = age
            diccionario[etiquetas[2]] = city
            lista.append(diccionario)
    return lista


