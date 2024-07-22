#Ejercicio 2 Laboratorio 2. 
from parse import parsechain


cadena = "a(a|b)*b+a?"

cadenas = [char for char in cadena]

print(parsechain(cadenas))


