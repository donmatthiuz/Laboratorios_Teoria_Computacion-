def separar_por_or(lista_produccion):
    indices_or = [i for i, simbolo in enumerate(lista_produccion) if simbolo == '|']
    producciones = []    
    inicio = 2    
    for index_or in indices_or:
        producciones.append(lista_produccion[inicio:index_or])
        inicio = index_or + 1    
    producciones.append(lista_produccion[inicio:])
    
    return producciones

produccion = ['S', '→', 'As', 'B', '|', 'B', 'C', '|', 'D', '|','F']
producciones_separadas = separar_por_or(produccion)

# Imprimimos las producciones separadas
for i, prod in enumerate(producciones_separadas, 1):
    print(f"Producción {i}: {prod}")
