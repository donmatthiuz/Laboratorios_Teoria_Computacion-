import matplotlib.pyplot as plt
import networkx as nx

#Clase Node cita: 
#tutorialspoint . (2024). tutorialspoint. 
# Obtenido de Python - Binary Tree: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def build_tree(postfix):
    stack = []
    for char in postfix:
        if char.isalnum() or char == 'ε':  # operand (ε for epsilon, a, b)
            node = Node(char)
            stack.append(node)
        elif char in ['*', '|', ' ']:  # operator
            if char == '*':
                node = Node(char)
                node.left = stack.pop()
            elif char == '|':
                node = Node(char)
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
    return stack[0]

def add_edges(graph, tree, pos, x=0, y=0, layer=1):
    if tree is not None:
        graph.add_node(tree.data, pos=(x, y))
        if tree.left:
            graph.add_edge(tree.data, tree.left.data)
            l = x - 1 / layer
            add_edges(graph, tree.left, pos, x=l, y=y-1, layer=layer+1)
        if tree.right:
            graph.add_edge(tree.data, tree.right.data)
            r = x + 1 / layer
            add_edges(graph, tree.right, pos, x=r, y=y-1, layer=layer+1)

def draw_tree(tree):
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, tree, pos)
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw(graph, pos, with_labels=True, arrows=False)
    plt.show()

# Expresión postfix
postfix = 'ab|*'

# Construir el árbol de la expresión postfix
root = build_tree(postfix)

# Dibujar el árbol
draw_tree(root)
