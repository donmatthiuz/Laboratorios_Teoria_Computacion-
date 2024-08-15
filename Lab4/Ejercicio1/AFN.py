import matplotlib.pyplot as plt
import networkx as nx
from Node import *

class AFN:
    def __init__(self, Q, Alfabeto, q0, S, F):
        self.Q = Q
        self.Alfabeto = Alfabeto
        self.q0 = q0
        self.S = S
        self.F = F
        

class Transicion:
    def __init__(self, initialstate, finalstate, valor):
        self.q0 = initialstate
        self.qf = finalstate
        self.valor = valor

class Estado:
   def __init__(self, numero, aceptacion = False):
      self.numero = numero
      self.aceptacion = aceptacion
   def set_to_Acept (self):
      self.aceptacion = True

def normalTransition (statecounter, label):
    q0 = Estado(statecounter+1)
    q1 = Estado(statecounter+2)
    transicion = Transicion(q0, q1, label)
    return transicion

def CleanOperator (statecounter, Nt, transiciones):
    q0 = Estado(statecounter+1)
    qf = Estado(statecounter+2)
    primera = Transicion(q0, qf, 'ε')
    transiciones.append(primera)
    segunda = Transicion(q0,Nt.q0, 'ε')
    transiciones.append(segunda)
    tercera = Transicion(Nt.qf,Nt.q0, 'ε')
    transiciones.append(tercera)
    cuarta = Transicion(Nt.qf,qf, 'ε')
    transiciones.append(cuarta)
    
    

def createTransitions(statecounter, tree, transiciones):
    if tree is not None:
        if tree.data.isalnum or tree.data == 'ε':
            transiciones.append(normalTransition(statecounter, tree.data))
        elif tree.data == '*':
            Nt = createTransitions(statecounter, tree.left, transiciones)
            transiciones.append(CleanOperator(statecounter, Nt, transiciones))
            
            
            
    
    


     

  
