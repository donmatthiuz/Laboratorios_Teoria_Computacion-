from Validators import *
import copy
from Regex import Regex
class CFG(object):
  def __init__(self, regx):
    self.regex = regx.gramatica
    self.T = []
    self.V = []
    self.P =[]
    self.S = regx.gramatica[0][0]
    self.build_CFG()

  def build_CFG(self):
    for produccions in self.regex:
      simbolonoTerminal = produccions[0]
      for production in produccions:
        if production != simbolonoTerminal and production not in productionOperator and production not in operadores:
          p = Production(nonterminal=simbolonoTerminal, terminal=production)
          self.P.append(p)
        for simbol in production:
          if validateNonTerminal(simbol) and simbol not in self.V:
            self.V.append(simbol)
          elif validateTerminal(simbol) and simbol not in self.T:
            self.T.append(simbol)
  
  def buscar_produccion(self, nonterminal, terminal):
        for produccion in self.P:
            if produccion.v_ == nonterminal and produccion.t_ == terminal:
                return True  
  
  def generar_combinaciones(self, produccion, anulables):
    combinaciones = set()
    combinaciones.add(produccion)
    for simbolo in produccion:
        if simbolo in anulables:
            nueva_produccion = produccion.replace(simbolo, '', 1)
            combinaciones.add(nueva_produccion)
    return list(combinaciones)

  def quit_epsilon(self):
    copy_productions = copy.deepcopy(self.P)
    #lo hacemos set para que no se dupliquen
    anulables = set()
    #verificamos los que tienen epsilon
    for produccion in self.P:
      if produccion.v_ in self.V and produccion.t_ == 'ε':
        anulables.add(produccion.v_)
    #ahora verificamos aquellas que nos llevan a las anulables
    cambios = True
    while cambios:
      cambios = False
      for produccion in self.P:
          if all(simbolo in anulables for simbolo in produccion.t_) and produccion.v_ not in anulables:
              anulables.add(produccion.v_)
              cambios = True
    #ahora lo que vamos a Eliminar las producciones epsilonn anulables
    anulables = list(anulables)
    for i, prod in enumerate(self.P):
      if prod.v_ in anulables and prod.t_ == 'ε':
        copy_productions.pop(i)
      #ahora si alguna produccion tiene simbolos anulables entonces vamos a generar las nuevas producciones 
      elif any(simbolo in prod.t_ for simbolo in anulables):
        lista = self.generar_combinaciones(produccion=prod.t_, anulables=anulables)
        for comb in lista:
          if (comb != '') and (not self.buscar_produccion(nonterminal=prod.v_ , terminal=comb)):
            produccion_combinacion = Production(nonterminal=prod.v_, terminal=comb)
            copy_productions.append(produccion_combinacion)
    # Aqui ya tenemos las producciones sin epsilon ahora las igualamos
    self.P =[]
    self.P = copy_productions
    
class Production(object):
  def __init__(self, nonterminal, terminal):
    self.v_ = nonterminal
    self.t_ = terminal

try:
  regx = Regex()
  regx.load_filename('Laboratorio_7\\file.txt')
  regx.validateChains()
  cfg = CFG(regx)
  cfg.quit_epsilon()
except ValueError as e:
  print(f"Se produjo un error :  {e}")
