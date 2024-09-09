from shuntingYard import *
from Node import *
from AFN import *

expresion = []
postfixes = []

def menu_afn(expresion, afn):
    print(f"\nDel AFN generado por la expresion {expresion}\n")
    print("      1) Graficar el AFN\n")
    print("      2) Determinar si una cadena w pertenece al lenguaje de la expresion regular\n")
    
    inside = True
    while inside:
        seleccion = str(input("Ingrese la opcion para su ejercicio, cualquier otro para salir: "))
        if seleccion == '1':
            afn.graphicAFN()
        elif seleccion == '2':
            w = str(input("Ingrese la cadena w: "))
            print(afn.acept_Chain(w))
        else:
            inside = False

def getExpresions_file_Postfix (filename):
  with open(filename, "r", encoding='utf-8') as file:
    lines = file.read().splitlines()
    for line in lines:
      postfix, step = infixToPostfix(line)
      expresion.append(line)
      postfixes.append(postfix)

getExpresions_file_Postfix("/Laboratorios_Teoria_Computacion-/Proyecto1/file_read.txt")



salir = True

while salir:
  print("\nEJERCICIO 1 Seleccione la expresion regular a evaluar\n")
  print("Ejercicios\n")
  print("      a) (a*|b*)+\n")
  print("      b) ((ε|a)|b*)*\n")
  print("      c) (a|b)*abb(a|b)*\n")
  print("      d) 0?(1?)?0*\n")
  valor = input("Ingrese la letra del ejercicio , cualquier otra para salir: ")
  if(valor == 'a'):
    postfix = postfixes[0]
    root = build_tree(postfix)
    afn = buildAFN(root)
    menu_afn(expresion[0], afn)  

  elif(valor == 'b'):
    postfix = postfixes[1]
    root = build_tree(postfix)
    afn = buildAFN(root)
    menu_afn(expresion[1], afn)
    
  elif(valor == 'c'):
    postfix = postfixes[2]
    root = build_tree(postfix)
    afn = buildAFN(root)
    menu_afn(expresion[2], afn)
    
  elif(valor == 'd'):
    postfix = postfixes[4]
    root = build_tree(postfix)
    afn = buildAFN(root)
    menu_afn(expresion[4], afn)
    
  else:
    salir = False
    break