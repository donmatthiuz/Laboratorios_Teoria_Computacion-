
def parsechain(cadena):
    cadena_return = []
    i = 0
    while i < len(cadena):
        cd = cadena[i]
        if cd == '(':
            cadena_popup, indice = parsechain(cadena[i + 1:])
            cadena_return.append(cadena_popup)
            i += indice + 1
        elif cd == ')':
            return cadena_return, i
        else:
            cadena_return.append(cd)
        i += 1
    return cadena_return
