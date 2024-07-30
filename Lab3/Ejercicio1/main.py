from shuntingYard import *
expresion = '((ε|a)|b*)*'
valor, pasos = infixToPostfix(expresion)
print(valor)
