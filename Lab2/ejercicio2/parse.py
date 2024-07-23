
def parsechain(cadena):
    cadena_return = []
    i = 0
    while i < len(cadena):
        cd = cadena[i]
        
        if cd == '(' or cd == '[' or cd == '{':
            parseada = parsechain(cadena[i + 1:])
            if isinstance(parseada, tuple):
                cadena_restante, indice = parseada
                cadena_return.append(cadena_restante)
                i += indice + 1
            else:
               i = len(cadena)
               return (cadena_return, 0)
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
    return True
  elif isinstance(parse_chain, tuple):
    return False
