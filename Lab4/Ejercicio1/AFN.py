import matplotlib.pyplot as plt
import networkx as nx
from Node import *
from shuntingYard import *

class AFN:
    def __init__(self, Q, Alfabeto, q0, F, S):
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
    return AFN(set([q0, q1]), set([label]), q0, q1, [transicion]), statecounter + 2

def CleanOperator(statecounter, Nt):
    q0 = Estado(statecounter+1)
    qf = Estado(statecounter+2)
    transiciones = []
    transiciones.append(Transicion(q0, qf, 'ε'))
    transiciones.append(Transicion(q0, Nt.q0, 'ε'))
    for final_state in Nt.F:
        transiciones.append(Transicion(final_state, Nt.q0, 'ε'))
        transiciones.append(Transicion(final_state, qf, 'ε'))
    return AFN(set([q0, qf]).union(Nt.Q), set(['ε']).union(Nt.Alfabeto), q0, qf, transiciones), statecounter + 2

def orOperator(statecounter, Nt, Nf):
    q0 = Estado(statecounter+1)
    qf = Estado(statecounter+2)
    transiciones = [
        Transicion(q0, Nt.q0, 'ε'),
        Transicion(q0, Nf.q0, 'ε'),
        Transicion(Nt.F, qf, 'ε'),
        Transicion(Nf.F, qf, 'ε')
    ]
    return AFN(set([q0, qf]).union(Nt.Q).union(Nf.Q), set(['ε']).union(Nt.Alfabeto).union(Nf.Alfabeto), q0, qf, transiciones), statecounter + 2

def Concatenate(Nt, Nf):
    for trans in Nt.S:
        if trans.qf == Nt.F:
            trans.qf = Nf.q0
    Nt.F = Nf.F
    return AFN(Nt.Q.union(Nf.Q), Nt.Alfabeto.union(Nf.Alfabeto), Nt.q0, Nf.F, Nt.S + Nf.S), None

def createTransitions(statecounter, tree):
    if tree is not None:
        if tree.data.isalnum():
            return normalTransition(statecounter, tree.data)
        elif tree.data == '*':
            Nt, statecounter = createTransitions(statecounter, tree.left)
            return CleanOperator(statecounter, Nt)
        elif tree.data == '|':
            Nt, statecounter = createTransitions(statecounter, tree.left)
            Nf, statecounter = createTransitions(statecounter, tree.right)
            return orOperator(statecounter, Nt, Nf)
        elif tree.data == ' ':
            Nt, statecounter = createTransitions(statecounter, tree.left)
            Nf, statecounter = createTransitions(statecounter, tree.right)
            return Concatenate(Nt, Nf)
    return None, statecounter

def buildAFN(tree):
    statecounter = 0
    afn, _ = createTransitions(statecounter, tree)
    return afn

def plotAFN(afn):
    G = nx.DiGraph()
    
    # Filtrar estados sin transiciones
    nodes_with_edges = set()
    for trans in afn.S:
        nodes_with_edges.add(trans.q0.numero)
        nodes_with_edges.add(trans.qf.numero)
    
    # Add nodes
    for estado in afn.Q:
        if estado.numero in nodes_with_edges or estado.numero == afn.q0.numero:
            shape = 'o'  
            color = 'lightblue'
            if estado == afn.q0:
                shape = 'o'  
                color = 'red'
            
            G.add_node(estado.numero, shape=shape, color=color)
    
    for trans in afn.S:
        if trans.q0.numero in G.nodes and trans.qf.numero in G.nodes:
            G.add_edge(trans.q0.numero, trans.qf.numero, label=trans.valor)
    
    # Layout sin especificar la posición horizontal
    pos = nx.spring_layout(G)

    node_shapes = set(nx.get_node_attributes(G, 'shape').values())
    for shape in node_shapes:
        nx.draw_networkx_nodes(
            G, pos, 
            nodelist=[n for n in G.nodes if G.nodes[n]['shape'] == shape], 
            node_size=500, 
            node_color=[G.nodes[n].get('color', 'lightblue') for n in G.nodes if G.nodes[n]['shape'] == shape], 
            node_shape=shape
        )
    
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    plt.axis('off')  # Turn off the axis
    plt.show()


regex = "a*"
postfix, _ = infixToPostfix(regex)
root = build_tree(postfix)
afn = buildAFN(root)
plotAFN(afn)
