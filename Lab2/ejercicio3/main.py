from shuntingYard import *

regex = "a(b|c)*d"
infixtopost = infixToPostfix(regex)
print(infixtopost)

print(formatRegEx(regex))