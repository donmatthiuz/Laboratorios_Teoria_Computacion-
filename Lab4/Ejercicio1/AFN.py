import matplotlib.pyplot as plt
import networkx as nx
from Node import *
from shuntingYard import *

class AFN:
    def __init__(self, Q, Alfabeto, q0, S, F):
        self.Q = Q
        self.Alfabeto = Alfabeto
        self.q0 = q0
        self.S = S
        self.F = F

    def set_q0(self, q0):
        self.q0 = q0

    def set_qf(self, qf):
        self.F = {qf}

class Transicion:
    def __init__(self, initialstate, finalstate, valor):
        self.q0 = initialstate
        self.qf = finalstate
        self.valor = valor

class Estado:
    def __init__(self, numero, aceptacion=False):
        self.numero = numero
        self.aceptacion = aceptacion

    def set_to_Acept(self):
        self.aceptacion = True

def normalTransition(statecounter, label):
    q0 = Estado(statecounter+1)
    q1 = Estado(statecounter+2)
    transicion = Transicion(q0, q1, label)
    return AFN(set([q0, q1]), set([label]), q0, {q1}, transicion)

def CleanOperator(statecounter, Nt):
    q0 = Estado(statecounter+1)
    qf = Estado(statecounter+2)
    transiciones = [
        Transicion(q0, qf, 'ε'),
        Transicion(q0, Nt.q0, 'ε'),
        Transicion(Nt.F, Nt.q0, 'ε'),
        Transicion(Nt.F, qf, 'ε')
    ]
    return AFN(set([q0, qf]).union(Nt.Q), set(['ε']).union(Nt.Alfabeto), q0, {qf}, transiciones)

def orOperator(statecounter, Nt, Nf):
    q0 = Estado(statecounter+1)
    qf = Estado(statecounter+2)
    transiciones = [
        Transicion(q0, Nt.q0, 'ε'),
        Transicion(q0, Nf.q0, 'ε'),
        Transicion(Nt.F, qf, 'ε'),
        Transicion(Nf.F, qf, 'ε')
    ]
    return AFN(set([q0, qf]).union(Nt.Q).union(Nf.Q), set(['ε']).union(Nt.Alfabeto).union(Nf.Alfabeto), q0, {qf}, transiciones)

def Concatenate(Nt, Nf):
    Nt.F = {Nf.q0}
    return AFN(Nt.Q.union(Nf.Q), Nt.Alfabeto.union(Nf.Alfabeto), Nt.q0, Nf.F, Nt.S + Nf.S)

def createTransitions(statecounter, tree):
    if tree is not None:
        if tree.data.isalnum():
            return normalTransition(statecounter, tree.data)
        elif tree.data == '*':
            Nt = createTransitions(statecounter, tree.left)
            return CleanOperator(statecounter, Nt)
        elif tree.data == '|':
            Nt = createTransitions(statecounter, tree.left)
            Nf = createTransitions(statecounter, tree.right)
            return orOperator(statecounter, Nt, Nf)
        elif tree.data == ' ':
            Nt = createTransitions(statecounter, tree.left)
            Nf = createTransitions(statecounter, tree.right)
            return Concatenate(Nt, Nf)
    return None

def buildAFN(tree):
    statecounter = 0
    afn = createTransitions(statecounter, tree)
    return afn

def plotAFN(afn):
    G = nx.DiGraph()
    
    # Add nodes
    for estado in afn.Q:
        shape = 'circle'
        color = 'lightblue'
        if estado == afn.q0:
            shape = 's'
            color = 'red'
        if estado in afn.F:
            shape = 'o'
            color = 'green'
        G.add_node(estado.numero, shape=shape, color=color)
    
    # Add edges
    for trans in afn.S:
        G.add_edge(trans.q0.numero, trans.qf.numero, label=trans.valor)
    
    pos = nx.spring_layout(G)
    node_shapes = set(nx.get_node_attributes(G, 'shape').values())
    for shape in node_shapes:
        nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=[G.nodes[n].get('color', 'lightblue') for n in G.nodes], node_shape=shape)
    
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    plt.show()


regex = "(a*)"
postfix, _ = infixToPostfix(regex)
root = build_tree(postfix)
afn = buildAFN(root)
plotAFN(afn)
