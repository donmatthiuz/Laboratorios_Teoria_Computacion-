#Laboratorio 12 MATHEW ALEXANDER CORDERO AQUINO


# EJERCICIO 1
D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

elementos_ordenados= sorted(D, key=lambda x: x['model'])
print(elementos_ordenados)


# EJERCICIO 2
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nueva_lista = list(map(lambda x: x ** 3, lista))
print(nueva_lista)


# EJERCICIO 3

X = [
    [1, 2, 3 , 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1]
]


Y = [(lambda i: [row[i] for row in X])(i) for i in range(len(X[0]))]

print(Y)