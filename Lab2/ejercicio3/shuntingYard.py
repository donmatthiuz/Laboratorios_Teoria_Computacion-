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

def format_to_based_expression(regex):
    res = ""
    stack = []
    i = 0

    while i < len(regex):
        character = regex[i]

        if character == "[":
            # Manejar los corchetes como un bloque
            block = ""
            while i < len(regex) and regex[i] != "]":
                block += regex[i]
                i += 1
            block += "]"  # Añadir el cierre del bloque
            stack.append(block)
        
        elif character == "+":
            if stack:
                last = stack.pop()
                stack.append(f"({last}{last}*)")
        
        elif character == "?":
            if stack:
                last = stack.pop()
                stack.append(f"({last}|ε)")
        
        else:
            stack.append(character)
        
        i += 1
    
    res = "".join(stack)
    return res

def formatRegEx(regex):
  res = ""
  allOperators = ['|', '?', '+', '*', '^']
  binaryOperators = ['^', '|', '+']
  for i in range (len(regex)):
    c1 = regex[i]
    if ((i+1)<len(regex)):
      c2 = regex[i+1]
      res += c1
      if (c1 != '(' and c2 != ')' and (c2 not in allOperators) and (c1 not in binaryOperators)):
        res += ' '
  res += regex[-1]
  return res

def contains_backslash(s):
    return '\\' in s

def infixToPostfix(regex):
    if (contains_backslash(regex)):
        regex = r"{}".format(regex)
    postfix = ""
    steps = []
    stack = Stack()
    regex = format_to_based_expression(regex)
    formattedRegEx = formatRegEx(regex)
    escape_next = False
    inside_brackets = False
    bracket_content = ""

    for c in formattedRegEx:
        if escape_next:
            postfix += c
            steps.append(f"Agregar caracter escapador: {c}")
            escape_next = False
        elif c == '\\':
            escape_next = True
        elif c == '[':
            inside_brackets = True
            bracket_content += c
        elif c == ']' and inside_brackets:
            bracket_content += c
            postfix += bracket_content
            steps.append(f"Agregar contenido de los []: {bracket_content}")
            bracket_content = ""
            inside_brackets = False
        elif inside_brackets:
            bracket_content += c
            bracket_content = bracket_content.replace(" ", "")
        elif c.isalnum():
            postfix += c
            steps.append(f"Agregar caracter alfanumerico: {c}")
        elif c == '(':
            stack.push(c)
            steps.append(f"Pushear '(': {stack}")
        elif c == ')':
            while stack.peek() != '(':
                top = stack.pop()
                postfix += top
                steps.append(f"Pop y agregar: {top}")
            stack.pop() 
            steps.append("Pop '('")
        else:
            while stack.size() > 0 and getPrecedence(stack.peek()) >= getPrecedence(c):
                top = stack.pop()
                postfix += top
                steps.append(f"Pop y agregar: {top}")
            stack.push(c)
            steps.append(f"Pushear operador: {c} | Stack: {stack}")
    
    while stack.size() > 0:
        top = stack.pop()
        postfix += top
        steps.append(f"Pop y agregar restante: {top}")
    
    return postfix, steps


  