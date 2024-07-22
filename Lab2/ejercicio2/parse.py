
def parsechain(cadena):
    cadena_return = []
    i = 0
    while i < len(cadena):
        cd = cadena[i]
        
        if cd == '(' or cd == '[' or cd == '{':
            cadena_restante, indice = parsechain(cadena[i + 1:])
            cadena_return.append(cadena_restante)
            i += indice + 1
        elif cd == ')' or cd == ']' or cd == '}':
            return cadena_return, i
        else:
            cadena_return.append(cd)
        i += 1
    return cadena_return

def determinate_balance(parse_chain):
  #si esta balanceada no devolvera el indice donde se quedo , ya que este se devuelve si esta completamente cerrada.
  # lo que hace que sea una lista si esta balanceada y una tupla si no. 
  if isinstance(parse_chain, list):
    print("La expresion regular esta balanceada")
  elif isinstance(parse_chain, tuple):
    print("La expresion regular no esta balanceada")
