from shuntingYard import *
expresion = '(a*|b*)+'
valor, pasos = infixToPostfix(expresion)
print(valor)