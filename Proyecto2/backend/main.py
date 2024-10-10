from CFG import CFG
from Reader import *
from Regex import Regex

try:
  regx = Regex()
  regx.load_filename('.\\file.txt')
  regx.validateChains()
  print("\nPROGRAMA PARA QUITAR PRODUCCIONES EPSILON\n")
  print("Gramatica Original:")
  print(regx.show_Gramatica())
  cfg = CFG(regx)
  cfg.quit_epsilon()
  rede = Reader(cfg=cfg)
  rede.show_CFG_productions()
  print("Gramatica Resultante:")
  print(rede.string_P)
except ValueError as e:
  print(f"Se produjo un error :  {e}")