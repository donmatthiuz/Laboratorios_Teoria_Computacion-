import matplotlib.pyplot as plt
import networkx as nx

#Clase Node cita: 
#tutorialspoint . (2024). tutorialspoint. 
# Obtenido de Python - Binary Tree: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
class Node:
    def __init__(self, data, id):
        self.left = None
        self.right = None
        self.data = data
        self.id = id  #se crea un id porque si agregamos el mismo nombre al nodo se une a varios lados del arbol
        #cada valor es unico en la cadena

#algoritmo de agregacion al arbol
def build_tree(postfix):
    stack = []
    id_counter = 0 
    for char in postfix:
        if char.isalnum() or char == 'ε':  
            node = Node(char, id_counter)  #solo agregamos el nodo
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
            #se hace esto porque * es de mayor presedencia que or. Y se aplicadirectamente a un valor unico
    return stack[0]

#a;adir las aristas al arbol . 
def add_edges(graph, tree, pos, x=0, y=0, layer=1):
    if tree is not None:
        graph.add_node(tree.id, label=tree.data, pos=(x, y))
        if tree.left:
            graph.add_edge(tree.id, tree.left.id)
            l = x - 1 / layer
            add_edges(graph, tree.left, pos, x=l, y=y-1, layer=layer+1)
        if tree.right:
            graph.add_edge(tree.id, tree.right.id)
            r = x + 1 / layer
            add_edges(graph, tree.right, pos, x=r, y=y-1, layer=layer+1)

#dibujar el arbol del tree
def draw_tree(tree):
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, tree, pos)
    pos = nx.get_node_attributes(graph, 'pos')
    labels = nx.get_node_attributes(graph, 'label')
    nx.draw(graph, pos, labels=labels, with_labels=True, arrows=False)
    plt.show()


postfix = '0ε|1ε|ε| 0* '

root = build_tree(postfix)

draw_tree(root)
