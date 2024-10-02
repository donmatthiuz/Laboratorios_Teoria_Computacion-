from Validators import *
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
  
  def quit_epsilon(self):
    anulables = []
    #verificamos los que tienen epsilon
    for produccion in self.P:
      if produccion.v_ in self.V and produccion.t_ == 'ε':
        anulables.append(produccion.v_)
    #ahora verificamos aquellas que nos llevan a las anulables
    cambios = True
    while cambios:
      cambios = False
      for produccion in self.P:
          if [simbolo for simbolo in anulables for simbolo in produccion.t_] and produccion.v_ not in anulables:
              anulables.append(produccion.v_)
              cambios = True

    print(anulables)

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
  print(cfg)
except ValueError as e:
  print(f"Se produjo un error :  {e}")
