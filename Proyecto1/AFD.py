import graphviz
from Node import *
from shuntingYard import *
from AFN import *

class AFD:
  def __init__(self, AFN):
    
    self.Alfabeto_ = AFN.Alfabeto
    self.q0 = Estado_AFD(0, estados_AFN=AFN.epsilon_closure({AFN.q0}))
    self.S_ = []
    self.F_ = []
    self.Q_=  []
    self.DfAD_states = []
    self.DfAD_states.append(AFN.epsilon_closure({AFN.q0}))
    self.Q_.append(self.q0)
    self.state_count = 0  

  def set_q0(self, q0):
    self.q0 = q0

  def set_qf(self, qf):
    self.F_ = {qf}
  
  def graphicAFN(self):
    f = graphviz.Digraph('finite_state_machine', filename='automataD.gv', format='png')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='doublecircle')
    f.node(str(self.F.numero))
    f.attr('node', shape='circle')
    for transicion in self.S:
        if transicion.q0.numero == self.q0.numero:
            f.node('', style='invis')
            f.edge('', str(transicion.q0.numero))
        f.edge(str(transicion.q0.numero), 
                str(transicion.qf.numero), 
                    label=str(transicion.valor))
    f.view()


class Estado_AFD:
    def __init__(self, numero, aceptacion=False, estados_AFN = []):
        self.numero = numero
        self.aceptacion = aceptacion
        self.estados_AFN = estados_AFN

    def set_to_Acept(self):
        self.aceptacion = True

class Transicion_AFD:
    def __init__(self, initialstate, finalstate, valor):
        self.q0 = initialstate
        self.qf = finalstate
        self.valor = valor

def subset_Algoritm(AFN):
  afd = AFD(AFN)
   #algoritmo creacion de subconjuntos
  for s in AFN.Alfabeto:
    # saco de la pila a T
    T = afd.DfAD_states.pop()
    # hago el regorido en el AFN
    R = AFN.epsilon_closure(AFN.move(T, s))
    # luego lo vuelvo a meter
    afd.DfAD_states.append(T)
    if R not in afd.DfAD_states:
       afd.DfAD_states.append(R)
  return afd


regex = "a*b*"
postfix, _ = infixToPostfix(regex)
root = build_tree(postfix)
afn = buildAFN(root)
# print(afn)
#afn.graphicAFN()
afd = subset_Algoritm(afn)
print(afd)
   