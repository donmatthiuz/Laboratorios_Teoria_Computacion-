from shuntingYard import *
expresion = '(a*|b*)+'
v, p = infixToPostfix(expresion)
print(format_to_based_expression(expresion))
print(f'{v}.')