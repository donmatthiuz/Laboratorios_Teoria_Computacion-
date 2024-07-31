from shuntingYard import *
expresion = '(a|b)*abb'
valor, pasos = infixToPostfix(expresion)
print(valor)
