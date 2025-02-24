El código define una función llamada contar_compras_por_pais que cuenta cuántas compras se han realizado en un país específico dentro de un archivo CSV
def contar_compras_por_pais(archivo_csv, pais):
Esta función recibe dos parámetros: primero archivo_csv: el nombre del archivo CSV donde están registradas las compras. y segundo pais: el país que queremos consultar.
luego en cantidad_compras = 0 se inicia la variable cantidad_compras en 0, que servirá para contar las compras realizadas en el país dado.
para despues en with open(archivo_csv, 'r', encoding='utf-8') as archivo: abrir el archivo en modo lectura ('r') con la codificación UTF-8 para manejar caracteres especiales.
encabezado = archivo.readline().strip().split(',') esta lee la primera línea del archivo, que contiene los nombres de las columnas. strip() elimina espacios o saltos de línea adicionales.
split(',') divide la línea en una lista usando la coma como separador. Se verifica que la columna "Country" exista en el archivo. Si está presente, se obtiene su índice (posición) dentro de la lista encabezado.
Si no se encuentra, se lanza un error con raise ValueError.
