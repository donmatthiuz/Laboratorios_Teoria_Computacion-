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

  


  

  


# EJERCICIO 2
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nueva_lista = list(map(lambda x: x ** 3, lista))
print("\nEjercicio 2")
print("Numeros: ", lista)
print("Numeros elevados al cubo",nueva_lista)


# EJERCICIO 3

X = [
    [1, 2, 3 , 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]


Y = [(lambda i: [row[i] for row in X])(i) for i in range(len(X[0]))]
print("\nEjercicio 3")
print("Matriz: ", X)
print("Matriz Transpuesta",Y)


# EJERCICIO 4

elementos = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
elementos_eliminar = ['amarillo', 'café', 'blanco']
lista_filtrada = list(filter(lambda x: x not in elementos_eliminar, elementos))
print("\nEjercicio 4")
print("Elementos: ",elementos )
print("Elementos a eliminar: ",elementos_eliminar )
print("Resultados: ", lista_filtrada)