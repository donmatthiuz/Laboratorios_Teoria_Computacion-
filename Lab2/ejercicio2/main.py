#Ejercicio 2 Laboratorio 2. 
from parse import parsechain, determinate_balance


def getExpresions_file (filename):
  with open(filename, "r") as file:
    lines = file.read().splitlines()
    for line in lines:
      cadena = line.split(" ")
      parsed = parsechain(cadena)
      print(parsed)
      determinate_balance(parsed)

getExpresions_file("file_reader.txt")

cad = "( [ [ az ] [ AZ ] ] ( ( ( ( ( . | ; ) | ; ) | . ) | . ) | . ) { 10 , 20 } ) ∗ ) +"
print(parsechain(cad.split(" ")))