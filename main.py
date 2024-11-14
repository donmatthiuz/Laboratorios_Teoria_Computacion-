#Laboratorio 12 MATHEW ALEXANDER CORDERO AQUINO

print("EJERCICIOS LABORATORIO 12")

variable = True
while variable:
  print("Seleccione un ejercicio  s para salir:")
  print("1) Ordenar Diccionarios")
  print("2) Calculo de la potencia n-esima de una lista")
  print("3) Calculo Transpuesta de una matriz")
  print("4) Eliminar elementos de una lista")
  var = input("Seleccione un ejercicio: ")
  if var == 's':
    variable = False
  elif var == '1':
    D = [
        {'make': 'Nokia', 'model': 216, 'color': 'Black'},
        {'make': 'Apple', 'model': 2, 'color': 'Silver'},
        {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]
    print("Lista de diccionarios: ", D)
    key_var = input("\nIngrese el key del diccionario: ")
    elementos_ordenados= sorted(D, key=lambda x: x[key_var])
    print(f"Lista de diccionarios ordenados por {key_var}",elementos_ordenados)
    print("\n")
  elif var == '2':
    lista = input("\nIngrese el listado de numeros separados por , no espacios : ")
    lista_numers = lista.split(",")
    lista_numers = [int(x) for x in lista_numers]
    numero = int(input("\n Ingresa la potencia: "))
    nueva_lista = list(map(lambda x: x ** numero, lista_numers))
    print("Numeros: ", lista_numers)
    print("Numeros elevados al cubo",nueva_lista)
    print("\n")
  elif var == '3':
    filas = int(input("\nIngrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    matriz = []
    for i in range(filas):
        fila = input(f"Ingrese los valores de la fila {i+1} separados por comas: ").split(',')
        fila = [int(x) for x in fila]
        if len(fila) != columnas:
            print("Error: El número de elementos ingresados no coincide con el número de columnas.")
            break
        matriz.append(fila)

    print("Matriz original:")
    for fila in matriz:
        print(fila)
    Y = [(lambda i: [row[i] for row in matriz])(i) for i in range(len(matriz[0]))]
    print("Matriz Transpuesta",Y)
  elif var == '4':
    elementos_v = input("Ingrese los elementos de la lista separados por coma: ")
    elementos_v = elementos_v.split(',')
    elementos_eliminar = input("Ingrese los elementos a eliminar de la lista separados por coma: ")
    elementos_eliminar = elementos_eliminar.split(',')
    lista_filtrada = list(filter(lambda x: x not in elementos_eliminar, elementos_v))
    print("Elementos: ",elementos_v )
    print("Elementos a eliminar: ",elementos_eliminar )
    print("Resultados: ", lista_filtrada)