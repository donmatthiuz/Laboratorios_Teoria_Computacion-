def getPrecedence (c):
  precedencias = {
    '(': 1,
    '|': 2,
    ' ': 3,
    '?': 4,
    '*': 4,
    '+': 4,
    '^': 5
  }
  return precedencias[c]

def formatRegEx(regex):
  res = ""
  allOperators = ['|', '?', '+', '*', '^']
  binaryOperators = ['^', '|']
  for i in range (len(regex)):
    c1 = regex[i]
    if ((i+1)<len(regex)):
      c2 = regex[i+1]
      res += c1
      if (c1 != '(' and c2 != ')' and (c2 not in allOperators) and (c1 not in binaryOperators)):
        res += ' '
  res += regex[-1]
  return res.strip()


