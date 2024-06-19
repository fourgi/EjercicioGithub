import csv
with open('nuevo_archivo.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Nombre', 'Edad', 'Comuna'])
    escritor_csv.writerows([
    ['Esteban', 25, 'Santiago'],
    ['María', 30, 'Valparaíso'],
    ['Carlos', 22, 'Osorno'],
    ['Sigrid', 50, 'Santiago'],
    ['Daniela', 10, 'La Cisterna'],
    ['Aylen', 22, 'La florida']
    ])

import csv
with open('nuevo_archivo.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
      print(fila)
with open("nuevo_archivo.csv", "r") as archivo_csv:
    lector_csv = csv.DictReader (archivo_csv)
    for fila in lector_csv:
        nombre = fila["Nombre"]
        edad = int(fila["Edad"])
        comuna = fila["Comuna"]
        estado_edad = "Mayor de edad" if edad >= 18 else "Menor de edad"
        print(f"{nombre} tiene {edad} años, es {estado_edad} y vive en {comuna}")
#DictReader sirve para leer un archivo csv y convertir cada fila en diccionario
#utilizamos for para recorrer la lista de informacion y así poder buscar cuál es mayor y menor
#writerow sirve para escribir múltiples filas a un archivo csv de una sola vez. Cada fila que se escribe debe ser una secuencia de valores.Ejemplo, una lista o una tupla