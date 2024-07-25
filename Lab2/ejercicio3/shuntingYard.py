from Stack import Stack
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
  return precedencias.get(c, 6)

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
  return res

def infixToPostfix(regex):
  postfix = ""
  stack = Stack()
  formattedRegEx = formatRegEx(regex)
  for c in formattedRegEx:
    if (c == '('):
      stack.push(c)
    elif (c == ')'):
      while (stack.peek() != '('):
        postfix += stack.pop()
      stack.pop()
    else:
      while (stack.size() > 0):
        peekedChar = stack.peek()
        peekedCharPrecedence = getPrecedence(peekedChar)
        currentCharPrecedence = getPrecedence(c)
        if (peekedCharPrecedence >= currentCharPrecedence):
           postfix += stack.pop()
        else:
          break
      stack.push(c)
  while (stack.size() > 0):
    postfix += stack.pop()
  return postfix

