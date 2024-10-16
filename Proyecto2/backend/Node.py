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
    dot.render('binary_tree_image', view=False)  

