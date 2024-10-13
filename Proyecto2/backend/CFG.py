from Validators import *
import copy
from Regex import Regex
from Reader import *
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
  
  def get_productions(self, nonterminal):
    productions = []
    for production in self.P:
        if production.v_ == nonterminal:
            productions.append(production)
    return productions
  
  def remove_production(self, nonterminal, terminal):
    self.P = [prod for prod in self.P if not (prod.v_ == nonterminal and prod.t_ == terminal)]

  def quit_epsilon(self):
    copy_productions = copy.deepcopy(self.P)
    #lo hacemos set para que no se dupliquen
    anulables = set()
    #verificamos los que tienen epsilon
    for produccion in self.P:
      if produccion.t_ == 'ε':
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
    copy_productions = [prod for prod in self.P if prod.t_ != 'ε']

    for prod in self.P:
      #ahora si alguna produccion tiene simbolos anulables entonces vamos a generar las nuevas producciones 
      if any(simbolo in prod.t_ for simbolo in anulables):
        lista = self.generar_combinaciones(produccion=prod.t_, anulables=anulables)
        for comb in lista:
          if comb and not self.buscar_produccion(nonterminal=prod.v_, terminal=comb):
            produccion_combinacion = Production(nonterminal=prod.v_, terminal=comb)
            copy_productions.append(produccion_combinacion)
    # Aqui ya tenemos las producciones sin epsilon ahora las igualamos
    self.P =[]
    self.P = copy_productions
  
  def eliminate_unari_productions(self):
    pares = []
    for produccion in self.P:
        if len(produccion.t_) == 1 and validateNonTerminal(produccion.t_):
            pares.append([produccion.v_, produccion.t_])
    nuevos_pares = []
    for par in pares:
        v1, v2 = par
        for produccion in pares:
            if produccion[0] == v2:
                v3 = produccion[1]
                if [v1, v3] not in pares and [v1, v3] not in nuevos_pares:
                    nuevos_pares.append([v1, v3])  
    pares_unarios  = pares + nuevos_pares
    
    # encontrar producciones de los pares
    print(f"Pares unarios: {pares_unarios}")
    for par in pares_unarios:
      producciones_t = self.get_productions(par[1])
      producciones_t = producciones_t
      for produc in producciones_t:
          if len(produc.t_) > 1 and not self.buscar_produccion(nonterminal=par[0] , terminal=produc.t_):
            generar_nueva_produccion = Production(nonterminal=par[0], terminal=produc.t_)
            self.P.append(generar_nueva_produccion)
      self.remove_production(nonterminal=par[0], terminal=par[1])
    


class Production(object):
  def __init__(self, nonterminal, terminal):
    self.v_ = nonterminal
    self.t_ = terminal

regx = Regex()
regx.load_filename('.\\file.txt')
regx.validateChains()
cfg = CFG(regx)
cfg.quit_epsilon()
cfg.eliminate_unari_productions()
rede = Reader(cfg=cfg)
rede.show_CFG_productions()
print("Gramatica Resultante:")
print(rede.string_P)