from shuntingYard import format_to_based_expression, infixToPostfix

# Ejemplo de uso
regex = r"if\([ae]+\)\{[ei]+\}(\n(else\{[jl]+\}))?"
formatted_expression = format_to_based_expression(regex)
print(formatted_expression)
postfix, steps = infixToPostfix(formatted_expression)
print(postfix)

print(format_to_based_expression("[ae03]+@[ae03]+.(com|net|org)(.(gt|cr|co))?"))


def contains_backslash(s):
    return '\\' in s

# Ejemplo de uso
cadena = "Esto es un ejemplo con una barra invertida ."
print(contains_backslash(cadena))  # Esto imprimirá: True

def contains_backslash(s):
    return '\\' in s

def process_regex(regex):
    if contains_backslash(regex):
        # Asignar la cadena como raw string (cadena sin formato)
        regex = r"{}".format(regex)
    return regex

# Ejemplo de uso
regex = "if\\([ae]+\\)\\{[ei]+\\}(\\n(else\\{[jl]+\\}))?"
processed_regex = process_regex(regex)
print(processed_regex)
