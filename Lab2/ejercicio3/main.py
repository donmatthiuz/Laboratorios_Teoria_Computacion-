from shuntingYard import *

# Ejemplo de uso:
regex = "a(b|c)+d"
postfix = infixToPostfix(regex)
print(f"Infix: {regex}")
print(f"Postfix: {postfix}")
