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
    def __init__(self, numero, estados_AFN = []):
        self.numero = numero
        self.estados_AFN = estados_AFN


def subset_Algoritm(AFN):
  afd = AFD(AFN)
   #algoritmo creacion de subconjuntos
  for s in AFN.Alfabeto:
    for T in afd.Q_:
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
  return afd


regex = "a*b*"
postfix, _ = infixToPostfix(regex)
root = build_tree(postfix)
afn = buildAFN(root)
# print(afn)
#afn.graphicAFN()
afd = subset_Algoritm(afn)
print(afd)
   