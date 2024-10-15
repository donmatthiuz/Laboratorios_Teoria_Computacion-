from Validators import *
import copy
from Regex import Regex
from Reader import *
from Production import *
from CYK import *
from Validators import *
from Parser import *
class CFG(object):
  def __init__(self, regx):
    self.regex = regx.gramatica
    self.T = []
    self.V = copy.deepcopy(non_terminal)
    self.P =[]
    self.S = regx.gramatica[0][0]
    self.build_CFG()
  
  def build_CFG(self):
    for produccions in self.regex:
      simbolonoTerminal = produccions[0]
      producciones_separadas = separar_por_or(produccions)
      for separacion in producciones_separadas:
        t_ = ' '.join(separacion)
        p = Production(nonterminal=simbolonoTerminal, terminal=t_)
        self.P.append(p)
        for s in separacion:
           if validateTerminal(s) and s not in self.T:
              self.T.append(s)

  def delete_recursividad(self):
     for produccions in self.regex:
        simbolonoTerminal = produccions[0]
        producciones_separadas = separar_por_or(produccions)
        if simbolonoTerminal == producciones_separadas[0][0]:
          alpha = producciones_separadas[0][1:]
          beta = producciones_separadas[1:]
          #Eliminar todas las producciones en self.P
          self.remove_all_production(nonterminal=simbolonoTerminal)
          #creamos un nuevo simbolo
          new_simbolo = f"{simbolonoTerminal}'"
          #ahora creamos sus producciones
          for p_b in beta:
             union1 = ' '.join(p_b)
             union = f'{union1} {new_simbolo}'
             prod = Production(nonterminal=simbolonoTerminal, terminal=union)
             self.P.append(prod)
          #ahora agregamos alpha
          alpha_new = f"{' '.join(alpha)} {new_simbolo}"
          self.P.append(Production(nonterminal=new_simbolo, terminal=alpha_new))
          self.P.append(Production(nonterminal=new_simbolo, terminal='ε'))
          #lo agregamos a los self.V
          self.V.append(new_simbolo)
     
  def remove_production_por_terminal(self, terminal):
    self.P = [prod for prod in self.P if terminal not in prod.t_]

  def buscar_produccion(self, nonterminal, terminal):
        for produccion in self.P:
            if produccion.v_ == nonterminal and produccion.t_ == terminal:
                return True  
  
  def generar_combinaciones(self, produccion, anulables):
    # Convertir la producción en una lista de símbolos para manipularlos individualmente
    simbolos = produccion.split()
    combinaciones = set()
    
    # Inicialmente agregar la producción original
    combinaciones.add(' '.join(simbolos))
    
    # Generar combinaciones eliminando anulables
    for i, simbolo in enumerate(simbolos):
        if simbolo in anulables:
            # Crear una nueva combinación sin el símbolo anulable
            nueva_produccion = simbolos[:i] + simbolos[i+1:]
            combinaciones.add(' '.join(nueva_produccion))
    
    return list(combinaciones)

  
  def get_productions(self, nonterminal):
    productions = []
    for production in self.P:
        if production.v_ == nonterminal:
            productions.append(production)
    return productions
  
  def get_productions_terminal(self, terminal):
    productions = []
    for production in self.P:
        if terminal in production.t_:
            productions.append(production.v_)
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
        if  validateNonTerminal(produccion.t_):
            pares.append([produccion.v_, produccion.t_])
    for par in pares:
        v1, v2 = par
        for produccion in pares:
            if produccion[0] == v2:
                v3 = produccion[1]
                if [v1, v3] not in pares:
                    pares.append([v1, v3])  
    pares_unarios  = pares
    # encontrar producciones de los pares
    for par in pares_unarios:
      producciones_t = self.get_productions(par[1])
      for produc in producciones_t:
          separados_por_V = produc.t_.split(' ')
          if validateTerminal(' '.join(separados_por_V)) and not self.buscar_produccion(nonterminal=par[0] , terminal=produc.t_):
            generar_nueva_produccion = Production(nonterminal=par[0], terminal=produc.t_)
            self.P.append(generar_nueva_produccion)
      self.remove_production(nonterminal=par[0], terminal=par[1])
  
  def remove_all_production(self, nonterminal):
    for product in self.P:
        if product.v_ == nonterminal:
          self.remove_production(nonterminal=nonterminal, terminal=product.t_)

  def quit_noproductions_symbols(self):
    productive_symbols = set(self.T)
    changed = True

    while changed:
        changed = False
        for v_ in self.V:
            productions = self.get_productions(v_)
            for prod in productions:
                if any(symbol in productive_symbols or symbol in self.T for symbol in prod.t_):
                    if v_ not in productive_symbols:
                        productive_symbols.add(v_)
                        changed = True
    #si encuentra una que no produce la elimina
    for non_ter in self.V:
       if non_ter not in productive_symbols:
          self.V.remove(non_ter)
          self.remove_all_production(nonterminal=non_ter)
          self.remove_production_por_terminal(terminal=non_ter)


       

  def quit_unreachable_nonterminals(self):
    reachable_symbols = set([self.S])
    #derivacion directa
    for v_ in self.V:
        productions = self.get_productions_terminal(v_)
        if self.S in productions:
            reachable_symbols.add(v_)
    
    for non_ter in self.V:
        if non_ter not in reachable_symbols:
            self.V.remove(non_ter)
            self.remove_all_production(nonterminal=non_ter)
            self.remove_production_por_terminal(terminal=non_ter)

  def delete_unseless_symbols(self):
    self.quit_noproductions_symbols()
    self.quit_unreachable_nonterminals()
  
  def convert_terminals(self):
     nuevas_producciones =  {}
     nuevos_simbolos = []
     i =0
     for t in self.T:
        if t != 'ε':
          nonterminal_new = 'α'
          i+=1 
          nonterminal_new += str(i)
          production = Production(nonterminal=nonterminal_new, terminal=t)
          self.P.append(production)
          self.V.append(nonterminal_new)
          nuevas_producciones[t] = nonterminal_new
          nuevos_simbolos.append(nonterminal_new)
     for p in self.P:
        separados = p.t_.split(' ')
        if any(elemento in self.V for elemento in separados) or len(separados) >1:
          for terminal in separados:
            if terminal in self.T and p.v_ not in nuevos_simbolos:
                p.t_ = p.t_.replace(terminal, nuevas_producciones[terminal])

  def separate_terminals(self):
    i = 0
    nuevos_simbolos = []
    nuevas_producciones =  {}
    for p in self.P:
        separados = p.t_.split(' ')
        while len(separados) > 2: 
          separar = [separados.pop(), separados.pop()]
          separar.reverse()
          resultado = ' '.join(separar)
          nuevo = 'β' + str(i)
          i += 1
          producciones_donde_esta = self.get_productions_terminal(resultado)
          booleano =any(elemento in nuevos_simbolos for elemento in producciones_donde_esta)
          if not booleano:
            self.P.append(Production(nonterminal=nuevo, terminal=resultado))
            self.V.append(nuevo)
            nuevos_simbolos.append(nuevo)          
            separados.append(nuevo)
            nuevas_producciones[resultado] = nuevo
            p.t_ = ' '.join(separados)
          else:
            
            separados.append(nuevas_producciones[resultado])
            p.t_ = ' '.join(separados)


  
  
  
  def convert_to_Chumsky(self):
    self.delete_recursividad()
    self.quit_epsilon()
    self.eliminate_unari_productions()
    self.delete_unseless_symbols()
    self.convert_terminals()
    self.separate_terminals()
             
                 

regx = Regex()
regx.load_filename('Proyecto2\\backend\\file.txt')
regx.validateChains()
cfg = CFG(regx)
cfg.convert_to_Chumsky()
cyk = CYK(cfg=cfg, w='b a a b a')
print(cyk.algoritm())
print(cyk.table)


rede = Reader(cfg=cfg)
rede.show_CFG_productions()
print("Gramatica Resultante:")
print(rede.string_P)