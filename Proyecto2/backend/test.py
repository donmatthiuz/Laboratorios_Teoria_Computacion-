import graphviz

class Node:
    def __init__(self, data, id):
        self.left = None
        self.right = None
        self.data = data
        self.id = id  # cada nodo tiene un identificador único

def build_tree(derivations):
    # Derivations vendrá del algoritmo CYK con la forma [(left_node, right_node, parent), ...]
    nodes = {}
    id_counter = 0

    for deriv in derivations:
        left_data, right_data, parent_data = deriv
        
        # Crear o reutilizar nodos
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

    # Retornar la raíz del árbol (último nodo añadido como raíz)
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
    dot.render('derivation_tree', view=True)

# Ejemplo de derivaciones desde el algoritmo CYK
# Cada tupla es (izquierdo, derecho, padre)
derivations = [
    ('the', 'cat', 'N'),  # N -> the cat
    ('C', 'N', 'B'),      # B -> C N
    ('the', None, 'C'),   # C -> the
    ('slept', None, 'A'), # A -> slept
    ('B', 'A', 'S')       # S -> B A
]

# Construir el árbol desde las derivaciones
tree = build_tree(derivations)

# Dibujar el árbol
draw_tree_graphviz(tree)
