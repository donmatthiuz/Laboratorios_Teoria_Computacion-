from shuntingYard import *
expresion = '(a|b)*abb'
valor, pasos = infixToPostfix(expresion)
print(f'{valor}.')
