from shuntingYard import *
from Node import *


expresion = []
postfixes = []
def getExpresions_file_Postfix (filename):
  with open(filename, "r", encoding='utf-8') as file:
    lines = file.read().splitlines()
    for line in lines:
      postfix, step = infixToPostfix(line)
      expresion.append(line)
      postfixes.append(postfix)

getExpresions_file_Postfix("/Laboratorios_Teoria_Computacion-/Lab3/Ejercicio1/file_reader.txt")

print("\nEJERCICIO 1 GRAFICA DE ARBOL SINTACTICA EXPRESIONES REGULARES\n")
print("Ejercicios\n")
print("      a) (a*|b*)+\n")
print("      b) ((ε|a)|b*)*\n")
print("      c) (a|b)*abb(a|b)*\n")
print("      d) 0?(1?)?0*\n")

salir = True

while salir:
  valor = input("Ingrese la letra del ejercicio , cualquier otra para salir: ")
  if(valor == 'a'):
    postfix = postfixes[0]
    root = build_tree(postfix)
    draw_tree(root)
  elif(valor == 'b'):
    postfix = postfixes[1]
    root = build_tree(postfix)
    draw_tree(root)
  elif(valor == 'c'):
    postfix = postfixes[2]
    root = build_tree(postfix)
    draw_tree(root)
  elif(valor == 'd'):
    postfix = postfixes[3]
    root = build_tree(postfix)
    draw_tree(root)
  else:
    salir = False
    break
