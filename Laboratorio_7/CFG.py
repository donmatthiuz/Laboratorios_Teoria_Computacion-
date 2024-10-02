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
      for production in produccions:
        for simbol in production:
          if validateNonTerminal(simbol) and simbol not in self.V:
            self.V.append(simbol)
          elif validateTerminal(simbol) and simbol not in self.T:
            self.T.append(simbol)
          

try:
  regx = Regex()
  regx.load_filename('Laboratorio_7\\file.txt')
  regx.validateChains()
  cfg = CFG(regx)
  print(cfg)
except ValueError as e:
  print(f"Se produjo un error :  {e}")
