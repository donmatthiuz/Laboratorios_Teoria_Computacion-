def getPrecedence (c):
  precedencias = {
    '(': 1,
    '|': 2,
    '': 3,
    '?': 4,
    '*': 4,
    '+': 4,
    '^': 5
  }
  return precedencias[c]

def formatRegEx(regex):
  allOperators = ['|', '?', '+', '*', '^']
  binaryOperators = ['^', '|']
  for i in range (len(regex)):
    c1 = regex[i]
    if ((i+1)<len(regex)):
      c2 = regex[i+1]
