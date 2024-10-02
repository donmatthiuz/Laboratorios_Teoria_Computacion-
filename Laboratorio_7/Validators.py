operadores = ['|']
productionOperator = ['→']
def validateNonTerminal (text):
  return text.isupper() and text.isalpha()

def validateTerminal (text):
  return not validateNonTerminal(text) and text not in operadores and text not in productionOperator