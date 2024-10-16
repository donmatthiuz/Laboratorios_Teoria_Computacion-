import graphviz
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
def build_tree(derivations):
    nodes = {}
    id_counter = 0

    for deriv in derivations:
        left_data, right_data, parent_data = deriv
        
       
        if parent_data not in nodes:
            nodes[parent_data] = Node(parent_data, id_counter)
            id_counter += 1
        parent = nodes[parent_data]

        if left_data not in nodes:
            nodes[left_data] = Node(left_data, id_counter)
            id_counter += 1
        parent.left = nodes[left_data]

        if right_data:
            if right_data not in nodes:
                nodes[right_data] = Node(right_data, id_counter)
                id_counter += 1
            parent.right = nodes[right_data]
    return nodes[derivations[-1][2]]



def draw_tree_graphviz(tree):
    dot = graphviz.Digraph(format='png')
    def add_edges_graphviz(tree):
        if tree is not None:
            dot.node(str(tree.id), tree.data)  
            if tree.left:
                dot.edge(str(tree.id), str(tree.left.id)) 
                add_edges_graphviz(tree.left) 
            if tree.right:
                dot.edge(str(tree.id), str(tree.right.id)) 
                add_edges_graphviz(tree.right)  
    add_edges_graphviz(tree) 
    dot.render('CYK_tree_image', view=False)  

