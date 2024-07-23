#Ejercicio 2 Laboratorio 2. 
from parse import parsechain, determinate_balance

def getExpresions_file (filename):
  with open(filename, "r") as file:
    lines = file.read().splitlines()
    for line in lines:
      cadena = line.split(" ")
      parsed = parsechain(cadena)
      determinate = determinate_balance(parsed)
      if(determinate):
        print(f"La expresion regular {line} esta balanceada")
      else:
        print(f"La expresion regular {line} no esta balanceada")
getExpresions_file("/Laboratorios_Teoria_Computacion-/Lab2/ejercicio2/file_reader.txt")
