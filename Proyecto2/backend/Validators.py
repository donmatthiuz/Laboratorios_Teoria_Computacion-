operadores = ['|']
productionOperator = ['→']
non_terminal = []

def validateNonTerminal (text):
  return (text.isupper() and text.isalpha() and len(text) == 1) or (text in non_terminal)

def set_nonterminal (lista):
  non_terminal.extend(lista)

def validateTerminal (text):
  return not validateNonTerminal(text) and text not in operadores and text not in productionOperator