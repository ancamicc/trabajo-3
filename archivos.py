def contar_compras_por_pais(archivo_csv, pais):
    
    cantidad_compras = 0
    
    
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        encabezado = archivo.readline().strip().split(',')
        
        
        if 'Country' in encabezado:
            indice_pais = encabezado.index('Country')
        else:
            raise ValueError("No se encontró la columna 'Country' en el archivo CSV")
        
       
        for linea in archivo:
            datos = linea.strip().split(',')
            if datos[indice_pais] == pais:
                cantidad_compras += 1
    
    return cantidad_compras

# Ejemplo de uso
archivo = 'files/salesjan2009.csv' 
pais_consulta = 'United Kingdom'
resultado = contar_compras_por_pais(archivo, pais_consulta)
print(f'El número de compras en {pais_consulta} es: {resultado}')