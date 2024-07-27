from shuntingYard import *


print("El simbolo (<) significa que termina la expresion regular y el espacio en blanco concatenacion")
def getExpresions_file_Postfix (filename):
  enuncements = ['a)','b)','c)','d)','e)','f)','g)','h)']
  n = 0
  steps = []
  expresion = []
  postfixes = []
  with open(filename, "r", encoding='utf-8') as file:
    lines = file.read().splitlines()
    for line in lines:
      postfix, step = infixToPostfix(line)
      print(f"\n{enuncements[n]}")
      print(f"Infix: {line}<")
      print(f"Postfix: {postfix}<")
      steps.append(step)
      expresion.append(line)
      postfixes.append(postfix)
      n += 1

  salir = True
  while salir:
    revisar_pasos = input("\nIngrese la letra del ejercicio para ver los pasos presione cualquier tecla para salir:  ")
    pasos = []
    expre = ''
    post = ''
    if (revisar_pasos == 'a'):
      pasos = steps[0]
      expre = expresion[0]
      post = postfixes[0]
    elif (revisar_pasos == 'b'):
      pasos = steps[1]
      expre = expresion[1]
      post = postfixes[1]
    elif (revisar_pasos == 'c'):
      pasos = steps[2]
      expre = expresion[2]
      post = postfixes[2]
    elif (revisar_pasos == 'd'):
      pasos = steps[3]
      expre = expresion[3]
      post = postfixes[3]
    elif (revisar_pasos == 'e'):
      pasos = steps[4]
      expre = expresion[4]
      post = postfixes[4]
    elif (revisar_pasos == 'f'):
      pasos = steps[5]
      expre = expresion[5]
      post = postfixes[5]
    elif (revisar_pasos == 'g'):
      pasos = steps[6]
      expre = expresion[6]
      post = postfixes[6]
    elif (revisar_pasos == 'h'):
      pasos = steps[7]
      expre = expresion[7]
      post = postfixes[7]
    else:
      salir = False
      break
    print(f"\nExpresion inicial: {expre}<")
    print(f"\nPasos: ")
    for paso in pasos:
        print(f"   -{paso}")
    print(f"Expresion final : {post}<")

getExpresions_file_Postfix("/Laboratorios_Teoria_Computacion-/Lab2/ejercicio3/file_reader.txt")
