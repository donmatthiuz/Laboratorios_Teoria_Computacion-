import graphviz
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

    def graphicAFN(self):
        f = graphviz.Digraph('finite_state_machine', filename='AFN_automata', format='png')
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
    
    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            for transicion in self.S:
                if transicion.q0 == state and transicion.valor == 'ε':
                    next_state = transicion.qf
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def move(self, states, symbol):
        next_states = set()
        for state in states:
            for transicion in self.S:
                if transicion.q0 == state and transicion.valor == symbol:
                    next_states.add(transicion.qf)
        return next_states

    def acept_Chain(self, w):
        current_states = self.epsilon_closure({self.q0})

        for symbol in w:
            current_states = self.epsilon_closure(self.move(current_states, symbol))

        return True if any(state == self.F for state in current_states) else False


     


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
    transiciones = [
        Transicion(q0, Nt.q0, 'ε'),
        Transicion(Nt.F, Nt.q0, 'ε'),
        Transicion(Nt.F, qf, 'ε'),
        Transicion(q0, qf, 'ε')
    ]
    transiciones.extend(Nt.S)
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
    transiciones.extend(Nt.S)
    transiciones.extend(Nf.S)
    return AFN(set([q0, qf]).union(Nt.Q).union(Nf.Q), set(['ε']).union(Nt.Alfabeto).union(Nf.Alfabeto), q0, qf, transiciones), statecounter + 2

def Concatenate(Nt, Nf, statecounter):
    for trans in Nt.S:
        if trans.qf == Nt.F:
            trans.qf = Nf.q0
    Nt.F = Nf.F
    return AFN(Nt.Q.union(Nf.Q), Nt.Alfabeto.union(Nf.Alfabeto), Nt.q0, Nf.F, Nt.S + Nf.S), statecounter

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
            return Concatenate(Nt, Nf, statecounter)
    return None, statecounter

def buildAFN(tree):
    statecounter = 0
    afn, _ = createTransitions(statecounter, tree)
    return afn