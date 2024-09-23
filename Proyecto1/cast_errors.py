def is_valid_operator_usage(regex):
    operand_stack = []
    binaryOperators = ['^', '|', '+']

    for i, char in enumerate(regex):
        if char.isalnum() or char == 'ε': 
            if operand_stack and operand_stack[-1] == 'RESULT':
                operand_stack.pop() 
                operand_stack.append('RESULT')
            operand_stack.append(char)

        elif char in binaryOperators:
            if len(operand_stack) < 2:
                raise ValueError(f"Error en el operador binario '{char}' en la posición {i}: no hay suficientes operandos.")
            operand_stack.pop()
            operand_stack.pop()
            operand_stack.append('RESULT')

        elif char in ['?', '*']:
            if not operand_stack:
                raise ValueError(f"Error en el operador unario '{char}' en la posición {i}: no hay operandos disponibles.")
            operand_stack.pop()
            operand_stack.append('RESULT')
    print(len(operand_stack))
    if len(operand_stack) < 1:
        raise ValueError("Error: la expresión tiene operandos no utilizados o incompletos.")


    
def is_balanced(regex):
    stack = []
    for i, char in enumerate(regex):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                raise ValueError(f"Paréntesis de cierre en la posición {i} no tiene un paréntesis de apertura correspondiente.")
            stack.pop()

    if stack:
        raise ValueError(f"Paréntesis de apertura en la posición {stack[-1]} no tiene un paréntesis de cierre correspondiente.")
