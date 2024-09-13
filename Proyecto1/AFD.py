import graphviz
from Node import *
from shuntingYard import *
from AFN import *

class AFD:
  def __init__(self, AFN):
    
    self.Alfabeto_ = [simbolo for simbolo in AFN.Alfabeto if simbolo != 'ε']
    self.q0 = Estado_AFD(0, estados_AFN=AFN.epsilon_closure({AFN.q0}))
    self.S_ = []
    self.F_ = []
    self.Q_=  []
    self.Q_.append(self.q0)
    #verficar si el q0 es uno de aceptacion
    estadosAFN = self.q0.estados_AFN
    for estado in estadosAFN:
       if estado == AFN.F:
          self.F_.append(self.q0)
    self.state_count = 0  

  def set_q0(self, q0):
    self.q0 = q0

  def set_qf(self, qf):
    self.F_ = {qf}
  
  def move_AFD(self, states, symbol):
        next_states = set()
        for state in states:
            for transicion in self.S_:
                if transicion.q0 == state and transicion.valor == symbol:
                    next_states.add(transicion.qf)
        return next_states
  
  def graphicAFD(self):
    f = graphviz.Digraph('finite_state_machine', filename='automataD.gv', format='png')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='doublecircle')
    for l in self.F_:
       f.node(str(l.numero))
    f.attr('node', shape='circle')   
    for transicion in self.S_:
        if transicion.q0.numero == self.q0.numero:
            f.node('', style='invis')
            f.edge('', str(transicion.q0.numero))
        f.edge(str(transicion.q0.numero), 
                str(transicion.qf.numero), 
                    label=str(transicion.valor))
    f.view()
    
  def separate_states(self):
     acept = []
     not_acept = []
     to_return = []
     for q in self.Q_:
        if q in self.F_:
           acept.append(q)
        else:
           not_acept.append(q)
     to_return.append(not_acept)
     to_return.append(acept)
     return to_return
        
  def minimizumAFD(self):
    P = self.separate_states() 
    W = self.separate_states()
    
    while len(W) != 0:
        A = W.pop() 
        for s in self.Alfabeto_:
            X = set() 
            for q in self.Q_:
                if self.move_AFD([q], s) & set(A):
                    X.add(q)
            
            for Y in P.copy():  
                Y_set = set(Y)  
                Y1 = Y_set & X
                Y2 = Y_set - X
                
                if Y1 and Y2: 
                    Y1_list = list(Y1)
                    Y2_list = list(Y2)
                    for p in P:
                        if set(p) == Y_set:
                            P.remove(p)
                            break
                    
                    P.append(Y1_list)
                    P.append(Y2_list)
                    
                    if Y in W: 
                        W.remove(Y)
                        W.append(Y1_list)
                        W.append(Y2_list)
                    else:
                        W.append(min(Y1_list, Y2_list, key=len))
    return P


        
   
class Estado_AFD:
    def __init__(self, numero, estados_AFN = []):
        self.numero = numero
        self.estados_AFN = estados_AFN


def subset_Algoritm(AFN):
  afd = AFD(AFN)
   #algoritmo creacion de subconjuntos
  for T in afd.Q_  :
    for s in afd.Alfabeto_:
       R = AFN.epsilon_closure(AFN.move(T.estados_AFN, s))
       estados_existentes = [i.estados_AFN for i in afd.Q_]
       if R not in estados_existentes:
          afd.state_count += 1
          new_state = Estado_AFD(afd.state_count, estados_AFN=R)
          # si existe un estado que es de aceptacion entonces lo hacemos de aceptacion
          for estado_afn in R:
             if estado_afn == AFN.F:
                afd.F_.append(new_state)
          afd.Q_.append(new_state)
          afd.S_.append(Transicion(T, new_state, s))
       else:
          estado_existente = [i for i in afd.Q_ if i.estados_AFN == R][0]
          afd.S_.append(Transicion(T, estado_existente, s))
  return afd


regex = "(a|b)*abb"
postfix, _ = infixToPostfix(regex)
root = build_tree(postfix)
afn = buildAFN(root)
# print(afn)
#afn.graphicAFN()
afd = subset_Algoritm(afn)
afd.graphicAFD()
P = afd.minimizumAFD()
print(P)
