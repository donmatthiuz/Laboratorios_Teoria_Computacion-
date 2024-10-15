from Validators import validateNonTerminal, validateTerminal, set_nonterminal, get_nonTerminal
import copy

class Regex(object):  
  def __init__(self):
    self.lines = []
    self.gramatica = []

  def load_filename(self,filename):
    with open(filename, "r", encoding='utf-8') as file:
      lines = file.read().splitlines()
    for line in lines:
      splitline = line.split()
      self.lines.append(splitline)
  
  def show_Gramatica(self):
    gram = ""
    for l in self.gramatica:
      for carac in l:
        gram += f"{carac} "
      gram+= "\n"
    return gram
        

  def load_by_text(self, text):
    lines = text.splitlines()
    for line in lines:
      splitline = line.split()
      self.lines.append(splitline)
  
  def dividebyOr(self):
    for line in self.lines:
        i = 0 
        while i < len(line):
            simbol = line[i]
            if "|" in simbol and len(simbol) > 1:
                separados = simbol.split('|')
                new_list = []
                for part in separados:
                    new_list.append(part)
                    new_list.append('|')

                new_list.pop()
                line.pop(i)
                line[i:i] = new_list
                i += len(new_list)
            else:
                i += 1

  def get_nonTerminals(self):
    all_nonterminals = set()
    for productions in self.lines:
      all_nonterminals.add(productions[0])
      for p in productions:
        if validateNonTerminal(p) and p not in get_nonTerminal():
          all_nonterminals.add(p)
    all_nonterminals = list(all_nonterminals)
    set_nonterminal(all_nonterminals)
    

  def validateChains(self):
    #separar por ors
    #validar si inicia con un
    #print(self.lines)
    #aqui seteamos los nonterminales
    self.get_nonTerminals()
    self.dividebyOr()
    self.gramatica = copy.deepcopy(self.lines)
    for index, productions in enumerate(self.lines):
      inicial = productions.pop(0)
      flecha =productions.pop(0)
      if validateNonTerminal(inicial):
        if flecha == "→":
          stack = []
          for i, produccion in enumerate(productions):
              if produccion == '|':
                if len(stack) >0:
                  if i + 1 < len(productions) and productions[i + 1] != '':
                    stack.pop()
                  else:
                    raise ValueError(f"En la fila {index+1} hay una produccion vacia despues del or")
                else:
                  raise ValueError(f"En la fila {index+1} hay una produccion faltante o el simbolo | sobra en la posicion {i}")  
              else:
                stack.append(produccion)
        else:
          raise ValueError(f"En la fila {index+1} no tiene una flecha → que indica la produccion")  
      else:
        raise ValueError(f"En la fila {index+1} no inicia la produccion con un no terminal")
