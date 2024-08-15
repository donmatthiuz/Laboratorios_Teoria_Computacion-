import matplotlib.pyplot as plt
import networkx as nx
from shuntingYard import *

class Node:
    def __init__(self, data, id):
        self.left = None
        self.right = None
        self.data = data
        self.id = id

def build_tree(postfix):
    stack = []
    id_counter = 0 
    for char in postfix:
        if char.isalnum() or char == 'ε':  
            node = Node(char, id_counter)
            id_counter += 1
            stack.append(node)
        elif char in ['*', '|', ' ']:  
            if char == '*':
                node = Node(char, id_counter)
                node.left = stack.pop()
                id_counter += 1
            elif char in ['|', ' ']:
                node = Node(char, id_counter)
                node.right = stack.pop()
                node.left = stack.pop()
                id_counter += 1
            stack.append(node)
    return stack[0]

def add_edges(graph, tree, pos, x=0, y=0, layer=1):
    if tree is not None:
        graph.add_node(tree.id, label=tree.data, pos=(x, y))
        if tree.left:
            graph.add_edge(tree.id, tree.left.id, label="izquierdo")
            l = x - 1 / layer
            add_edges(graph, tree.left, pos, x=l, y=y-1, layer=layer+1)
        if tree.right:
            graph.add_edge(tree.id, tree.right.id, label="right")
            r = x + 1 / layer
            add_edges(graph, tree.right, pos, x=r, y=y-1, layer=layer+1)

def draw_tree(tree):
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, tree, pos)
    pos = nx.get_node_attributes(graph, 'pos')
    labels = nx.get_node_attributes(graph, 'label')
    edge_labels = nx.get_edge_attributes(graph, 'label')
    
    nx.draw(graph, pos, labels=labels, with_labels=True, arrows=False)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show()





regex = "aa"
postfix, _ = infixToPostfix(regex)
root = build_tree(postfix)

draw_tree(root)
